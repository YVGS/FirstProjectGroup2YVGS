

import streamlit as st

import Q1
import Q2
import Q3
import Q4

# ---------------- Page setup ----------------
st.set_page_config(
    page_title="Group2 Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- Styling ----------------
st.markdown("""
<style>
    .main {
        background-color: #f7f9fc;
    }
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }
    .hero {
        padding: 24px;
        border-radius: 16px;
        background: linear-gradient(120deg, #e8f1ff, #f2eaff);
        border: 1px solid #e0e7f5;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.title("📊 group2 Dashboard")
st.caption("AM 3038/3084 · Week 04 Activity 01")

# ---------------- Sidebar navigation ----------------
page = st.sidebar.radio(
    "Navigate to a question",
    [
        "Home",
        "Question 1 · Statistics",
        "Question 2 · Matrices",
        "Question 3 · Calculus",
        "Question 4 · Student Data"
    ],
    key="main_navigation"
)

st.sidebar.markdown("---")
st.sidebar.caption("Python · NumPy · SymPy · Pandas · Matplotlib")

# ---------------- Page routing ----------------
if page == "Home":
    st.markdown("""
    <div class="hero">
        <h2>Welcome 👋</h2>
        <p>Explore the calculations and visualisations
        from Questions 1–4.</p>
        <p>Select a question from the sidebar to begin.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Dashboard modules")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### 📈 Question 1")
        st.write("Statistics and data visualisation.")

        st.markdown("### 🧮 Question 2")
        st.write("Matrix calculations and linear systems.")

    with c2:
        st.markdown("### ∫ Question 3")
        st.write("Polynomial calculations and calculus.")

        st.markdown("### 🎓 Question 4")
        st.write("Student data analysis and plots.")

elif page == "Question 1 · Statistics":
    Q1.show()

elif page == "Question 2 · Matrices":
    Q2.show()

elif page == "Question 3 · Calculus":
    Q3.show()

elif page == "Question 4 · Student Data":
    Q4.show()

# ---------------- Footer ----------------
st.markdown("---")
st.caption("AM 3038/3084 · Activity dashboard")






