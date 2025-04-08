import streamlit as st

st.title("🧮 Model Inputs Explained")
st.markdown("This page provides an in-depth explanation of the input parameters used in the relationship game theory model.")

st.header("🔹 Emotional Stability")
with st.expander("Why it matters"):
    st.markdown("""
    Emotional stability reflects a person's ability to remain calm, resilient, and composed under stress. It's a cornerstone of **relationship durability**.  
    - Higher emotional stability = less conflict escalation  
    - Strong correlation with **secure attachment** and **long-term satisfaction**

    **Studies:**
    - _Costa & McCrae (1992)_: Low neuroticism (high emotional stability) strongly predicts romantic satisfaction.
    - _Gottman Institute_: Emotional regulation is a top predictor of marital success.
    """)

st.header("🔹 Value Alignment")
with st.expander("What is 'Value Alignment'?"):
    st.markdown("""
    Value alignment refers to the degree to which both partners **share fundamental beliefs**, life goals, and ethics.  
    Misalignment often leads to major conflicts over time — especially in long-term relationships.

    **Measured dimensions:**
    - Beliefs around family, children, money, religion
    - Lifestyle expectations
    - Ambition and future planning

    **Why it matters:**
    - Shared values increase **mutual respect**, decision-making harmony, and reduce friction in crisis.

    **Studies:**
    - _Finkel et al. (2014)_: Partners with aligned long-term goals report higher life satisfaction.
    - _Psychology Today_: Value congruence is more predictive of longevity than shared hobbies.
    """)

st.header("🔹 Probable Life Events")
with st.expander("How they affect compatibility"):
    st.markdown("""
    Life throws curveballs. This model simulates **how each partner adapts to change**.

    These events include:
    - **Career Growth**: Who thrives or struggles with change in ambition?
    - **Emotional Burnout**: Do you support each other or collapse together?
    - **Relocation**: Willingness to move can strain or strengthen a relationship.
    - **Parenthood**: Involves values, emotional energy, and mutual support.
    - **Health Events**: Can highlight emotional capacity and future planning compatibility.

    The scores in the simulator reflect **relative gain or stress** from each event, showing how robust the bond is over time.
    """)