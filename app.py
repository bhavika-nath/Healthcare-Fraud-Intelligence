import streamlit as st
import pandas as pd
import requests

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Healthcare Fraud Intelligence Platform",
    layout="wide"
)

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("Dashboards/powerbi_data/provider_dashboard_data.csv")

df = load_data()

# -----------------------------
# Ollama / Llama Connection
# -----------------------------
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1"

def ask_llama(prompt):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    return response.json()["response"]

# -----------------------------
# KPI Calculations
# -----------------------------
total_providers = df["rndrng_npi"].nunique()
total_payments = df["tot_mdcr_pymt_amt"].sum()
avg_risk = df["fraud_risk_score"].mean()
high_risk = (df["risk_category"] == "High Risk").sum()

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("Healthcare Fraud Platform")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "AI Assistant",
        "Provider Search",
        "Analytics",
        "Data Preview"
    ]
)

# -----------------------------
# Home Page
# -----------------------------
if page == "Home":
    st.title("Healthcare Fraud Intelligence Platform")
    st.caption("AI-powered Medicare provider fraud investigation assistant")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Providers", f"{total_providers:,}")
    col2.metric("Total Medicare Payments", f"${total_payments / 1e9:.2f}B")
    col3.metric("Average Fraud Risk", f"{avg_risk:.2f}")
    col4.metric("High-Risk Providers", f"{high_risk:,}")

    st.divider()

    st.subheader("Project Overview")
    st.write(
        "This platform analyzes CMS Medicare provider data to identify high-risk billing patterns, "
        "prioritize providers for review, and support fraud investigation using machine learning, "
        "Power BI dashboards, SHAP explainability, and a local Llama 3.1 AI assistant."
    )

# -----------------------------
# AI Assistant Page
# -----------------------------
elif page == "AI Assistant":
    st.title("AI Healthcare Fraud Investigation Assistant")
    st.caption("Ask natural-language questions about provider risk, billing behavior, specialties, and Medicare payments.")

    question = st.text_input(
        "Ask a fraud investigation question",
        placeholder="Example: Which providers should investigators review first?"
    )

    if st.button("Ask AI"):
        if question.strip() == "":
            st.warning("Please enter a question.")
        else:
            with st.spinner("Analyzing fraud data with Llama 3.1..."):
                top_high_risk = (
                    df[df["risk_category"] == "High Risk"]
                    .sort_values("fraud_risk_score", ascending=False)
                    .head(10)
                )

                context = f"""
Dataset Summary:
Total Providers: {total_providers:,}
Total Medicare Payments: ${total_payments:,.2f}
Average Fraud Risk Score: {avg_risk:.2f}
High-Risk Providers: {high_risk:,}

Top High-Risk Providers:
{top_high_risk.to_string(index=False)}
"""

                prompt = f"""
You are an AI Healthcare Fraud Investigation Assistant.

User Question:
{question}


Use only this healthcare fraud dataset context:
{context}

Instructions:
- Answer clearly like a fraud analyst.
- Do not claim fraud is proven.
- Use terms like "high-risk", "unusual billing pattern", and "recommended for review".
- Explain why the result matters for healthcare fraud investigation.
- Keep the response concise and practical.
"""

                answer = ask_llama(prompt)

                st.subheader("AI Investigation Response")
                st.write(answer)

# -----------------------------
# Provider Search Page
# -----------------------------
elif page == "Provider Search":
    st.title("Provider Search")
    st.caption("Search providers by name, NPI, state, specialty, or risk category.")

    search_term = st.text_input("Search provider data")

    if search_term:
        result = df[
            df["rndrng_prvdr_last_org_name"].astype(str).str.contains(search_term, case=False, na=False)
            | df["rndrng_prvdr_first_name"].astype(str).str.contains(search_term, case=False, na=False)
            | df["rndrng_npi"].astype(str).str.contains(search_term, case=False, na=False)
            | df["rndrng_prvdr_state_abrvtn"].astype(str).str.contains(search_term, case=False, na=False)
            | df["rndrng_prvdr_type"].astype(str).str.contains(search_term, case=False, na=False)
            | df["risk_category"].astype(str).str.contains(search_term, case=False, na=False)
        ]

        st.write(f"Results found: {len(result):,}")

        display_cols = [
            "rndrng_npi",
            "rndrng_prvdr_last_org_name",
            "rndrng_prvdr_first_name",
            "rndrng_prvdr_type",
            "rndrng_prvdr_state_abrvtn",
            "risk_category",
            "fraud_risk_score",
            "tot_mdcr_pymt_amt",
            "payment_per_beneficiary",
            "charge_to_payment_ratio"
        ]

        st.dataframe(
            result[display_cols].head(100),
            use_container_width=True
        )

# -----------------------------
# Analytics Page
# -----------------------------
elif page == "Analytics":
    st.title("Fraud Analytics")
    st.caption("Explore risk distribution, high-risk states, specialties, and provider-level fraud indicators.")

    st.subheader("Risk Category Distribution")
    risk_counts = df["risk_category"].value_counts()
    st.bar_chart(risk_counts)

    st.divider()

    st.subheader("Top 10 States by High-Risk Providers")
    state_high_risk = (
        df[df["risk_category"] == "High Risk"]["rndrng_prvdr_state_abrvtn"]
        .value_counts()
        .head(10)
    )
    st.bar_chart(state_high_risk)

    st.divider()

    st.subheader("Top 10 Specialties by Average Fraud Risk")
    specialty_risk = (
        df.groupby("rndrng_prvdr_type")["fraud_risk_score"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )
    st.bar_chart(specialty_risk)

    st.divider()

    st.subheader("Top 20 Providers by Fraud Risk Score")
    top_risk = (
        df.sort_values("fraud_risk_score", ascending=False)
        .head(20)
    )

    display_cols = [
        "rndrng_npi",
        "rndrng_prvdr_last_org_name",
        "rndrng_prvdr_first_name",
        "rndrng_prvdr_type",
        "rndrng_prvdr_state_abrvtn",
        "risk_category",
        "fraud_risk_score",
        "tot_mdcr_pymt_amt",
        "payment_per_beneficiary",
        "charge_to_payment_ratio"
    ]

    st.dataframe(
        top_risk[display_cols],
        use_container_width=True
    )

# -----------------------------
# Data Preview Page
# -----------------------------
elif page == "Data Preview":
    st.title("Provider Data Preview")
    st.caption("Preview the final dashboard-ready provider dataset used by the AI assistant and Power BI dashboard.")

    st.write("Dataset Shape:", df.shape)

    st.dataframe(
        df.head(100),
        use_container_width=True
    )
    