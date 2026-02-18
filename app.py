import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =========================
# Title & Intro
# =========================
st.title("🎓 Smart Student Dashboard")
st.write("A simple Streamlit app to collect student details and visualize data.")

st.markdown("---")

# =========================
# Sidebar
# =========================
st.sidebar.title("📌 Navigation")
st.sidebar.write("Student Dashboard Demo")

# =========================
# Student Profile Section
# =========================
st.header("👤 Student Profile")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=100)
dob = st.date_input("Select your birth date")
about = st.text_area("Tell something about yourself")

course = st.selectbox(
    "Select your course",
    ["Computer Science", "Information Technology", "Electronics", "Mechanical"]
)

skills = st.multiselect(
    "Select your skills",
    ["Python", "Java", "C++", "Web Development", "Data Analysis"]
)

if st.button("Submit Profile"):
    st.success(f"Welcome {name}! Your profile has been submitted.")

st.markdown("---")

# =========================
# CSV Analyzer Section
# =========================
st.header("📊 CSV Analyzer")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

st.markdown("---")

# =========================
# Data Visualization Section
# =========================
st.header("📈 Data Visualization")

data = pd.DataFrame(
    np.random.randn(10, 2),
    columns=["Column A", "Column B"]
)

st.line_chart(data)
st.bar_chart(data)

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
ax.set_title("Sample Matplotlib Plot")
st.pyplot(fig)

st.markdown("---")

# =========================
# Code Showcase
# =========================
st.header("💻 Sample Code")

st.code(
    "for i in range(5):\n    print(i)",
    language="python"
)

