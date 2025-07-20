# RODEOS Document Processing Pipeline
# Simple pipeline with local/remote processing options

# Configuration
REMOTE_MODEL ?= openai/gpt-4o-mini
LOCAL_MODEL ?= qwen2.5:3b
PDF_DIR = assets/pdf
MARKDOWN_DIR = assets/markdown

# Default target
.PHONY: help
help:
	@echo "RODEOS Document Processing Pipeline"
	@echo ""
	@echo "Usage:"
	@echo "  make process FILE=document.pdf          # Process single PDF (remote)"
	@echo "  make process-local FILE=document.pdf    # Process single PDF (local)"
	@echo "  make process-batch                      # Process all PDFs (remote)"
	@echo "  make process-batch-local                # Process all PDFs (local)"
	@echo ""
	@echo "Model Configuration:"
	@echo "  REMOTE_MODEL: $(REMOTE_MODEL) (default for remote processing)"
	@echo "  LOCAL_MODEL: $(LOCAL_MODEL) (default for local processing)"
	@echo ""
	@echo "Examples:"
	@echo "  make process FILE=doc.pdf REMOTE_MODEL=anthropic/claude-3-haiku"
	@echo "  make process-local FILE=doc.pdf LOCAL_MODEL=llama3.2:3b"
	@echo ""
	@echo "Pipeline Steps:"
	@echo "  1. PDF → Markdown (Mistral API)"
	@echo "  2. Markdown → Chunked (Context analysis)"
	@echo "  3. Chunked → Semantic Model (RODEOS extraction)"

# Process single PDF file (remote)
.PHONY: process
process:
	@if [ -z "$(FILE)" ]; then \
		echo "Error: FILE parameter required. Usage: make process FILE=document.pdf"; \
		exit 1; \
	fi
	@echo "🚀 Starting remote pipeline for $(FILE)"
	@basename_file=$$(basename "$(FILE)" .pdf); \
	echo "📄 Step 1/3: PDF Extraction"; \
	uv run src/informationExtraction/mistralApiExtraction.py "$(PDF_DIR)/$(FILE)"; \
	echo "💭 Step 2/3: Contextualization (remote: $(REMOTE_MODEL))"; \
	uv run src/contextualEnrichment/context.py "$(MARKDOWN_DIR)/$${basename_file}_MISTRAL.md" --model $(REMOTE_MODEL); \
	echo "🎯 Step 3/3: Semantic Model Extraction (remote: $(REMOTE_MODEL))"; \
	uv run src/extractInformation/extraction.py "$(MARKDOWN_DIR)/$${basename_file}_MISTRAL_CHUNKED.md" --model $(REMOTE_MODEL)
	@echo "✅ Remote pipeline completed for $(FILE)"

# Process single PDF file (local)
.PHONY: process-local
process-local:
	@if [ -z "$(FILE)" ]; then \
		echo "Error: FILE parameter required. Usage: make process-local FILE=document.pdf"; \
		exit 1; \
	fi
	@echo "🚀 Starting local pipeline for $(FILE)"
	@basename_file=$$(basename "$(FILE)" .pdf); \
	echo "📄 Step 1/3: PDF Extraction"; \
	uv run src/informationExtraction/localDoclingExtraction.py "$(PDF_DIR)/$(FILE)" --enhanced; \
	echo "💭 Step 2/3: Contextualization (local: $(LOCAL_MODEL))"; \
	uv run src/contextualEnrichment/context.py "$(MARKDOWN_DIR)/$${basename_file}_DOCLING_enhanced.md" --local --model $(LOCAL_MODEL); \
	echo "🎯 Step 3/3: Semantic Model Extraction (local: $(LOCAL_MODEL))"; \
	uv run src/extractInformation/extraction.py "$(MARKDOWN_DIR)/$${basename_file}_DOCLING_enhanced_CHUNKED.md" --local --model $(LOCAL_MODEL)
	@echo "✅ Local pipeline completed for $(FILE)"

# Process all PDF files (remote)
.PHONY: process-batch
process-batch:
	@echo "🚀 Starting remote batch pipeline"
	@if [ ! -d "$(PDF_DIR)" ]; then \
		echo "Error: PDF directory $(PDF_DIR) not found"; \
		exit 1; \
	fi
	@pdf_count=$$(ls -1 $(PDF_DIR)/*.pdf 2>/dev/null | wc -l); \
	if [ $$pdf_count -eq 0 ]; then \
		echo "Error: No PDF files found in $(PDF_DIR)"; \
		exit 1; \
	fi; \
	echo "📄 Found $$pdf_count PDF files to process"
	@echo "📄 Step 1/3: PDF Extraction"
	@for pdf in $(PDF_DIR)/*.pdf; do \
		echo "Processing $$pdf with Mistral API..."; \
		uv run src/informationExtraction/mistralApiExtraction.py "$$pdf" || echo "Failed: $$pdf"; \
	done
	@echo "💭 Step 2/3: Contextualization (remote: $(REMOTE_MODEL))"
	@uv run src/contextualEnrichment/context.py --batch --model $(REMOTE_MODEL)
	@echo "🎯 Step 3/3: Semantic Model Extraction (remote: $(REMOTE_MODEL))"
	@uv run src/extractInformation/extraction.py --batch --model $(REMOTE_MODEL)
	@echo "✅ Remote batch pipeline completed"

# Process all PDF files (local)
.PHONY: process-batch-local
process-batch-local:
	@echo "🚀 Starting local batch pipeline"
	@if [ ! -d "$(PDF_DIR)" ]; then \
		echo "Error: PDF directory $(PDF_DIR) not found"; \
		exit 1; \
	fi
	@pdf_count=$$(ls -1 $(PDF_DIR)/*.pdf 2>/dev/null | wc -l); \
	if [ $$pdf_count -eq 0 ]; then \
		echo "Error: No PDF files found in $(PDF_DIR)"; \
		exit 1; \
	fi; \
	echo "📄 Found $$pdf_count PDF files to process"
	@echo "📄 Step 1/3: PDF Extraction"
	@for pdf in $(PDF_DIR)/*.pdf; do \
		echo "Processing $$pdf with local extraction..."; \
		uv run src/informationExtraction/localDoclingExtraction.py "$$pdf" --enhanced || echo "Failed: $$pdf"; \
	done
	@echo "💭 Step 2/3: Contextualization (local: $(LOCAL_MODEL))"
	@uv run src/contextualEnrichment/context.py --batch --local --model $(LOCAL_MODEL)
	@echo "🎯 Step 3/3: Semantic Model Extraction (local: $(LOCAL_MODEL))"
	@uv run src/extractInformation/extraction.py --batch --local --model $(LOCAL_MODEL)
	@echo "✅ Local batch pipeline completed"

# Clean generated files
.PHONY: clean
clean:
	@echo "🧹 Cleaning generated files..."
	@rm -rf assets/markdown/*_MISTRAL.md
	@rm -rf assets/markdown/*_DOCLING_*.md
	@rm -rf assets/markdown/*_CHUNKED.md
	@rm -rf assets/models/*.json
	@rm -rf src/contextualEnrichment/prompts/*.md
	@echo "✅ Cleanup completed"

# Show pipeline status
.PHONY: status
status:
	@echo "📊 Pipeline Status:"
	@echo "PDF files: $$(ls -1 $(PDF_DIR)/*.pdf 2>/dev/null | wc -l)"
	@echo "Extracted markdowns: $$(ls -1 $(MARKDOWN_DIR)/*_MISTRAL.md $(MARKDOWN_DIR)/*_DOCLING_*.md 2>/dev/null | wc -l)"
	@echo "Chunked markdowns: $$(ls -1 $(MARKDOWN_DIR)/*_CHUNKED.md 2>/dev/null | wc -l)"
	@echo "Semantic models: $$(ls -1 assets/models/*.json 2>/dev/null | wc -l)" 