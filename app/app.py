import json
import datetime as dt
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Procore AI Field Assistant — Mock", layout="wide", page_icon="🦺")

css_path = Path(__file__).parent / "theme.css"
st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

# Topbar
st.markdown(
    "<div class='pc-topbar'><div class='title'>🦺 Procore AI Field Assistant <span class='small-muted'>— mock demo</span></div>"
    "<div class='badge'>Guided • Templates • JSON</div></div>",
    unsafe_allow_html=True
)
st.write("")

with st.sidebar:
    st.markdown("### Project")
    project = st.text_input("Select project", "Main Street Bridge")
    st.markdown("---")
    st.markdown("**Quick Tips**")
    st.caption("• Use plain language.\n\n• The assistant structures data for Procore.\n\n• Download JSON for upload or future API.")
    st.markdown("---")
    st.caption("Skin: Procore‑style | No live APIs")

# Tabs: existing + new
tab1, tab2, tab3, tab4, tab5 = st.tabs(["✅ Inspection", "📒 Daily Log", "📨 RFI", "🧰 Template Builder", "📊 Adoption Dashboard"])

data_dir = Path(__file__).resolve().parent.parent / "data"

# ---------- INSPECTION ----------
with tab1:
    st.markdown("<div class='pc-card'>", unsafe_allow_html=True)
    st.markdown("#### Safety Inspection (Field Mode)")
    st.markdown("<div class='pc-steps'><div class='pc-step done'>1 · Basics</div><div class='pc-step'>2 · Checks</div><div class='pc-step'>3 · Review</div></div>", unsafe_allow_html=True)

    workers = st.number_input("Workers on site", min_value=0, value=12, step=1)
    incidents = st.multiselect("Incidents", ["None", "Near Miss", "First Aid", "Recordable"], default=["None"])
    note = st.text_area("Notes", "Debris near Pier 3")

    colA, colB = st.columns([1,1])
    with colA:
        attach = st.file_uploader("Attach photos (optional)", type=["jpg","png","jpeg"], accept_multiple_files=True)
    with colB:
        st.markdown("<div class='pc-section'>Template</div>", unsafe_allow_html=True)
        st.caption("Using standard Safety Inspection v1.2")

    st.markdown("<div class='pc-divider'></div>", unsafe_allow_html=True)
    if st.button("Generate Inspection JSON", type="primary", use_container_width=True):
        data = json.loads((data_dir / "inspection_example.json").read_text())
        data["project"] = project
        data["team"]["workers_on_site"] = int(workers)
        data["incidents"] = [] if ("None" in incidents or len(incidents)==0) else incidents
        data["checklist"][2]["notes"] = note
        if attach:
            data["attachments"] = [f.name for f in attach]
        st.success("Inspection ready for Procore upload (simulated).")
        st.json(data)
        st.download_button("Download inspection.json", data=json.dumps(data, indent=2), file_name="inspection.json", mime="application/json")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- DAILY LOG ----------
with tab2:
    st.markdown("<div class='pc-card'>", unsafe_allow_html=True)
    st.markdown("#### Daily Log")
    st.markdown("<div class='pc-steps'><div class='pc-step done'>1 · Weather</div><div class='pc-step'>2 · Labor & Equip</div><div class='pc-step'>3 · Review</div></div>", unsafe_allow_html=True)

    delay = st.number_input("Weather delay (hours)", min_value=0.0, value=2.0, step=0.5)
    note = st.text_area("Notes", "Coordinate lane closure schedule for Thursday")

    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown("<div class='pc-section'>Labor</div>", unsafe_allow_html=True)
        conc = st.number_input("Concrete crew", min_value=0, value=8, step=1)
        elec = st.number_input("Electrical crew", min_value=0, value=4, step=1)
    with col2:
        st.markdown("<div class='pc-section'>Equipment</div>", unsafe_allow_html=True)
        ex_hours = st.number_input("Excavator CAT320 (hrs)", min_value=0.0, value=6.5, step=0.5)
        sc_hours = st.number_input("Scissor lift (hrs)", min_value=0.0, value=3.0, step=0.5)

    st.markdown("<div class='pc-divider'></div>", unsafe_allow_html=True)
    if st.button("Generate Daily Log JSON", type="primary", use_container_width=True):
        data = json.loads((data_dir / "daily_log_example.json").read_text())
        data["project"] = project
        data["notes"] = note
        data["weather"]["am"] = f"Delay {delay}h"
        data["labor"][0]["count"] = int(conc)
        data["labor"][1]["count"] = int(elec)
        data["equipment"][0]["hours"] = float(ex_hours)
        data["equipment"][1]["hours"] = float(sc_hours)
        st.success("Daily Log ready for Procore upload (simulated).")
        st.json(data)
        st.download_button("Download daily_log.json", data=json.dumps(data, indent=2), file_name="daily_log.json", mime="application/json")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- RFI ----------
with tab3:
    st.markdown("<div class='pc-card'>", unsafe_allow_html=True)
    st.markdown("#### RFI")
    st.markdown("<div class='pc-steps'><div class='pc-step done'>1 · Draft</div><div class='pc-step'>2 · Attach</div><div class='pc-step'>3 · Review</div></div>", unsafe_allow_html=True)

    subject = st.text_input("Subject", "Clarification on conduit routing near East abutment")
    proposed = st.text_area("Proposed Solution", "Use 2.5\\\" conduit with strut support at 5' spacing.")
    due = st.date_input("Required By", dt.date.today())

    attach_rfi = st.file_uploader("Attach references (photos/PDF)", type=["jpg","png","jpeg","pdf"], accept_multiple_files=True)

    st.markdown("<div class='pc-divider'></div>", unsafe_allow_html=True)
    if st.button("Generate RFI JSON", type="primary", use_container_width=True):
        data = json.loads((data_dir / "rfi_example.json").read_text())
        data["project"] = project
        data["subject"] = subject
        data["proposed_solution"] = proposed
        data["required_date"] = str(due)
        if attach_rfi:
            data["attachments"] = [f.name for f in attach_rfi]
        st.success("RFI ready for Procore upload (simulated).")
        st.json(data)
        st.download_button("Download rfi.json", data=json.dumps(data, indent=2), file_name="rfi.json", mime="application/json")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- TEMPLATE BUILDER (new) ----------
with tab4:
    st.markdown("<div class='pc-card'>", unsafe_allow_html=True)
    st.markdown("#### Template Builder")
    st.caption("Create reusable Action Plans & Inspections aligned to SOPs and KPIs.")

    catalog = json.loads((data_dir / "template_catalog.json").read_text())
    choice = st.selectbox("Template type", list(catalog.keys()))
    version = st.text_input("Version label", "v1.0")
    owner = st.text_input("Owner / Discipline", "Safety")
    kpis = catalog[choice]["kpis"]

    st.markdown("<div class='pc-section'>Preview KPIs</div>", unsafe_allow_html=True)
    st.write(", ".join(kpis))

    if st.button("Generate Action Plan JSON", type="primary", use_container_width=True):
        out = {
            "project": project,
            "template_name": choice,
            "version": version,
            "owner": owner,
            "category": catalog[choice]["category"],
            "kpis": kpis,
            "checklist_version": catalog[choice]["checklist_version"],
            "created": str(dt.date.today()),
            "status": "Reusable Template"
        }
        st.success("Action Plan template generated.")
        st.json(out)
        st.download_button("Download action_plan.json", data=json.dumps(out, indent=2), file_name="action_plan.json", mime="application/json")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- ADOPTION DASHBOARD (new) ----------
with tab5:
    st.markdown("<div class='pc-card'>", unsafe_allow_html=True)
    st.markdown("#### Adoption Dashboard (Mock)")
    st.caption("What we'd track during a pilot to drive real adoption.")
    dash = json.loads((data_dir / "adoption_dashboard_mock.json").read_text())

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Template Usage", f"{int(dash['template_usage_rate']*100)}%")
    c2.metric("Avg Time Saved", f"{dash['avg_time_saved_minutes']} min")
    c3.metric("SOP Views", dash["sop_views"])
    c4.metric("Active Users", dash["active_users"])
    c5.metric("Positive Feedback", f"{int(dash['feedback_positive_pct']*100)}%")

    st.markdown("<div class='pc-divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='pc-section'>Project Adoption</div>", unsafe_allow_html=True)
    for proj in dash["projects"]:
        st.write(f"{proj['name']}: {int(proj['adoption']*100)}%")
        st.progress(proj["adoption"])

    st.markdown("<div class='pc-section'>8‑Week Trend</div>", unsafe_allow_html=True)
    st.line_chart(dash["trend_last_8_weeks"])

    st.markdown("</div>", unsafe_allow_html=True)
