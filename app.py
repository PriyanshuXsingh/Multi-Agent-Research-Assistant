import io
import contextlib
from datetime import datetime

import streamlit as st

from pipeline import run_research_pipeline


# ---------- helpers ----------

def to_text(value) -> str:
    """Normalize chain/LLM outputs (strings or message objects) into plain text."""
    if value is None:
        return ""
    if hasattr(value, "content"):
        return value.content
    return str(value)


def reset_state():
    for key in ("result", "logs", "topic_run"):
        st.session_state.pop(key, None)


# ---------- page setup ----------

st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    layout="wide",
)

st.title("ReaseachGPT:Multi-Agent Research Assistant")
st.caption("Search agent → Reader agent → Writer chain → Critic chain")

with st.sidebar:
    st.subheader("How it works")
    st.markdown(
        "1. **Search agent** looks up recent, reliable sources on your topic.\n"
        "2. **Reader agent** picks the best result and scrapes it for depth.\n"
        "3. **Writer chain** drafts a report from the combined research.\n"
        "4. **Critic chain** reviews the report and gives feedback."
    )
    st.divider()
    if st.button("Start a new research run", use_container_width=True):
        reset_state()
        st.rerun()


# ---------- input form ----------

with st.form("research_form"):
    topic = st.text_input(
        "Research topic",
        placeholder="e.g. Impact of large language models on radiology",
    )
    submitted = st.form_submit_button("Run pipeline", use_container_width=True)

if submitted:
    if not topic.strip():
        st.warning("Please enter a topic before running the pipeline.")
    else:
        log_buffer = io.StringIO()
        start = datetime.now()
        try:
            with st.spinner("Running the multi-agent pipeline... this can take a minute or two."):
                with contextlib.redirect_stdout(log_buffer):
                    result = run_research_pipeline(topic)
        except Exception as exc:
            st.error(f"Pipeline failed: {exc}")
            st.code(log_buffer.getvalue() or "No logs captured.")
            st.stop()

        elapsed = (datetime.now() - start).total_seconds()
        st.session_state["result"] = result
        st.session_state["logs"] = log_buffer.getvalue()
        st.session_state["topic_run"] = topic
        st.session_state["elapsed"] = elapsed


# ---------- results ----------

if "result" in st.session_state:
    result = st.session_state["result"]
    st.success(
        f"Research complete for **{st.session_state['topic_run']}** "
        f"({st.session_state['elapsed']:.1f}s)"
    )

    report_text = to_text(result.get("report"))
    feedback_text = to_text(result.get("feedback"))
    search_text = to_text(result.get("search_results"))
    scraped_text = to_text(result.get("scraped_content"))

    tab_report, tab_feedback, tab_search, tab_scraped, tab_logs = st.tabs(
        ["Final Report", "Critic Feedback", "Search Results", "Scraped Content", "Process Logs"]
    )

    with tab_report:
        st.markdown(report_text)
        st.download_button(
            "Download report (.md)",
            data=report_text,
            file_name=f"{st.session_state['topic_run'].replace(' ', '_')}_report.md",
            mime="text/markdown",
        )

    with tab_feedback:
        st.markdown(feedback_text)

    with tab_search:
        st.text_area("Raw search results", search_text, height=400)

    with tab_scraped:
        st.text_area("Raw scraped content", scraped_text, height=400)

    with tab_logs:
        st.code(st.session_state.get("logs", "No logs captured."), language="text")
else:
    st.info("Enter a topic above and click **Run pipeline** to get started.")