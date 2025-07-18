# RODEOS Document Processing Pipeline
# Processes PDFs through extraction, contextualization, and semantic model creation

# Configuration
EXTRACTION_MODE ?= remote
MODEL ?= openai/gpt-4o-mini
PDF_DIR = assets/pdf
MARKDOWN_DIR = assets/markdown

# Default target
.PHONY: help
help:
	@echo "RODEOS Document Processing Pipeline"
	@echo ""
	@echo "Usage:"
	@echo "  make process FILE=document.pdf          # Process single PDF (remote extraction)"
	@echo "  make process FILE=document.pdf EXTRACTION_MODE=local  # Process with local extraction"
	@echo "  make process-batch                      # Process all PDFs (remote extraction)"
	@echo "  make process-batch EXTRACTION_MODE=local MODEL=anthropic/claude-3-haiku  # Batch with options"
	@echo ""
	@echo "Options:"
	@echo "  EXTRACTION_MODE: remote (default) or local"
	@echo "  MODEL: openai/gpt-4o-mini (default) or other OpenRouter model"
	@echo ""
	@echo "Pipeline Steps:"
	@echo "  1. PDF → Markdown (Mistral API or Docling)"
	@echo "  2. Markdown → Chunked (Context analysis)"
	@echo "  3. Chunked → Semantic Model (RODEOS extraction)"

# Process single PDF file
.PHONY: process
process:
	@if [ -z "$(FILE)" ]; then \
		echo "Error: FILE parameter required. Usage: make process FILE=document.pdf"; \
		exit 1; \
	fi
	@echo "🚀 Starting pipeline for $(FILE)"
	@echo "📄 Step 1/3: PDF Extraction ($(EXTRACTION_MODE) mode)"
	@basename_file=$$(basename "$(FILE)" .pdf); \
	if [ "$(EXTRACTION_MODE)" = "local" ]; then \
		uv run src/informationExtraction/localDoclingExtraction.py "$(PDF_DIR)/$(FILE)" --enhanced; \
		echo "💭 Step 2/3: Contextualization"; \
		uv run src/contextualEnrichment/context.py "$(MARKDOWN_DIR)/$${basename_file}_DOCLING_enhanced.md" --remote $(MODEL); \
	else \
		uv run src/informationExtraction/mistralApiExtraction.py "$(PDF_DIR)/$(FILE)"; \
		echo "💭 Step 2/3: Contextualization"; \
		uv run src/contextualEnrichment/context.py "$(MARKDOWN_DIR)/$${basename_file}_MISTRAL.md" --remote $(MODEL); \
	fi; \
	echo "🎯 Step 3/3: Semantic Model Extraction"; \
	if [ "$(EXTRACTION_MODE)" = "local" ]; then \
		uv run src/extractInformation/extraction.py "$(MARKDOWN_DIR)/$${basename_file}_DOCLING_enhanced_CHUNKED.md" --model $(MODEL); \
	else \
		uv run src/extractInformation/extraction.py "$(MARKDOWN_DIR)/$${basename_file}_MISTRAL_CHUNKED.md" --model $(MODEL); \
	fi
	@echo "✅ Pipeline completed for $(FILE)"

# Process all PDF files in batch
.PHONY: process-batch
process-batch:
	@echo "🚀 Starting batch pipeline for all PDFs"
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
	@echo "📄 Step 1/3: PDF Extraction ($(EXTRACTION_MODE) mode)"
	@if [ "$(EXTRACTION_MODE)" = "local" ]; then \
		for pdf in $(PDF_DIR)/*.pdf; do \
			echo "Processing $$pdf with local extraction..."; \
			python src/informationExtraction/localDoclingExtraction.py "$$pdf" --enhanced || echo "Failed: $$pdf"; \
		done; \
	else \
		for pdf in $(PDF_DIR)/*.pdf; do \
			echo "Processing $$pdf with Mistral API..."; \
			python src/informationExtraction/mistralApiExtraction.py "$$pdf" || echo "Failed: $$pdf"; \
		done; \
	fi
	@echo "💭 Step 2/3: Contextualization"
	@python src/contextualEnrichment/context.py --batch --remote $(MODEL)
	@echo "🎯 Step 3/3: Semantic Model Extraction"
	@python src/extractInformation/extraction.py --batch --model $(MODEL)
	@echo "✅ Batch pipeline completed"

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