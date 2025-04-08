# Relationship Game Theory App with Short-term vs Long-term Toggle, Decision Trees, and Dynamic Power Balance

import streamlit as st
import math

st.set_page_config(page_title="Relationship Game Theory Tool", layout="wide")

st.title("💘 Relationship Compatibility: Game Theory Edition")

st.markdown("""
A tool that uses **game theory + decision trees** to:
- Measure compatibility
- Simulate power balance dynamics
- Compare short-term vs long-term relationship strategies

---

### 🧠 Understanding Power & Strategy in Relationships

This tool models the interaction of rational decision-making with emotional, economic, and psychological compatibility. It draws on insights from:
- **Short-term game theory**: Often driven by immediate gratification, resource signaling, and impression management (see Trivers' Parental Investment Theory).
- **Long-term game theory**: Focused on cooperation, trust-building, resilience to life events, and shared future goals (see Axelrod’s Iterated Prisoner’s Dilemma).

**Power balance** in this model reflects differences in leverage and attraction. While 'dominant' partners may exert more influence, the healthiest relationships often show dynamic equilibrium — where influence adapts over time.

---
""")

# ------------------------ INPUTS --------------------------
st.header("🔢 Personal Parameters")
col1, col2 = st.columns(2)

with col1:
    your_age = st.slider("Your Age", 18, 60, 25)
    your_income = st.selectbox("Your Monthly Income (USD)", ["< $1000", "$1000-$3000", "$3000-$10,000", "> $10,000"])
    your_occupation = st.selectbox("Your Occupation", ["Engineering", "Medicine", "Tech", "Academia", "Other"])
    your_emotional_stability = st.slider("Your Emotional Stability (0-10)", 0, 10, 7)
    your_values = st.slider("Your Value Alignment (0-10)", 0, 10, 8)

with col2:
    partner_age = st.slider("Partner Age", 18, 60, 37)
    partner_income = st.selectbox("Partner Monthly Income (USD)", ["< $1000", "$1000-$3000", "$3000-$10,000", "> $10,000"])
    partner_occupation = st.selectbox("Partner Occupation", ["Engineering", "Medicine", "Tech", "Academia", "Other"])
    partner_emotional_stability = st.slider("Partner Emotional Stability (0-10)", 0, 10, 6)
    partner_values = st.slider("Partner Value Alignment (0-10)", 0, 10, 8)

strategy = st.radio("Which strategy are you modeling?", ["🏃 Short-term", "🐢 Long-term"], horizontal=True)

# ------------------------ SCORING --------------------------
income_score = {"< $1000": 1, "$1000-$3000": 2, "$3000-$10,000": 3, "> $10,000": 4}
occupation_score = {"Engineering": 3, "Medicine": 4, "Tech": 4, "Academia": 2, "Other": 2}

if strategy == "🏃 Short-term":
    weights = dict(age=0.3, income=2, occupation=1.5, emotional=1, values=1)
else:
    weights = dict(age=0.1, income=1.2, occupation=1.2, emotional=2.5, values=2.5)

your_score = (
    (60 - abs(your_age - partner_age)) * weights['age'] +
    income_score[your_income] * weights['income'] +
    occupation_score[your_occupation] * weights['occupation'] +
    your_emotional_stability * weights['emotional'] +
    your_values * weights['values']
)

partner_score = (
    (60 - abs(partner_age - your_age)) * weights['age'] +
    income_score[partner_income] * weights['income'] +
    occupation_score[partner_occupation] * weights['occupation'] +
    partner_emotional_stability * weights['emotional'] +
    partner_values * weights['values']
)

compatibility = round((your_score + partner_score) / 2, 2)
power_balance = round(abs(your_score - partner_score), 2)
dominant = "Equal" if power_balance < 3 else ("You" if your_score > partner_score else "Partner")

# ------------------------ OUTPUT --------------------------
st.header("📊 Compatibility & Power Dynamics")
st.metric("❤️ Compatibility Score", compatibility)
st.metric("⚖️ Power Balance", power_balance)
st.metric("🧠 Dominant Partner", dominant)

# ------------------------ DECISION TREE -------------------
st.header("🌿 Future Scenarios")
scenarios = {
    "Career Growth": (3, 2),
    "Emotional Burnout": (-2, -3),
    "Relocation Willingness": (2, 1),
    "Children / Parenthood": (4, 4),
    "Health Events": (-3, -2)
}

st.subheader("🤔 Probable Life Events")
for event, (you_outcome, partner_outcome) in scenarios.items():
    st.write(f"**{event}**: You gain {you_outcome}, Partner gains {partner_outcome}")

future_score_you = sum([v[0] for v in scenarios.values()])
future_score_partner = sum([v[1] for v in scenarios.values()])

st.metric("📈 Your Long-Term Outcome Score", future_score_you)
st.metric("📈 Partner's Long-Term Outcome Score", future_score_partner)

# ------------------------ NOTE ----------------------------
st.info("""
This tool is an evolving experiment in applying **rational choice theory**, **affective computing**, and **behavioral economics** to relationships. It's not deterministic, but rather an interactive lens for thoughtful reflection.
""")
