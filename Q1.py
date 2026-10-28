import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

#Question 1 

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def show():
    st.header("Question 1: Statistics")

    # Original data
    A = np.array([
        5, 2, 8, 4, 7, 1, 5, 10, 4, 7,
        3, 6, 3, 5, 2, 7, 4, 9, 5, 11
    ])

    st.subheader("(a) and (b) Original data statistics")

    mean = np.mean(A)
    median = np.median(A)
    sample_variance = np.var(A, ddof=1)
    standard_deviation = np.std(A, ddof=1)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Mean", f"{mean:.2f}")
    c2.metric("Median", f"{median:.2f}")
    c3.metric("Sample Variance", f"{sample_variance:.2f}")
    c4.metric("Standard Deviation", f"{standard_deviation:.2f}")

    # Modified data
    st.subheader("(c) Modified data")

    A2 = A.copy()
    A2[2] = 12

    st.write("Modified array A2:")
    st.write(A2)

    mean2 = np.mean(A2)
    median2 = np.median(A2)
    sample_variance2 = np.var(A2, ddof=1)
    standard_deviation2 = np.std(A2, ddof=1)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Mean", f"{mean2:.2f}")
    c2.metric("Median", f"{median2:.2f}")
    c3.metric("Sample Variance", f"{sample_variance2:.2f}")
    c4.metric("Standard Deviation", f"{standard_deviation2:.2f}")

    # Histogram
    st.subheader("(d) Histogram of A2")

    fig, ax = plt.subplots(figsize=(9, 4))

    ax.hist(
        A2,
        bins=np.arange(0.5, 13.5, 1),
        edgecolor="black"
    )

    ax.set_title("Histogram of A2")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_xticks(range(1, 13))

    ax.grid(axis="y", alpha=0.3)
    st.pyplot(fig)
    plt.close(fig)
