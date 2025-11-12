# Makefile for Procore AI Field Assistant (local demo)
VENV := .venv
PY := python3
VPY := $(VENV)/bin/python

.PHONY: setup run clean reinstall

setup:
	@echo "🚀 Ensuring virtual environment and dependencies..."
	@[ -d $(VENV) ] || $(PY) -m venv $(VENV)
	@$(VPY) -m pip install --upgrade pip
	@$(VPY) -m pip install -r app/requirements.txt
	@echo "✅ Setup complete! Run 'make run' to start the demo."

run:
	@echo "▶️  Starting Streamlit app..."
	@[ -d $(VENV) ] || (echo 'No venv found. Run "make setup" first.' && exit 1)
	@$(VPY) -m streamlit run app/app.py

reinstall:
	@echo "🔁 Reinstalling dependencies..."
	@[ -d $(VENV) ] || $(PY) -m venv $(VENV)
	@$(VPY) -m pip install --upgrade pip
	@$(VPY) -m pip install --force-reinstall -r app/requirements.txt

clean:
	@echo "🧹 Removing virtual environment and caches..."
	@rm -rf $(VENV) __pycache__ */__pycache__