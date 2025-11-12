# Makefile for Procore AI Field Assistant (local demo)

# Virtual environment folder
VENV := .venv
PY := python3

.PHONY: setup run clean

setup:
	@echo "🚀 Creating virtual environment and installing requirements..."
	@$(PY) -m venv $(VENV)
	@. $(VENV)/bin/activate; \
	$(PY) -m pip install --upgrade pip; \
	pip install -r app/requirements.txt
	@echo "✅ Setup complete! Run 'make run' to start the demo."

run:
	@echo "▶️  Starting Streamlit app..."
	@. $(VENV)/bin/activate; \
	streamlit run app/app.py

clean:
	@echo "🧹 Removing virtual environment and caches..."
	@rm -rf $(VENV) __pycache__ */__pycache__
