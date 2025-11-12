# app.py — thin launcher that runs the real app in app/app.py
import os, runpy, pathlib
base = pathlib.Path(__file__).parent
runpy.run_path(str(base / "app" / "app.py"))