import json
import streamlit as st
from pathlib import Path
import datetime

st.set_page_config(page_title="Procore AI Field Assistant (Mock)", layout="centered")

st.title("Procore AI Field Assistant — Mock Demo")
st.caption("No API keys required. This demo uses canned logic and JSON templates.")

st.markdown("### Choose a workflow")
flow = st.selectbox("Workflow", ["Inspection", "Daily Log", "RFI"])

project = st.text_input("Project", "Main Street Bridge")

if flow == "Inspection":
    workers = st.number_input("Workers on site", min_value=0, value=12)
    incidents = st.multiselect("Incidents", ["None", "Near Miss", "First Aid", "Recordable"])
    notes = st.text_area("Notes", "Debris near Pier 3")
    if st.button("Generate Inspection JSON"):
        data = json.loads(Path("../data/inspection_example.json").read_text())
        data["project"] = project
        data["team"]["workers_on_site"] = workers
        data["incidents"] = [] if "None" in incidents or not incidents else incidents
        data["checklist"][2]["notes"] = notes
        st.success("Inspection ready for Procore upload (simulated).")
        st.json(data)

elif flow == "Daily Log":
    delay_hours = st.number_input("Weather delay (hours)", min_value=0.0, value=2.0, step=0.5)
    note = st.text_area("Notes", "Coordinate lane closure schedule for Thursday")
    if st.button("Generate Daily Log JSON"):
        data = json.loads(Path("../data/daily_log_example.json").read_text())
        data["project"] = project
        data["notes"] = note
        data["weather"]["am"] = f"Delay {delay_hours}h"
        st.success("Daily Log ready for Procore upload (simulated).")
        st.json(data)

else:
    subject = st.text_input("RFI Subject", "Clarification on conduit routing near East abutment")
    proposed = st.text_area("Proposed Solution", "Use 2.5" conduit with strut support at 5' spacing.")
    if st.button("Generate RFI JSON"):
        data = json.loads(Path("../data/rfi_example.json").read_text())
        data["project"] = project
        data["subject"] = subject
        data["proposed_solution"] = proposed
        data["required_date"] = str(datetime.date.today())
        st.success("RFI ready for Procore upload (simulated).")
        st.json(data)

st.markdown("---")
st.markdown("**Tip:** Replace canned JSON with your templates or connect to live services when ready.")
