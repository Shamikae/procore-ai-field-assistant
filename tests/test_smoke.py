import json
from pathlib import Path

def test_requirements_present():
    assert (Path("app") / "requirements.txt").exists()

def test_app_importable():
    # We don't run Streamlit; just ensure the app file loads without syntax errors
    app_path = Path("app") / "app.py"
    code = app_path.read_text(encoding="utf-8")
    compile(code, str(app_path), "exec")

def test_sample_jsons_valid():
    for p in ["data/inspection_example.json", "data/daily_log_example.json", "data/rfi_example.json", "data/adoption_dashboard_mock.json", "data/template_catalog.json"]:
        path = Path(p)
        assert path.exists(), f"Missing {p}"
        json.loads(path.read_text())