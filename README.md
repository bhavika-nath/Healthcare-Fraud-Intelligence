# 🏥 Healthcare Fraud Intelligence Platform

AI-powered healthcare fraud detection platform built using **Python, SQL, Hive, PostgreSQL, Machine Learning, SHAP, Power BI, Streamlit, and Llama 3.1**.

---

# Project Overview

Healthcare fraud results in billions of dollars in unnecessary healthcare spending every year. This project analyzes Medicare provider billing data to identify providers with unusual billing patterns and prioritize them for further investigation.

The platform combines data engineering, machine learning, explainable AI, business intelligence, and generative AI into a complete fraud analytics solution.

---

# Key Features

- Detect high-risk healthcare providers using machine learning
- Engineer fraud-related risk indicators
- Explain fraud predictions using SHAP
- Analyze provider billing behavior
- Interactive Power BI dashboard
- AI-powered fraud investigation assistant using Llama 3.1
- Streamlit web application
- Provider search and fraud analytics dashboard

---

# Technology Stack

| Category | Technologies |
|-----------|--------------|
| Programming | Python, SQL |
| Big Data | Apache Hive |
| Database | PostgreSQL |
| Machine Learning | Isolation Forest |
| Explainable AI | SHAP |
| Visualization | Power BI |
| Web Application | Streamlit |
| AI Assistant | Ollama, Llama 3.1 |
| Version Control | Git, GitHub |

---

# Dataset

**Source**

CMS Medicare Provider Utilization and Payment Data

Dataset Size

- 1,296,739 Providers
- 16 Features
- Medicare Payments
- Provider Specialty
- State Information
- Fraud Risk Score
- Risk Category

---

# Project Workflow

```text
CMS Medicare Data
        │
        ▼
Data Cleaning
(Python)
        │
        ▼
Hive Analytics
        │
        ▼
PostgreSQL Data Warehouse
        │
        ▼
Feature Engineering
        │
        ▼
Isolation Forest
Machine Learning
        │
        ▼
SHAP Explainability
        │
        ▼
Power BI Dashboard
        │
        ▼
AI Investigation Assistant
(Llama 3.1)
        │
        ▼
Streamlit Web Application
```

---

# Project Structure

```
Healthcare-Fraud-Intelligence
│
├── ai_assistant/
├── Dashboards/
│   └── powerbi_data/
├── data/
├── Images/
├── Notebooks/
│   ├── 01_Data_Understanding.ipynb
│   ├── 02_DataCleaning.ipynb
│   ├── 03_Hive_Analytics.ipynb
│   ├── 04_PostgreSQL_Data_Warehouse.ipynb
│   ├── 05_Feature_Engineering.ipynb
│   ├── 06_Fraud_Detection_Model.ipynb
│   ├── 07_SHAP_Explainability.ipynb
│   ├── 08_PowerBI_Dashboard_Data.ipynb
│   ├── 09_AI_Assistant.ipynb
│   └── 10_AI_Investigation_Assistant.ipynb
│
├── app.py
├── requirements.txt
└── README.md
```

---

# Machine Learning Pipeline

- Data preprocessing
- Feature engineering
- Fraud risk score generation
- Isolation Forest anomaly detection
- SHAP explainability
- High-risk provider identification

---

# Power BI Dashboard

The dashboard includes:

- Executive KPI Summary
- Medicare Payment Analysis
- High-Risk Provider Detection
- State-Level Fraud Analysis
- Specialty Risk Analysis
- Provider Search
- Fraud Risk Indicators

---

# AI Investigation Assistant

The AI assistant uses **Llama 3.1** running locally with **Ollama** to answer natural language questions about the Medicare dataset.

### Example Questions

- Which providers should investigators review first?
- Which specialties have the highest fraud risk?
- Which states have the most high-risk providers?
- Summarize the healthcare fraud dashboard.
- Which providers received the highest Medicare payments?
- Explain unusual billing patterns.
- Compare California and Texas.
- Which specialties should investigators prioritize?

---

# Streamlit Application

The web application includes:

- Home Dashboard
- KPI Summary
- AI Investigation Assistant
- Provider Search
- Fraud Analytics
- Interactive Charts
- Dataset Preview

---

# Installation

Clone the repository

```bash
git clone https://github.com/bhavika-nath/Healthcare-Fraud-Intelligence.git
```

Go to the project folder

```bash
cd Healthcare-Fraud-Intelligence
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start Ollama

```bash
ollama run llama3.1
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

# Results

- Processed over **1.29 million Medicare provider records**
- Identified **5,620 high-risk providers**
- Generated fraud risk scores using machine learning
- Built explainable AI insights with SHAP
- Created interactive Power BI dashboards
- Developed an AI-powered investigation assistant for fraud analysis

---

# Future Improvements

- Real-time fraud monitoring
- Cloud deployment (Azure/AWS)
- Retrieval-Augmented Generation (RAG)
- Multi-model AI support
- Automated investigation report generation
- Interactive geospatial fraud maps

---

# Author

**Bhavika Gungurthi**

Master of Information Systems

Iowa State University

### Areas of Interest

- Data Analytics
- Data Engineering
- Machine Learning
- Business Intelligence
- Artificial Intelligence

---

## License

This project is intended for educational and portfolio purposes.
