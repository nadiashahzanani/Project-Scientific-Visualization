import streamlit as st

# Page configuration
st.set_page_config(
    page_title="TikTok Shop Impulse Buying Study",
    layout="wide"
)

# Title
st.title("📊 Determinants of Students' Impulse Buying Behavior on TikTok Shop")

# Project Overview
st.markdown("""
### 🎯 Project Overview
This Streamlit application presents an interactive analysis of **students' impulse buying behavior on TikTok Shop** based on survey data collected from students.
""")

st.markdown("---")

# Group Problem Statement
st.subheader("📌 Problem Statement")
st.write("""
TikTok Shop has become very popular among students because it combines entertainment, promotions, and instant purchasing in one platform. 
Many students end up buying products impulsively without planning or careful consideration. 
However, students are often not fully aware of what factors influence their impulse buying behavior, such as promotions, product presentation, trust, and social influence.

At the same time, sellers and marketers lack clear visual insights into how these factors affect students’ purchasing decisions. 
Without proper data analysis and visualization, it is difficult to understand patterns, trends, and relationships within impulse buying behavior. 
Therefore, there is a need to analyze and visualize survey data to better understand the determinants of students’ impulse buying behavior on TikTok Shop.
""")

# Group Objectives
st.subheader("🎯 Project Objectives")
st.write("""
1. To identify the key factors that influence students’ impulse buying behavior on TikTok Shop.  
2. To analyze students’ impulse buying tendencies using survey data collected through an online questionnaire.  
3. To apply scientific visualization techniques to present impulse buying patterns clearly and effectively.  
4. To explore relationships between demographic factors (such as age, gender, and income) and impulse buying behavior.
""")

# Features
st.subheader("✨ Features")
st.write("""
- Interactive filters for demographic information (age, gender, income)
- Five different scientific visualizations showing the impact of key factors
- Clear interpretation of impulse buying behavior for better understanding
- Streamlit-based interactive dashboard for real-time data exploration
""")

# Tools
st.subheader("🛠 Tools Used")
st.write("""
- Python  
- Streamlit  
- Pandas  
- Plotly (for interactive visualizations)  
- Matplotlib  
- Seaborn  
""")

# Dataset Info
st.subheader("📂 Dataset")
st.write("""
Survey responses were collected from university students using Google Forms.
""")

# Deployment Info
st.subheader("🚀 Deployment")
st.write("""
The application is deployed using [Streamlit Cloud](https://share.streamlit.io/) and provides an interactive interface for exploring the survey results and visualizations.
""")

# Sidebar navigation info
st.markdown("---")
st.markdown("""
### 👥 Group Members & Pages
Use the sidebar to navigate between pages:

- **Main Page** – Project overview  
- **Member Pages** – MemberA (Nadia Shahzanani)
                   - MemberB
                   - Memberc
                   - MemberD

Each member focuses on a **different objective** using scientific visualization techniques.
""")
st.info("📌 Navigate using the sidebar on the left.")
