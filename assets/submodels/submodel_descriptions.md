# Submodel Descriptions

This document provides a concise, generic description of each submodel contained in the provided files. Each section outlines the submodel's intended purpose, main components, and typical use cases. These descriptions are intended to support decision-making when selecting submodels for specific assets or AI components.

---

## Submodel: AI Dataset (`AIDataset`)

**Description**:  
Captures metadata and structural information for datasets used in AI development or evaluation. It supports both classification and regression datasets and includes fields for versioning, storage location, labeling structure, and optional file-based annotations.

**Key Components**:
- Dataset version and URI
- Contact reference
- Storage path
- Classification and regression label details
- Label balancing, number of labels, label names
- File-based annotations and sample details

**Typical Use Cases**:
- Describing datasets used for training AI models
- Documenting data provenance and structure
- Annotating and indexing labeled datasets for reuse

---

## Submodel: AI Deployment (`AIDeployment`)

**Description**:  
Describes how an AI model is deployed, including technical and environmental details. It covers versioning, deployment inputs/outputs, runtime constraints, performance metrics, and references to the original model.

**Key Components**:
- Product URI and deployment version
- Contact information
- References to model metadata
- Storage (e.g. Docker, ONNX)
- Input/output schemas
- Software and hardware requirements
- Performance and inference time
- Live monitoring (e.g. confidence values)

**Typical Use Cases**:
- Documenting how an AI model is deployed into a runtime system
- Defining required resources and configurations
- Capturing performance metrics or deployment audit trails

---

## Submodel: Generic Technical Data (`TechnicalData`)

**Description**:  
Represents general technical and classification information for an asset. It includes manufacturer details, product identifiers, product images, and classification according to industrial taxonomies like ECLASS or UNSPSC.

**Key Components**:
- Manufacturer name, logo, article number
- Product designation and order code
- Product images with captions
- Product classifications (system, version, ID, coded name)

**Typical Use Cases**:
- Providing a digital nameplate for technical components
- Supporting part identification, catalog integration, and procurement
- Linking to product master data in engineering or manufacturing systems

---# Submodel Descriptions

Available submodels for RODEOS semantic model enhancement:

- **aas_ai_dataset**: Asset Administration Shell submodel for AI datasets, containing categories and information about data assets used in AI/ML workflows including dataset metadata, classification, and properties.

- **aas_ai_deployment**: Asset Administration Shell submodel for AI deployment scenarios, containing information about model deployment configurations, runtime environments, and operational parameters for AI services.

- **aas_generic_frame_technical_data**: Asset Administration Shell submodel for technical data and product classifications, containing comprehensive technical specifications, dimensions, performance parameters, and standardized product classification information for industrial assets. 