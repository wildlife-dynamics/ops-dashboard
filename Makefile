.PHONY: help compile recompile run clean

WORKFLOW_ID  := ops_dashboard
WORKFLOW_DIR := ecoscope-workflows-ops-dashboard-workflow
PARAM_FILE   ?= param.yaml
OUTPUT_DIR   ?= /tmp/ops-dashboard-output

-include Makefile.local

help:
	@echo ""
	@echo "  compile    — fresh compile (installs pixi env)"
	@echo "  recompile  — recompile after spec.yaml changes"
	@echo "  run        — run the workflow with param.yaml"
	@echo "  clean      — delete output directory"
	@echo ""
	@echo "  Overrides: make run PARAM_FILE=my-params.yaml OUTPUT_DIR=/tmp/out"
	@echo ""

compile:
	pixi run compile

recompile:
	pixi run recompile

run:
	@mkdir -p $(OUTPUT_DIR)
	@echo "Running $(WORKFLOW_ID) → $(OUTPUT_DIR)"
	cd $(WORKFLOW_DIR) && \
	ECOSCOPE_WORKFLOWS_RESULTS="file://$(OUTPUT_DIR)" \
	pixi run $(WORKFLOW_DIR) run \
		--config-file ../$(PARAM_FILE) \
		--execution-mode sequential \
		--no-mock-io
	@echo ""
	@echo "Output:"
	@ls -lh $(OUTPUT_DIR)
	@echo ""
	@python3 -m json.tool $(OUTPUT_DIR)/result.json 2>/dev/null || echo "No result.json"

clean:
	rm -rf $(OUTPUT_DIR)
	@echo "Cleaned $(OUTPUT_DIR)"
