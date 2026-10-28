
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


def show():
    st.header("Question 4: Student Performance Analysis")

    # Load dataset
    file_path = Path(__file__).parent / "student_performance.csv"

    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        st.error(
            "student_performance.csv was not found. "
            "Place it in the same folder as Q4.py."
        )
        return

    # Dataset dimensions
    st.subheader("(a) Dataset overview")
    rows, columns = df.shape

    col1, col2 = st.columns(2)
    col1.metric("Number of rows", rows)
    col2.metric("Number of columns", columns)

    st.write("**Data types**")
    st.dataframe(
        df.dtypes.astype(str).rename("Data type").to_frame()
    )

    st.write("**First five rows**")
    st.dataframe(df.head(), use_container_width=True)

    # Summary statistics
    st.subheader("(b) Basic summary statistics")
    st.dataframe(df.describe(), use_container_width=True)

    # Check required columns
    required_columns = ["Study Hours", "Exam", "Assignment"]
    missing_columns = [
        col for col in required_columns if col not in df.columns
    ]

    if missing_columns:
        st.error(f"Missing required columns: {missing_columns}")
        return

    # Exam statistics
    st.subheader("(c) Exam score statistics")

    mean_exam_score = df["Exam"].mean()
    median_exam_score = df["Exam"].median()
    sd = df["Exam"].std()

    c1, c2, c3 = st.columns(3)
    c1.metric("Mean exam score", f"{mean_exam_score:.2f}")
    c2.metric("Median exam score", f"{median_exam_score:.2f}")
    c3.metric("Standard deviation", f"{sd:.2f}")

    # Student with highest exam marks
    st.write("**Student(s) with the highest exam marks**")
    highest_exam_score = df["Exam"].max()
    st.write(f"Highest exam score: {highest_exam_score}")
    st.dataframe(
        df[df["Exam"] == highest_exam_score],
        use_container_width=True
    )

    # Pearson correlation
    st.subheader("(d) Pearson correlation")
    r = df["Study Hours"].corr(df["Exam"], method="pearson")
    st.metric("Study Hours vs Exam", f"{r:.4f}")

    # Clean data
    st.subheader("(e) Clean and categorize data")

    original_rows = len(df)
    df = df.drop_duplicates()
    df = df.dropna(subset=required_columns).copy()
    removed_rows = original_rows - len(df)

    def categorize_marks(mark):
        if mark < 60:
            return "Low"
        elif mark < 80:
            return "Medium"
        else:
            return "High"

    df["Category"] = df["Exam"].apply(categorize_marks)

    st.write(f"Rows removed during cleaning: {removed_rows}")
    st.write("**Cleaned dataset with exam categories**")
    st.dataframe(df, use_container_width=True)

    # Summary statistics for cleaned data
    summary = df.describe(include="all")

    # Download files instead of saving to a fixed working directory
    cleaned_csv = df.to_csv(index=False).encode("utf-8")
    summary_csv = summary.to_csv().encode("utf-8")

    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            "Download cleaned data CSV",
            data=cleaned_csv,
            file_name="cleaned_data.csv",
            mime="text/csv"
        )

    with col2:
        st.download_button(
            "Download summary statistics CSV",
            data=summary_csv,
            file_name="summary_statistics.csv",
            mime="text/csv"
        )

    # Plots
    st.subheader("(f) Data visualizations")

    fig1, ax1 = plt.subplots(figsize=(8, 4))
    ax1.scatter(df["Study Hours"], df["Exam"])
    ax1.set_xlabel("Study Hours")
    ax1.set_ylabel("Exam Marks")
    ax1.set_title("Study Hours vs Exam Marks")
    ax1.grid(alpha=0.3)
    st.pyplot(fig1)
    plt.close(fig1)

    fig2, ax2 = plt.subplots(figsize=(8, 4))
    ax2.hist(df["Exam"], bins=10, edgecolor="black")
    ax2.set_xlabel("Exam Marks")
    ax2.set_ylabel("Frequency")
    ax2.set_title("Distribution of Exam Marks")
    st.pyplot(fig2)
    plt.close(fig2)

    fig3, ax3 = plt.subplots(figsize=(8, 4))
    sns.boxplot(y=df["Exam"], ax=ax3)
    ax3.set_ylabel("Exam Marks")
    ax3.set_title("Box Plot of Exam Marks")
    st.pyplot(fig3)
    plt.close(fig3)

    fig4, ax4 = plt.subplots(figsize=(6, 4))
    heatmap_data = df[["Study Hours", "Assignment"]].corr()

    sns.heatmap(
        heatmap_data,
        annot=True,
        vmin=-1,
        vmax=1,
        ax=ax4
    )

    ax4.set_title("Correlation Heatmap")
    st.pyplot(fig4)
    plt.close(fig4)
