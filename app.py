import streamlit as st

st.set_page_config(
    page_title="TreeSense AI",
    page_icon="🌳",
    layout="wide"
)

st.title("🌳 TreeSense AI")

st.subheader("AI-Based Urban Tree Health Monitoring System")

st.write(
    """
    TreeSense AI is an intelligent urban tree monitoring platform
    designed to assess tree health using image analysis, field
    observations and geospatial information.
    """
)

st.success("TreeSense AI is running successfully!")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Healthy Trees", "0")

with col2:
    st.metric("Moderately Stressed", "0")

with col3:
    st.metric("Diseased / Damaged", "0")

st.markdown("---")

st.info(
    "The AI diagnosis, tree inventory and interactive health map "
    "will be added in the next development stage."
)
