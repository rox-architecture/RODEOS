#!/usr/bin/env python3
"""
RODEOS Semantic Model Instance Generator
Dynamic Streamlit UI for creating semantic model instances
"""

import streamlit as st
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

# Page configuration
st.set_page_config(
    page_title="RODEOS Semantic Model Generator",
    page_icon="🤖",
    layout="wide"
)

def load_semantic_model() -> Dict[str, Any]:
    """Load the semantic model from the assets folder."""
    model_path = Path("assets/semantic_model.json")
    if not model_path.exists():
        st.error(f"Semantic model not found at {model_path}")
        return {}

    with open(model_path, 'r') as f:
        return json.load(f)

def parse_field_type(field_type: str) -> Dict[str, Any]:
    """Parse field type string to determine input widget type and validation."""
    result = {
        'type': 'text',
        'is_list': False,
        'is_enum': False,
        'enum_values': [],
        'validation': None
    }

    # Check for List type
    if field_type.startswith('List['):
        result['is_list'] = True
        field_type = field_type[5:-1]  # Extract inner type

    # Check for enum
    if field_type.startswith('enum['):
        result['is_enum'] = True
        result['type'] = 'enum'
        # Extract enum values
        enum_str = field_type[5:-1]
        result['enum_values'] = [v.strip() for v in enum_str.split(',')]
    elif field_type == 'xsd:integer':
        result['type'] = 'integer'
        result['validation'] = r'^\d+$'
    elif field_type == 'xsd:decimal':
        result['type'] = 'decimal'
        result['validation'] = r'^\d+\.?\d*$'
    elif field_type == 'xsd:boolean':
        result['type'] = 'boolean'
    elif field_type == 'xsd:anyUri':
        result['type'] = 'uri'
        result['validation'] = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'
    elif field_type == 'xsd:hexBinary':
        result['type'] = 'hex'
        result['validation'] = r'^[0-9A-Fa-f]+$'
    elif field_type in ['xsd:text', 'skos:concept', 'schema:quantitativeValue']:
        result['type'] = 'text'

    return result

def create_input_widget(field_name: str, field_type: str, key_prefix: str,
                        required: bool = True, default_value: Any = None) -> Any:
    """Create appropriate input widget based on field type."""
    parsed = parse_field_type(field_type)
    key = f"{key_prefix}_{field_name}"
    label = f"{field_name} ({field_type})" + (" *" if required else "")

    if parsed['is_list']:
        # Handle list inputs
        st.write(f"**{label}** (comma-separated)")
        if parsed['type'] == 'text':
            value = st.text_area(
                "Enter values separated by commas",
                key=key,
                value=default_value if default_value else "",
                height=100
            )
            if value:
                return [v.strip() for v in value.split(',') if v.strip()]
            return []
        else:
            # For other list types, use text input with validation
            value = st.text_input(
                "Enter values separated by commas",
                key=key,
                value=default_value if default_value else ""
            )
            if value:
                items = [v.strip() for v in value.split(',') if v.strip()]
                # Validate each item if needed
                if parsed['validation']:
                    valid_items = []
                    for item in items:
                        if re.match(parsed['validation'], item):
                            valid_items.append(item)
                        else:
                            st.warning(f"Invalid value: {item}")
                    return valid_items
                return items
            return []

    elif parsed['is_enum']:
        # Dropdown for enum
        return st.selectbox(
            label,
            options=parsed['enum_values'],
            key=key,
            index=0 if default_value is None else
                  parsed['enum_values'].index(default_value) if default_value in parsed['enum_values'] else 0
        )

    elif parsed['type'] == 'boolean':
        return st.checkbox(label, key=key, value=default_value if default_value else False)

    elif parsed['type'] == 'integer':
        value = st.text_input(
            label,
            key=key,
            value=str(default_value) if default_value else "",
            placeholder="Enter integer value"
        )
        if value and re.match(parsed['validation'], value):
            return int(value)
        elif value:
            st.error(f"Invalid integer: {value}")
        return None

    elif parsed['type'] == 'decimal':
        value = st.text_input(
            label,
            key=key,
            value=str(default_value) if default_value else "",
            placeholder="Enter decimal value"
        )
        if value and re.match(parsed['validation'], value):
            return float(value)
        elif value:
            st.error(f"Invalid decimal: {value}")
        return None

    elif parsed['type'] == 'uri':
        value = st.text_input(
            label,
            key=key,
            value=default_value if default_value else "",
            placeholder="https://example.com"
        )
        if value and parsed['validation']:
            if re.match(parsed['validation'], value):
                return value
            else:
                st.error("Invalid URI format. Must start with http://, https://, or ftp://")
                return None
        return value if value else None

    elif parsed['type'] == 'hex':
        value = st.text_input(
            label,
            key=key,
            value=default_value if default_value else "",
            placeholder="Enter hexadecimal value"
        )
        if value and parsed['validation']:
            if re.match(parsed['validation'], value):
                return value
            else:
                st.error("Invalid hex format. Use only 0-9 and A-F characters")
                return None
        return value if value else None

    else:  # Default text input
        return st.text_input(
            label,
            key=key,
            value=default_value if default_value else "",
            placeholder=f"Enter {field_name}"
        )

def render_fields(fields: Dict[str, str], key_prefix: str,
                 required: bool = True, defaults: Dict[str, Any] = None) -> Dict[str, Any]:
    """Render form fields and collect values."""
    values = {}
    defaults = defaults or {}

    for field_name, field_type in fields.items():
        default_val = defaults.get(field_name)
        value = create_input_widget(field_name, field_type, key_prefix, required, default_val)
        if value is not None and value != "" and value != []:
            values[field_name] = value

    return values

def get_hierarchy_depth(model: Dict[str, Any], path: List[str]) -> Dict[str, Any]:
    """Navigate to the current level in the model hierarchy."""
    current = model
    for step in path:
        if 'instances' in current and step in current['instances']:
            current = current['instances'][step]
        elif step == 'dcat:Resource':
            current = model.get('dcat:Resource', {})
    return current

def render_hierarchy_level(model: Dict[str, Any], path: List[str], depth: int = 0) -> Dict[str, Any]:
    """Render a single level of the hierarchy with proper indentation and context."""
    result = {}
    current_level = get_hierarchy_depth(model, path)

    # Display current path for context
    if path:
        display_path = " → ".join([p.replace('rodeos:', '') for p in path[1:]])  # Skip dcat:Resource
        if display_path:
            st.caption(f"📍 Current selection path: {display_path}")

    # Render mandatory fields
    if 'mandatory' in current_level and current_level['mandatory']:
        if current_level['mandatory']:  # Only show if not empty
            st.markdown(f"{'  ' * depth}#### Mandatory Fields")
            mandatory_values = render_fields(
                current_level['mandatory'],
                "_".join(path + ['mandatory']),
                required=True,
                defaults=current_level.get('defaultValues', {})
            )
            result.update(mandatory_values)

    # Render optional fields
    if 'optional' in current_level and current_level['optional']:
        if current_level['optional']:  # Only show if not empty
            with st.expander(f"{'  ' * depth}Optional Fields", expanded=False):
                optional_values = render_fields(
                    current_level['optional'],
                    "_".join(path + ['optional']),
                    required=False
                )
                result.update(optional_values)

    # Handle instances (sub-types)
    if 'instances' in current_level and current_level['instances']:
        instance_options = list(current_level['instances'].keys())

        # Determine selection key based on component type or other special fields
        selection_key = None

        # Special handling for component type
        if 'rodeos:componentType' in result:
            component_type = result['rodeos:componentType']
            selection_key = f"rodeos:{component_type}"
        elif 'rodeos:robotOperationSystemType' in result:
            # For software components, use the specific type
            selection_key = 'rodeos:robotOperationSoftware'
        elif len(instance_options) > 0:
            # Let user choose from available instances
            st.markdown(f"{'  ' * depth}#### Select Type")

            # Create more readable labels
            readable_options = {opt: opt.replace('rodeos:', '').replace('_', ' ').title()
                              for opt in instance_options}

            selected = st.selectbox(
                "Choose sub-type:",
                options=instance_options,
                format_func=lambda x: readable_options[x],
                key="_".join(path + ['instance_selection']),
                help="Select the specific type to configure its properties"
            )
            selection_key = selected

        # Render the selected instance
        if selection_key and selection_key in current_level['instances']:
            st.markdown("---")
            st.markdown(f"### Configuring: {selection_key.replace('rodeos:', '').replace('_', ' ').title()}")

            # Recursively render the next level
            sub_result = render_hierarchy_level(
                model,
                path + [selection_key],
                depth + 1
            )
            result.update(sub_result)

    return result

def main():
    st.title("🤖 RODEOS Semantic Model Instance Generator")
    st.markdown("Generate concrete instances using the RODEOS semantic model structure")

    # Load semantic model
    model = load_semantic_model()
    if not model:
        return

    # Initialize session state
    if 'generated_model' not in st.session_state:
        st.session_state.generated_model = {}

    st.markdown("---")

    # Get the dcat:Resource structure
    if 'dcat:Resource' not in model:
        st.error("Invalid semantic model structure: missing dcat:Resource")
        return

    resource_model = model['dcat:Resource']

    # Step 1: Fill mandatory dcat:Resource fields
    st.header("Step 1: Basic Resource Information")
    st.markdown("Fill in the mandatory fields for the DCAT Resource")

    resource_data = {}

    # Render mandatory resource fields
    if 'mandatory' in resource_model:
        mandatory_values = render_fields(
            resource_model['mandatory'],
            'resource_mandatory',
            required=True
        )
        resource_data.update(mandatory_values)

    # Check if core type was selected
    if 'rodeos:coreType' in resource_data:
        core_type = resource_data['rodeos:coreType']

        st.markdown("---")
        st.header(f"Step 2: Configure {core_type}")

        # Map core type to instance key
        instance_key = f"rodeos:{core_type}"

        if instance_key in resource_model.get('instances', {}):
            # Render the specific instance type form
            instance_data = render_hierarchy_level(
                model,
                ['dcat:Resource', instance_key],
                depth=0
            )
            resource_data.update(instance_data)

    # Display the generated model
    st.markdown("---")
    st.header("Generated Semantic Model")

    if resource_data:
        # Clean up the data (remove None values)
        cleaned_data = {k: v for k, v in resource_data.items()
                       if v is not None and v != "" and v != []}

        # Store in session state
        st.session_state.generated_model = cleaned_data

        # Display as JSON
        st.json(cleaned_data)

        # Download button
        if cleaned_data:
            json_str = json.dumps(cleaned_data, indent=2)
            st.download_button(
                label="📥 Download Semantic Model (JSON)",
                data=json_str,
                file_name="rodeos_semantic_instance.json",
                mime="application/json"
            )
    else:
        st.warning("Please fill in the required fields to generate the semantic model")

    # Add a reset button
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("🔄 Reset Form"):
            st.session_state.clear()
            st.rerun()

if __name__ == "__main__":
    main()