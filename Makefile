# ==============================================================================
# StackCalc Master Reference Manuals & Documentation Pipeline (Dependency-Driven)
# ==============================================================================
# Automatically rebuilds the full SC-32 Scientific and SC-6 Elementary books
# whenever any dependent file changes:
#   1. OpenSCAD (.scad) -> STL (.stl) -> Orthographic Block Diagrams & blocks_registry.json
#   2. Swift Layout & SwiftUI Tests (.swift) -> layout_data*.json, sequences_registry.json, & Screenshots
#   3. Manuscript Chapters (.md) + Registries + book_engine.py -> Validated Guides & RPNCore Unit Tests
#   4. Validated Guides + Assets + generate_manual_pdfs.py -> Publication PDFs
#   5. Publication PDFs + mkdocs.yml + Chapters -> Strict MkDocs Site (site/index.html)
# ==============================================================================

SHELL := /bin/bash
.DEFAULT_GOAL := book
.DELETE_ON_ERROR:

PYTHON ?= $(if $(wildcard .venv/bin/python3),.venv/bin/python3,python3)
MKDOCS ?= $(if $(wildcard .venv/bin/mkdocs),.venv/bin/mkdocs,mkdocs)
BLENDER ?= $(if $(wildcard /Applications/Blender.app/Contents/MacOS/Blender),/Applications/Blender.app/Contents/MacOS/Blender,blender)
SIMULATOR_NAME ?= iPhone 17 Pro

WATCH_REPO := ../watch-calc-32
EDUCATION_DIR := $(WATCH_REPO)/Education

# 1. Upstream CAD / STL / Manipulative Diagram Dependencies
SCAD_SOURCES := $(wildcard $(EDUCATION_DIR)/scad/*.scad $(EDUCATION_DIR)/scad/lib/*.scad $(WATCH_REPO)/Hardware/designs/*.scad)
STL_FILES := $(wildcard $(WATCH_REPO)/scratch/stl/*.stl $(WATCH_REPO)/scratch/stl/education/*.stl $(EDUCATION_DIR)/build/stl/components/*.stl)
DIAGRAM_SCRIPT := $(EDUCATION_DIR)/tools/generate_book_diagrams.py
BLOCKS_REGISTRY := docs/assets/manuals/blocks_registry.json
BLOCK_PNGS := $(addprefix docs/assets/manuals/, \
	ten_frame_bridging_ten.png \
	counting_tiles_box_3x1x13u.png \
	counting_tiles_array_3x8.png \
	counting_tiles_distributive_4color.png \
	counting_tiles_fraction_datum_84mm.png \
	fraction_studio_twin_comparator.png \
	prime_studio_comparator_stage.png \
	prime_studio_commutativity.png \
	prime_lcm_gcd_venn.png \
	planetary_geared_clock_330.png \
	dice_spinner_probability.png \
	place_value_regrouping.png \
	number_rack_subitizing.png \
	math_dominoes_pairing.png \
	algebra_factoring_area.png)

# 2. Upstream Swift Layout, Keystroke Sequence & Screenshot Dependencies
SWIFT_LAYOUT_SOURCES := \
	$(WATCH_REPO)/RPNCore/Sources/RPNCore/CalculatorOperation+Legends.swift \
	$(WATCH_REPO)/RPNCore/Sources/RPNCore/MenuSystem.swift \
	$(WATCH_REPO)/RPNCore/Sources/RPNCore/StackCalc6/StackCalc6KeyMap.swift \
	$(WATCH_REPO)/StackCalc32ContainerTests/DecalExportTests.swift

SWIFT_SCREENSHOT_SOURCES := \
	$(SWIFT_LAYOUT_SOURCES) \
	$(WATCH_REPO)/Shared/HardwareReplicaView.swift \
	$(WATCH_REPO)/Shared/RetroNameplateView.swift \
	$(WATCH_REPO)/Shared/HardwareReplicaKeyCap.swift \
	$(WATCH_REPO)/Shared/LCDDisplayView.swift \
	$(WATCH_REPO)/Shared/FaceplateTheme.swift \
	$(WATCH_REPO)/StackCalc32ContainerTests/SwiftUIVisualFuzzTests.swift

LAYOUT_SC32_JSON := docs/assets/manuals/layout_data.json
LAYOUT_SC6_JSON := docs/assets/manuals/layout_data_sc6.json
SEQUENCES_REGISTRY := docs/assets/manuals/sequences_registry.json
SCREENSHOT_PNGS := $(wildcard docs/assets/manuals/screenshots/*.png)

# 3. Manuscript & Macro Engine Dependencies
SC32_CHAPTERS := $(wildcard docs/manuals/sc32/*.md)
SC6_CHAPTERS := $(wildcard docs/manuals/sc6/*.md)
BOOK_ENGINE_TOOLS := Tools/book_engine.py Tools/transform_and_validate_manuals.py
RPN_TESTS := \
	$(WATCH_REPO)/RPNCore/Tests/RPNCoreTests/TextbookVerificationTests_SC32.swift \
	$(WATCH_REPO)/RPNCore/Tests/RPNCoreTests/StackCalc6/TextbookVerificationTests_SC6.swift

USER_GUIDES := docs/manuals/sc32-user-guide.md docs/manuals/sc6-user-guide.md
PDF_MANUALS := docs/downloads/manuals/sc32-scientific-manual.pdf docs/downloads/manuals/sc6-elementary-manual.pdf
SITE_INDEX := site/index.html

.PHONY: help all book manuals blocks screenshots layouts verify pdfs site clean

help:
	@echo "StackCalc Reference Manuals & Documentation Build System"
	@echo "--------------------------------------------------------"
	@echo "  make book        - Incrementally update blocks, layouts, screenshots, macros, tests, PDFs, & MkDocs site"
	@echo "  make blocks      - Rebuild STL-backed OpenSCAD orthographic diagrams & blocks_registry.json if SCAD/STLs changed"
	@echo "  make layouts     - Export layout_data.json and layout_data_sc6.json if Swift keymaps changed"
	@echo "  make screenshots - Run SwiftUI Paper-theme test suite to update screenshots & sequences_registry.json"
	@echo "  make verify      - Validate all book macros (keys, sequences, screenshots, blocks) and run 81 RPNCore unit tests"
	@echo "  make pdfs        - Compile publication-grade SC-32 and SC-6 PDF manuals if chapters or assets changed"
	@echo "  make site        - Build MkDocs documentation site with --strict validation"

all: book
manuals: book
book: $(PDF_MANUALS) $(SITE_INDEX)

# ------------------------------------------------------------------------------
# Stage 1: OpenSCAD / STL -> Orthographic Block Diagrams & blocks_registry.json
# ------------------------------------------------------------------------------
blocks: $(BLOCKS_REGISTRY)

$(BLOCKS_REGISTRY) $(BLOCK_PNGS): $(SCAD_SOURCES) $(STL_FILES) $(DIAGRAM_SCRIPT)
	@echo "==> [1/5] Updating STL-backed manipulative diagrams & blocks_registry.json..."
	$(MAKE) -C $(EDUCATION_DIR) ../../stackcalc/docs/assets/manuals/blocks_registry.json

# ------------------------------------------------------------------------------
# Stage 2: Swift Key Layouts & SwiftUI Test Suite -> JSON Registries & Screenshots
# ------------------------------------------------------------------------------
layouts: $(LAYOUT_SC32_JSON) $(LAYOUT_SC6_JSON)

$(LAYOUT_SC32_JSON) $(LAYOUT_SC6_JSON): $(SWIFT_LAYOUT_SOURCES)
	@echo "==> Exporting SC-32 and SC-6 key layouts from DecalExportTests..."
	cd $(WATCH_REPO) && xcodebuild test \
		-project StackCalc32.xcodeproj \
		-scheme StackCalc32Container \
		-destination "platform=iOS Simulator,name=$(SIMULATOR_NAME)" \
		-only-testing:StackCalc32ContainerTests/DecalExportTests/testExportDecal
	@cp -f $(WATCH_REPO)/scratch/decals/layout_data.json $(LAYOUT_SC32_JSON) 2>/dev/null || true
	@cp -f $(WATCH_REPO)/scratch/decals/layout_data_sc6.json $(LAYOUT_SC6_JSON) 2>/dev/null || true
	@touch $(LAYOUT_SC32_JSON) $(LAYOUT_SC6_JSON)

screenshots: $(SEQUENCES_REGISTRY)

$(SEQUENCES_REGISTRY): $(SWIFT_SCREENSHOT_SOURCES)
	@echo "==> [2/5] Running SwiftUI Paper-theme visual test suite to export screenshots & sequences_registry.json..."
	cd $(WATCH_REPO) && xcodebuild test \
		-project StackCalc32.xcodeproj \
		-scheme StackCalc32Container \
		-destination "platform=iOS Simulator,name=$(SIMULATOR_NAME)" \
		-only-testing:StackCalc32ContainerTests/SwiftUIVisualFuzzTests/testExportTextbookScreenshotsAndSequences
	@touch $(SEQUENCES_REGISTRY) $(LAYOUT_SC32_JSON) $(LAYOUT_SC6_JSON)

# ------------------------------------------------------------------------------
# Stage 3: Macro Validation, Auto-Numbering, Guide Sync & RPNCore Unit Tests
# ------------------------------------------------------------------------------
verify: $(USER_GUIDES)
	@echo "==> Running RPNCore TextbookVerificationTests (SC-32 & SC-6)..."
	cd $(WATCH_REPO)/RPNCore && swift test --filter TextbookVerificationTests

$(USER_GUIDES): $(SC32_CHAPTERS) $(SC6_CHAPTERS) $(BOOK_ENGINE_TOOLS) $(LAYOUT_SC32_JSON) $(LAYOUT_SC6_JSON) $(SEQUENCES_REGISTRY) $(BLOCKS_REGISTRY) $(RPN_TESTS)
	@echo "==> [3/5] Validating macros, auto-numbering sections, syncing guides, & running RPNCore tests..."
	$(PYTHON) Tools/transform_and_validate_manuals.py
	cd $(WATCH_REPO)/RPNCore && swift test --filter TextbookVerificationTests
	@touch $(USER_GUIDES)

# ------------------------------------------------------------------------------
# Stage 4: Publication PDF Manuals (ReportLab)
# ------------------------------------------------------------------------------
pdfs: $(PDF_MANUALS)

$(PDF_MANUALS): $(USER_GUIDES) Tools/generate_manual_pdfs.py $(BLOCK_PNGS) $(SCREENSHOT_PNGS)
	@echo "==> [4/5] Compiling SC-32 and SC-6 publication PDFs..."
	$(PYTHON) Tools/generate_manual_pdfs.py
	@touch $(PDF_MANUALS)

# ------------------------------------------------------------------------------
# Stage 5: MkDocs Strict Documentation Build
# ------------------------------------------------------------------------------
site: $(SITE_INDEX)

$(SITE_INDEX): $(PDF_MANUALS) mkdocs.yml $(SC32_CHAPTERS) $(SC6_CHAPTERS)
	@echo "==> [5/5] Building MkDocs site (--strict)..."
	$(MKDOCS) build --strict
	@touch $(SITE_INDEX)
