# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

RODEOS (RObotic Data EcOsystem Semantic Model) is an LLM-powered pipeline for transforming technical robotics documentation into structured semantic models. The system processes PDFs through extraction, contextualization, semantic modeling, and knowledge graph generation stages.

## Commands

### Development & Testing
```bash
# Install dependencies and activate environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv sync

# Run complete pipeline for single PDF
make process FILE=document.pdf                    # Remote processing (Mistral + OpenRouter)
make process-local FILE=document.pdf              # Local processing (Docling + Ollama)

# Batch process all PDFs in assets/pdf/
make process-batch                                # Remote batch
make process-batch-local                          # Local batch

# Generate knowledge graph from semantic models
make kg                                            # Remote LLM normalization
make kg-local                                      # Local LLM normalization
make kg-open                                       # Open visualization

# Check pipeline status
make status

# Clean generated files
make clean
```

### Direct Script Execution
```bash
# 1. PDF Extraction
uv run src/informationExtraction/mistralApiExtraction.py assets/pdf/document.pdf
uv run src/informationExtraction/localDoclingExtraction.py assets/pdf/document.pdf --enhanced

# 2. Contextualization
uv run src/contextualEnrichment/context.py assets/markdown/document_MISTRAL.md --model openai/gpt-4o-mini
uv run src/contextualEnrichment/context.py --batch --local --model qwen2.5:3b

# 3. Semantic Model Extraction
uv run src/extractInformation/extraction.py assets/markdown/document_CHUNKED.md --model openai/gpt-4o-mini
uv run src/extractInformation/extraction.py --batch --local --model qwen2.5:3b

# 4. Knowledge Graph Generation
uv run src/knowledgeGraphGeneration/kg.py --model anthropic/claude-3-haiku
uv run src/knowledgeGraphGeneration/kg.py --local --model qwen2.5:3b
```

## Architecture

### Pipeline Flow
```
PDF Documents → Markdown Extraction → Contextual Chunking → Semantic Model Generation → Knowledge Graph
```

### Key Components

1. **Information Extraction** (`src/informationExtraction/`)
   - `mistralApiExtraction.py`: Cloud-based PDF processing via Mistral AI
   - `localDoclingExtraction.py`: Privacy-first local processing with optional VLM enhancement

2. **Contextual Enrichment** (`src/contextualEnrichment/`)
   - `context.py`: LLM-based semantic chunking and context addition
   - Saves prompts to `prompts/` for transparency and audit

3. **Semantic Model Extraction** (`src/extractInformation/`)
   - `extraction.py`: Transforms chunks into RODEOS-compliant JSON models
   - Auto-classifies assets as Dataset/Model/Service
   - Integrates AAS submodels from `assets/submodels/`

4. **Knowledge Graph Generation** (`src/knowledgeGraphGeneration/`)
   - `kg.py`: Builds NetworkX graphs from semantic models
   - LLM-powered value normalization to reduce duplicates
   - Interactive pyvis visualization with physics simulation

### Output Structure
- `assets/pdf/`: Source PDFs
- `assets/markdown/`: Extracted and chunked markdown
- `assets/models/`: RODEOS semantic models (JSON)
- `assets/kg/`: Knowledge graph visualizations and data
- `src/contextualEnrichment/prompts/`: LLM interaction logs

## Environment Variables

Required in `.env`:
```bash
# For Mistral PDF extraction
MISTRAL_API_KEY=your_key

# For OpenRouter remote models
OPENROUTER_API_KEY=your_key
```

## Model Configuration

- **Remote Models**: Any OpenRouter-compatible model (e.g., `openai/gpt-4o-mini`, `anthropic/claude-3-haiku`)
- **Local Models**: Any Ollama model (e.g., `qwen2.5:3b`, `deepseek-r1:8b`, `llama3.2:3b`)
- **Default Remote**: `openai/gpt-4o-mini`
- **Default Local**: `qwen2.5:3b`

## Key Design Patterns

1. **Modular Pipeline**: Each stage is independent and can use different LLM providers
2. **Prompt Transparency**: All LLM prompts saved for audit and reproducibility
3. **Thinking Tag Filtering**: Automatically removes `<think>` blocks from responses
4. **Retry Logic**: JSON parsing includes validation and automatic retry
5. **Batch Processing**: All scripts support both single-file and batch modes

## RODEOS Semantic Model

The pipeline generates JSON following the RODEOS structure extending W3C DCAT-3:
- **Dataset**: Raw sensor data, logs, traces
- **Model**: Kinematic models, CAD files, meshes
- **Service**: Motion skills, perception pipelines, safety checks

Each model includes DCAT metadata, RODEOS-specific properties, and relevant AAS submodels.