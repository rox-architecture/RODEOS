# RODEOS Semantic Model UI

## Overview
A dynamic Streamlit interface for generating RODEOS semantic model instances based on the semantic model structure defined in `assets/semantic_model.json`.

## Features
- **Dynamic Form Generation**: Automatically generates forms based on the semantic model structure
- **Type-Aware Input Fields**:
  - Dropdowns for enum values
  - Text inputs with validation for URIs, integers, decimals, hex values
  - Checkboxes for boolean values
  - Comma-separated inputs for lists
- **Hierarchical Navigation**: Guides users through nested model structures
- **Validation**: Regular expression-based validation for different data types
- **JSON Export**: Download the generated semantic model as JSON

## Usage

### Starting the UI
```bash
# Run with uv (recommended)
uv run streamlit run semantic_model_ui.py

# Or with standard Python
streamlit run semantic_model_ui.py
```

The UI will open at http://localhost:8501

### Workflow

1. **Basic Resource Information**
   - Fill in mandatory DCAT resource fields
   - Select the core type (Dataset, Component, or Service)

2. **Type-Specific Configuration**
   - Based on your core type selection:
     - **Dataset**: Configure data format, sensitivity, product info
     - **Component**: Choose hardware/software, then specific sub-types
     - **Service**: Define service type and endpoints

3. **Hierarchical Selection**
   - For Components, navigate through the hierarchy:
     - Hardware → Robot/Tooling/Controller/Sensor → Specific types
     - Software → Operation/Motion/Vision/AI software types

4. **Optional Fields**
   - Expand optional field sections to add additional metadata

5. **Export**
   - Review the generated JSON in the preview
   - Click "Download Semantic Model (JSON)" to save

## Examples

### Creating a Mobile Robot (AGV)
1. Fill basic resource info
2. Select `rodeos:coreType` = "Component"
3. Choose `rodeos:componentType` = "hardwareComponent"
4. Select "rodeos:roboter"
5. Choose "rodeos:mobileRobot"
6. Select "rodeos:agv"
7. Fill AGV-specific fields (guidance system, load capacity)

### Creating a Dataset
1. Fill basic resource info
2. Select `rodeos:coreType` = "Dataset"
3. Configure data format, size, sensitivity classification
4. Add optional endpoint information if applicable

### Creating a Service
1. Fill basic resource info
2. Select `rodeos:coreType` = "Service"
3. Define service type and endpoints
4. Link to models used by the service

## Data Types and Validation

| Type | Input Widget | Validation |
|------|-------------|------------|
| `xsd:text` | Text input | None |
| `xsd:integer` | Text input | Digits only |
| `xsd:decimal` | Text input | Decimal numbers |
| `xsd:boolean` | Checkbox | True/False |
| `xsd:anyUri` | Text input | Valid URI format |
| `xsd:hexBinary` | Text input | Hex characters only |
| `enum[...]` | Dropdown | Predefined values |
| `List[...]` | Text area | Comma-separated values |

## Extending the Model

The UI dynamically reads `assets/semantic_model.json`, so you can:
1. Edit the semantic model JSON to add new fields or types
2. The UI will automatically adapt to the changes
3. No code changes required in the UI

## Reset

Click the "Reset Form" button to clear all inputs and start over.