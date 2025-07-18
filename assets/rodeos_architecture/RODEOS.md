# Semantic Interoperability Metadata Model

This document describes the structure and semantics of the metadata model used in the Semantic Interoperability Service (SIS). The model is centered around the `dcat:Resource` concept and provides structured support for three types of digital assets: **Datasets**, **Models**, and **Services**.

## Top-Level: `dcat:Resource`

All asset types inherit from `dcat:Resource`, which provides general metadata fields for identification, provenance, and discovery.

### Core Properties

- `dcterms:title`: Title of the resource
- `dcterms:type`: Type of the resource
- `dcterms:publisher`: Publisher of the resource
- `dcterms:license`: License applied
- `dcterms:identifier`: Unique identifier
- `dcterms:description`: Description of the resource
- `dcat:version`: Version of the resource
- `dcat:keyword`: List of keywords/tags
- `dcat:contactPoint`: Contact information

## Asset Types

### `rodeos:Dataset`

A `Dataset` represents a structured or unstructured data asset that can be used in AI pipelines or analytical workflows.

#### Dataset-Specific Properties

- `dprod:informationSensitivityClassification`: Classification according to sensitivity
- `dprod:type`: Type of data (e.g., tabular, computerVision, nlp, timeseries, audio, graph)
- `rodeos:dataFormat`: Format of the dataset (e.g., csv, json, parquet)
- `rodeos:isDataProduct`: Boolean indicating whether it's a data product
- `rodeos:dataTypeSize`: Size of the datatype
- `rodeos:dataTypeSchema`: XML schema type (e.g., xsd:string, xsd:dateTime)
- `dcat:checksum`: Checksum for data integrity
- `dcat:endpointDescription`: Description of the access endpoint
- `dcat:endpointURL`: URL to access the dataset
- `dcat:protocol`: Access protocol (e.g., HTTP, FTP)
- `dprod:dataProductOwner`: Owner of the data product

---

### `rodeos:Model`

A `Model` describes an AI model, including metadata about its structure, data types, and execution framework.

#### Model-Specific Properties

- `rodeos:modelType`: Specifies the model's domain or functionality

  **Possible Values:**
  - Image Generation
  - Video Generation
  - Text Generation
  - Language Translation
  - Speech Synthesis
  - 3D Modeling
  - Object Detection
  - Text Analysis
  - Image Editing
  - Code Generation
  - Question Answering
  - Data Visualization
  - Voice Cloning
  - Background Removal
  - Image Upscaling
  - OCR
  - Document Analysis
  - Visual QA
  - Image Captioning
  - Chatbots
  - Sentiment Analysis
  - Text Summarization
  - Music Generation
  - Medical Imaging
  - Financial Analysis
  - Game AI
  - Model Benchmarking
  - Fine Tuning Tools
  - Dataset Creation
  - Pose Estimation
  - Face Recognition
  - Anomaly Detection
  - Recommendation Systems
  - Character Animation
  - Style Transfer
  - Image Classification
  - Instance Segmentation
  - Keypoint Detection
  - Semantic Segmentation
  - Multimodal

- `rodeos:inputShape`: Input shape of data
- `rodeos:outputShape`: Output shape of data
- `rodeos:inputDataType`: Type of input data
- `rodeos:outputDataType`: Type of output data
- `rodeos:modelParameters`: Model-specific parameters
- `rodeos:framework`: The ML framework used (e.g., PyTorch, TensorFlow)

---

### `rodeos:Service`

A `Service` is an operational interface that exposes AI capabilities over a network or system boundary.

#### Service-Specific Properties

- `rodeos:usedModels`: Reference to used models
- `rodeos:serviceTypeMain`: Main category of the service
- `rodeos:serviceType`: Subcategory or fine-grained type of the service

  **Possible Categories:**

  **Generative AI Services**
  - Content Generation
  - Multimodal Generation
  - Style Transfer & Enhancement

  **Conversational & Interaction Services**
  - Conversational AI & Chatbots
  - Virtual Assistants & Agent Orchestration
  - Voice Interaction & Speech Synthesis
  - Visual Question Answering

  **Language & Knowledge Services**
  - Language Translation & Localization
  - Text Summarization & Paraphrasing
  - Sentiment & Intent Analysis
  - Knowledge Extraction & Information Retrieval
  - Document Understanding & Analysis

  **Vision & Perception Services**
  - Image & Video Analysis
  - Object & Face Recognition
  - Pose & Gesture Estimation
  - Medical Imaging Analysis
  - OCR & Document Scanning

  **Data & Analytics Services**
  - Data Annotation & Labeling
  - Data Quality & Benchmarking
  - Recommendation & Personalization
  - Anomaly & Fraud Detection
  - Predictive Analytics & Forecasting

  **Automation & Orchestration Services**
  - Workflow Automation
  - AI Agent Services
  - AI Model Orchestration & Composition
  - Model-as-a-Service (MaaS)
  - API Gateway Services

  **Creative & Design Services**
  - 3D Modeling & Simulation
  - Image/Video Editing & Enhancement
  - Music & Audio Generation
  - Character Animation

  **Domain-Specific AI Services**
  - Financial Analysis & Forecasting
  - Medical Diagnostic & Healthcare AI
  - Game Intelligence & NPC Services
  - Legal & Compliance AI
  - Industrial & IoT AI

  **Infrastructure & Enablement Services**
  - AI Model Deployment & Hosting
  - Fine-Tuning & Customization
  - Dataset Management & Creation
  - Security & Privacy AI

- `dcat:endpointURL`: Service endpoint URL
- `rodeos:inputShape`: Shape of service input
- `rodeos:inputDataType`: Input data type
- `rodeos:outputDataType`: Output data type
- `dcat:endpointDescription`: Endpoint metadata
- `dcat:landingPage`: Human-readable service documentation

---

## Extensibility

The `submodels` array allows hierarchical modeling of composed resources, such as pipelines or compound services.

---

## Summary

This model aims to enable interoperable, discoverable, and semantically enriched metadata for assets relevant to modern AI-driven ecosystems.