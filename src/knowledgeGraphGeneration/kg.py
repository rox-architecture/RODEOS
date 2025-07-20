#!/usr/bin/env python3
"""
RODEOS Knowledge Graph Generation

This module creates dynamic knowledge graphs from RODEOS semantic models,
focusing on dcat:Resource and metadata fields to build interconnected
knowledge representations with normalized values.

Features:
- Dynamic graph construction from semantic models
- Value normalization using LLM to avoid duplicates
- Interactive visualization with pyvis
- NetworkX graph structure for analysis
- CLI interface consistent with other RODEOS modules
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional

import networkx as nx
from pyvis.network import Network
import requests
from ollama import chat


def validate_models_directory(models_dir: str) -> Path:
    """
    Validate that the models directory exists and contains JSON files.
    
    Args:
        models_dir: Path to the models directory
        
    Returns:
        Path object for the validated directory
        
    Raises:
        FileNotFoundError: If directory doesn't exist
        ValueError: If no JSON files found
    """
    models_path = Path(models_dir)
    
    if not models_path.exists():
        raise FileNotFoundError(f"Models directory not found: {models_dir}")
    
    if not models_path.is_dir():
        raise ValueError(f"Path is not a directory: {models_dir}")
    
    json_files = list(models_path.glob("*.json"))
    if not json_files:
        raise ValueError(f"No JSON files found in: {models_dir}")
    
    return models_path


def get_openrouter_api_key() -> str:
    """
    Get the OpenRouter API key from environment variables.
    
    Returns:
        The API key string
        
    Raises:
        ValueError: If API key is not found
    """
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENROUTER_API_KEY environment variable not found. "
            "Please set it with your OpenRouter API key."
        )
    return api_key


def check_ollama_connection() -> bool:
    """
    Check if Ollama is running and accessible.
    
    Returns:
        True if Ollama is accessible, False otherwise
    """
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        return response.status_code == 200
    except Exception:
        return False


def clean_thinking_tags(text: str) -> str:
    """
    Remove <think> and </think> tags and their content from the response.
    
    Args:
        text: Text that may contain thinking tags
        
    Returns:
        Cleaned text without thinking tags and content
    """
    cleaned = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    cleaned = re.sub(r'\n\s*\n\s*\n', '\n\n', cleaned)
    return cleaned.strip()


def call_model_remote(prompt: str, model: str, temperature: float = 0.1) -> str:
    """
    Call a remote model via OpenRouter API.
    
    Args:
        prompt: The prompt to send to the model
        model: Model name (e.g., "openai/gpt-4o-mini")
        temperature: Sampling temperature
        
    Returns:
        Model response text
        
    Raises:
        Exception: If model call fails
    """
    api_key = get_openrouter_api_key()
    
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "model": model,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": temperature,
                "max_tokens": 4096
            })
        )
        response.raise_for_status()
        result = response.json()
        
        content = result['choices'][0]['message']['content']
        return clean_thinking_tags(content)
        
    except Exception as e:
        raise Exception(f"Failed to call remote model {model}: {str(e)}")


def call_model_local(prompt: str, model: str, temperature: float = 0.1) -> str:
    """
    Call a local model via Ollama.
    
    Args:
        prompt: The prompt to send to the model
        model: Model name
        temperature: Sampling temperature
        
    Returns:
        Model response text
        
    Raises:
        Exception: If model call fails
    """
    try:
        response = chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            options={
                "num_ctx": 8192,
                "temperature": temperature,
                "min_p": 0.01,
                "repeat_penalty": 1.0,
                "top_k": 64,
                "top_p": 0.95,
            },
        )
        content = response.message.content
        return clean_thinking_tags(content)
        
    except Exception as e:
        raise Exception(f"Failed to call local model {model}: {str(e)}")


def call_model(prompt: str, model: str, use_remote: bool = True, temperature: float = 0.1) -> str:
    """
    Call either a local or remote LLM model.
    
    Args:
        prompt: The prompt to send to the model
        model: Model name to use
        use_remote: Whether to use remote API via OpenRouter
        temperature: Sampling temperature
        
    Returns:
        Model response text
        
    Raises:
        Exception: If model call fails
    """
    if use_remote:
        return call_model_remote(prompt, model, temperature)
    else:
        return call_model_local(prompt, model, temperature)


def load_semantic_models(models_dir: Path) -> List[Dict]:
    """
    Load all semantic model JSON files from the models directory.
    
    Args:
        models_dir: Path to the models directory
        
    Returns:
        List of loaded semantic model dictionaries
        
    Raises:
        Exception: If loading fails
    """
    models = []
    json_files = list(models_dir.glob("*.json"))
    
    print(f"📁 Found {len(json_files)} semantic model files")
    
    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                model_data = json.load(f)
            
            # Add source file information
            model_data['_source_file'] = json_file.name
            models.append(model_data)
            print(f"✓ Loaded: {json_file.name}")
            
        except Exception as e:
            print(f"⚠️  Warning: Failed to load {json_file.name}: {e}")
            continue
    
    return models


def extract_graph_data(models: List[Dict]) -> List[Dict]:
    """
    Extract graph-relevant data from semantic models following strict JSON structure.
    
    Args:
        models: List of semantic model dictionaries
        
    Returns:
        List of extracted graph data for each model
    """
    graph_data = []
    
    for model in models:
        try:
            resource = model.get("dcat:Resource", {})
            if not resource:
                print(f"⚠️  Warning: No dcat:Resource found in {model.get('_source_file', 'unknown')}")
                continue
            
            # Extract all key-value pairs where value is not empty
            all_properties = {}
            
            # 1. Extract direct dcat:Resource fields (excluding assets, submodels, metadata)
            for key, value in resource.items():
                if key not in ["assets", "submodels", "metadata"] and value and str(value).strip():
                    all_properties[key] = str(value).strip()
            
            # 2. Extract asset type and its properties
            assets = resource.get("assets", {})
            asset_type = None
            for asset_key, asset_value in assets.items():
                if asset_key.startswith("rodeos:") and asset_value:
                    asset_type = asset_key
                    # Add all non-empty properties from the asset
                    for prop_key, prop_value in asset_value.items():
                        if prop_value and str(prop_value).strip():
                            all_properties[prop_key] = str(prop_value).strip()
                    break
            
            # 3. Extract metadata properties
            metadata = resource.get("metadata", {})
            for key, value in metadata.items():
                if value and str(value).strip():
                    all_properties[key] = str(value).strip()
            
            # Create extracted data structure
            extracted = {
                "_source_file": model.get("_source_file", "unknown"),
                "_asset_type": asset_type or "unknown",
                "_title": all_properties.get("dcterms:title", model.get("_source_file", "unknown").replace(".json", "")),
                "_identifier": all_properties.get("dcterms:identifier", ""),
                "properties": all_properties
            }
            
            graph_data.append(extracted)
            
            # Save each extracted graph data as a JSON file in the json folder
            json_dir = Path("assets/kg/json") / "json"
            json_dir.mkdir(exist_ok=True)
            output_file = json_dir / f"{Path(extracted.get('_source_file', 'model')).stem}_graph.json"
            try:
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump(extracted, f, ensure_ascii=False, indent=2)
            except Exception as e:
                print(f"⚠️  Warning: Could not save graph data to {output_file}: {e}")
            
        except Exception as e:
            print(f"⚠️  Warning: Failed to extract data from {model.get('_source_file', 'unknown')}: {e}")
            continue
    
    print(f"✓ Extracted graph data from {len(graph_data)} models")
    return graph_data


def normalize_values(values: Set[str], model: str, use_remote: bool = True) -> Dict[str, str]:
    """
    Normalize values using LLM to avoid duplicates and synonyms.
    
    Args:
        values: Set of values to normalize
        model: Model to use for normalization
        use_remote: Whether to use remote API
        
    Returns:
        Dictionary mapping original values to normalized forms
    """
    if not values:
        return {}
    
    values_list = list(values)
    values_text = "\n".join([f"- {val}" for val in values_list])
    
    prompt = f"""
Normalize the following values to create consistent, standardized forms. Group similar values together and provide a single canonical form for each group.

VALUES TO NORMALIZE:
{values_text}

Rules:
1. Group similar values (e.g., "Roboception GmbH" and "roboception" → "Roboception GmbH")
2. Standardize company names, technical terms, and product names
3. Keep technical accuracy but ensure consistency
4. Use proper capitalization and spacing
5. Remove unnecessary whitespace or formatting

Respond with each original value followed by its normalized form, one per line:
ORIGINAL → NORMALIZED

Example:
roboception → Roboception GmbH
ROBOCEPTION GMBH → Roboception GmbH
api documentation → API Documentation
"""
    
    try:
        response = call_model(prompt, model, use_remote, temperature=0.1)
        
        # Parse response
        normalization_map = {}
        lines = response.strip().split('\n')
        
        for line in lines:
            if '→' in line:
                parts = line.split('→', 1)
                if len(parts) == 2:
                    original = parts[0].strip()
                    normalized = parts[1].strip()
                    if original in values_list:
                        normalization_map[original] = normalized
        
        # Add missing values as-is
        for value in values_list:
            if value not in normalization_map:
                normalization_map[value] = value
        
        return normalization_map
        
    except Exception as e:
        print(f"⚠️  Warning: Failed to normalize values: {e}")
        # Fallback: return values as-is
        return {value: value for value in values_list}


def build_knowledge_graph(graph_data: List[Dict], model: str, use_remote: bool = True) -> nx.Graph:
    """
    Build a NetworkX knowledge graph from the extracted data.
    
    Args:
        graph_data: List of extracted graph data
        model: Model for value normalization
        use_remote: Whether to use remote API
        
    Returns:
        NetworkX graph object
    """
    print("🔗 Building knowledge graph...")
    
    # Collect all unique values for normalization
    all_values = set()
    
    for data in graph_data:
        for value in data.get("properties", {}).values():
            if isinstance(value, str) and value.strip():
                all_values.add(value.strip())
    
    print(f"📊 Normalizing {len(all_values)} unique values...")
    value_normalization = normalize_values(all_values, model, use_remote)
    
    # Create NetworkX graph
    G = nx.Graph()
    
    for data in graph_data:
        source_file = data["_source_file"]
        asset_type = data.get("_asset_type", "unknown")
        
        # Create root node with comprehensive information
        title = data.get("_title", source_file.replace(".json", ""))
        identifier = data.get("_identifier", source_file.replace(".json", ""))
        
        # Create unique root ID
        root_id = f"{asset_type}:{title}".replace(" ", "_").replace(":", "_")
        
        # Create comprehensive root node label
        root_label = f"{asset_type}\n{title}\nID: {identifier}"
        
        # Add root node with all essential information
        G.add_node(root_id, 
                  label=root_label,
                  type="root",
                  asset_type=asset_type,
                  title=title,
                  identifier=identifier,
                  source_file=source_file,
                  size=40,  # Larger size for root nodes
                  color="#FF6B6B")
        
        # Process all properties
        for property_key, property_value in data.get("properties", {}).items():
            if not property_value or not isinstance(property_value, str):
                continue
            
            # Normalize value
            normalized_value = value_normalization.get(property_value.strip(), property_value.strip())
            
            # Create value node ID
            value_id = f"value:{normalized_value}".replace(" ", "_").replace(":", "_")
            
            # Add value node if not exists
            if not G.has_node(value_id):
                # Determine color based on property key prefix
                if property_key.startswith("dcterms:") or property_key.startswith("dcat:"):
                    node_color = "#4ECDC4"  # Teal for basic DCAT properties
                elif property_key.startswith("rodeos:"):
                    node_color = "#45B7D1"  # Blue for RODEOS-specific properties
                else:
                    node_color = "#96CEB4"  # Green for metadata properties
                
                G.add_node(value_id,
                          label=normalized_value,
                          type="value",
                          property_key=property_key,
                          size=15,
                          color=node_color)
            
            # Add edge with property as label
            G.add_edge(root_id, value_id, 
                      label=property_key,
                      property=property_key)
    
    print(f"✓ Created graph with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")
    return G


def create_visualization(graph: nx.Graph, output_dir: Path) -> Path:
    """
    Create an interactive pyvis visualization of the knowledge graph.
    
    Args:
        graph: NetworkX graph object
        output_dir: Output directory for the visualization
        
    Returns:
        Path to the generated HTML file
    """
    print("🎨 Creating interactive visualization...")
    
    # Create pyvis network
    net = Network(height="800px", width="100%", bgcolor="#222222", font_color="white")
    net.set_options("""
    var options = {
      "physics": {
        "enabled": true,
        "stabilization": {"iterations": 100},
        "barnesHut": {
          "gravitationalConstant": -8000,
          "centralGravity": 0.3,
          "springLength": 95,
          "springConstant": 0.04,
          "damping": 0.09
        }
      },
      "nodes": {
        "borderWidth": 2,
        "font": {"size": 14}
      },
      "edges": {
        "color": {"inherit": true},
        "smooth": false,
        "font": {"size": 10, "align": "middle"}
      }
    }
    """)
    
    # Add nodes
    for node_id, node_data in graph.nodes(data=True):
        # Create appropriate tooltip based on node type
        if node_data.get("type") == "root":
            tooltip = f"Asset Type: {node_data.get('asset_type', 'unknown')}\nTitle: {node_data.get('title', 'N/A')}\nIdentifier: {node_data.get('identifier', 'N/A')}\nSource: {node_data.get('source_file', 'N/A')}"
        else:
            tooltip = f"Type: {node_data.get('type', 'unknown')}\nProperty: {node_data.get('property_key', 'N/A')}\nValue: {node_data.get('label', 'N/A')}"
        
        net.add_node(node_id, 
                    label=node_data.get("label", node_id),
                    title=tooltip,
                    size=node_data.get("size", 10),
                    color=node_data.get("color", "#97C2FC"))
    
    # Add edges
    for source, target, edge_data in graph.edges(data=True):
        net.add_edge(source, target, 
                    label=edge_data.get("label", ""),
                    title=f"Property: {edge_data.get('property', 'unknown')}")
    
    # Save visualization
    html_file = output_dir / "knowledge_graph.html"
    net.save_graph(str(html_file))
    
    print(f"✓ Visualization saved to: {html_file}")
    return html_file


def save_graph_data(graph: nx.Graph, graph_data: List[Dict], output_dir: Path) -> Path:
    """
    Save graph data and statistics to JSON file.
    
    Args:
        graph: NetworkX graph object
        graph_data: Original extracted data
        output_dir: Output directory
        
    Returns:
        Path to the saved JSON file
    """
    # Create summary statistics
    stats = {
        "total_nodes": graph.number_of_nodes(),
        "total_edges": graph.number_of_edges(),
        "node_types": {},
        "asset_types": {},
        "property_prefixes": {}
    }
    
    for node_id, node_data in graph.nodes(data=True):
        node_type = node_data.get("type", "unknown")
        stats["node_types"][node_type] = stats["node_types"].get(node_type, 0) + 1
        
        if node_type == "root":
            asset_type = node_data.get("asset_type", "unknown")
            stats["asset_types"][asset_type] = stats["asset_types"].get(asset_type, 0) + 1
        elif node_type == "value":
            property_key = node_data.get("property_key", "unknown")
            prefix = property_key.split(":")[0] if ":" in property_key else "other"
            stats["property_prefixes"][prefix] = stats["property_prefixes"].get(prefix, 0) + 1
    
    # Save comprehensive data
    output_data = {
        "statistics": stats,
        "graph_structure": {
            "nodes": [
                {
                    "id": node_id,
                    "label": node_data.get("label", node_id),
                    "type": node_data.get("type", "unknown"),
                    "properties": node_data
                }
                for node_id, node_data in graph.nodes(data=True)
            ],
            "edges": [
                {
                    "source": source,
                    "target": target,
                    "property": edge_data.get("property", "unknown")
                }
                for source, target, edge_data in graph.edges(data=True)
            ]
        },
        "source_models": [data["_source_file"] for data in graph_data]
    }
    
    json_file = output_dir / "knowledge_graph_data.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Graph data saved to: {json_file}")
    return json_file


def export_for_gephi(graph: nx.Graph, output_dir: Path) -> Path:
    """
    Export NetworkX graph to GEXF format for Gephi visualization.
    
    Args:
        graph: NetworkX graph object
        output_dir: Output directory
        
    Returns:
        Path to the exported GEXF file
        
    Raises:
        Exception: If export fails
    """
    print("📈 Exporting graph for Gephi...")
    
    try:
        # Create output file path
        gexf_file = output_dir / "knowledge_graph.gexf"
        
        # NetworkX write_gexf expects all node attributes to be strings or numbers
        # Clean up any problematic attributes
        cleaned_graph = graph.copy()
        
        for node_id, node_data in cleaned_graph.nodes(data=True):
            # Ensure all attributes are serializable
            for key, value in node_data.items():
                if value is None:
                    node_data[key] = ""
                elif not isinstance(value, (str, int, float, bool)):
                    node_data[key] = str(value)
        
        for source, target, edge_data in cleaned_graph.edges(data=True):
            # Ensure all edge attributes are serializable
            for key, value in edge_data.items():
                if value is None:
                    edge_data[key] = ""
                elif not isinstance(value, (str, int, float, bool)):
                    edge_data[key] = str(value)
        
        # Export to GEXF format (Gephi's native format)
        nx.write_gexf(cleaned_graph, gexf_file)
        
        print(f"✓ Gephi file saved to: {gexf_file}")
        return gexf_file
        
    except Exception as e:
        print(f"⚠️  Warning: Failed to export graph for Gephi: {e}")
        # Create empty file as fallback
        gexf_file = output_dir / "knowledge_graph.gexf"
        gexf_file.touch()
        return gexf_file


def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Generate knowledge graphs from RODEOS semantic models",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate graph from all models (remote by default)
  python kg.py
  
  # Generate with local model
  python kg.py --local
  
  # Use specific remote model
  python kg.py --model anthropic/claude-3-haiku
  
  # Use specific local model
  python kg.py --local --model llama3.2:3b
  
  # Custom models directory
  python kg.py --models-dir custom_models
  
  # Custom output directory
  python kg.py --output-dir custom_output

Remote Requirements (default):
  - OPENROUTER_API_KEY environment variable set
  - Valid OpenRouter API key with credits

Local Requirements:
  - Ollama running locally
  - A suitable LLM model installed (e.g., qwen2.5:3b, llama3.2:3b)

Prerequisites:
  - Semantic model JSON files in assets/models directory
        """
    )
    
    parser.add_argument(
        '--models-dir',
        default='assets/models',
        help='Directory containing semantic model JSON files (default: assets/models)'
    )
    
    parser.add_argument(
        '--output-dir',
        default='assets/kg',
        help='Output directory for knowledge graph files (default: assets/kg)'
    )
    
    parser.add_argument(
        '--model',
        default='openai/gpt-4o-mini',
        help='Model to use (default: openai/gpt-4o-mini for remote, qwen2.5:3b for local)'
    )
    
    parser.add_argument(
        '--local',
        action='store_true',
        help='Use local Ollama model instead of OpenRouter API'
    )
    
    args = parser.parse_args()
    
    # Determine processing mode and model
    use_remote = not args.local
    if args.local and args.model == 'openai/gpt-4o-mini':
        # User specified --local but didn't change model, use local default
        model = 'qwen2.5:3b'
    else:
        model = args.model
    
    try:
        # Check requirements based on processing mode
        if use_remote:
            get_openrouter_api_key()
            print(f"🌐 Using remote model: {model}")
        else:
            if not check_ollama_connection():
                raise Exception("Ollama is not running. Please start Ollama service first.")
            print(f"🏠 Using local model: {model}")
        
        # Validate inputs
        models_dir = validate_models_directory(args.models_dir)
        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"🚀 Starting knowledge graph generation...")
        
        # Load semantic models
        models = load_semantic_models(models_dir)
        if not models:
            raise Exception("No valid semantic models found")
        
        # Extract graph data
        graph_data = extract_graph_data(models)
        if not graph_data:
            raise Exception("No graph data extracted from models")
        
        # Build knowledge graph
        graph = build_knowledge_graph(graph_data, model, use_remote)
        
        # Create visualization
        html_file = create_visualization(graph, output_dir)
        
        # Save graph data
        json_file = save_graph_data(graph, graph_data, output_dir)
        
        # Export graph for Gephi
        gephi_file = export_for_gephi(graph, output_dir)
        
        # Summary
        print(f"\n✅ Knowledge graph generation completed!")
        print(f"📊 Processed {len(models)} semantic models")
        print(f"🔗 Created graph with {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges")
        print(f"📁 Output directory: {output_dir}")
        print(f"🌐 Visualization: {html_file}")
        print(f"📄 Data file: {json_file}")
        print(f"📈 Gephi file: {gephi_file}")
        
    except KeyboardInterrupt:
        print(f"\n⏹️  Processing interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
