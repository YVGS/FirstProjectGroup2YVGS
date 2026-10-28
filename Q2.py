import numpy  as np
import streamlit as st


def show():
    st.header("Question 2: Matrix Calculations")

    # Define matrices
    A = np.array([
        [2, 1, 1],
        [1, 3, 2],
        [3, 1, 2]
    ])

    B = np.array([
        [10],
        [18],
        [17]
    ])

    # Display matrices
    st.subheader("(a) Given matrices")
    col1, col2 = st.columns(2)

    with col1:
        st.write("Matrix A")
        st.write(A)

    with col2:
        st.write("Matrix B")
        st.write(B)

    # Determinant
    st.subheader("(b) Determinant of A")
    st.write(f"det(A) = {np.linalg.det(A):.4f}")

    # Inverse
    st.subheader("(c) Inverse of A")
    st.write(np.linalg.inv(A))

    # Eigenvalues and eigenvectors
    st.subheader("(d) Eigenvalues and eigenvectors")

    eigenvalues, eigenvectors = np.linalg.eig(A)

    st.write("Eigenvalues:")
    st.write(eigenvalues)

    st.write("Eigenvectors (columns):")
    st.write(eigenvectors)

    # Solve AX = B
    st.subheader("(e) Solve AX = B")

    X = np.linalg.solve(A, B)

    st.write("Solution [x, y, z]:")
    st.write(X)

    # Residual
    st.subheader("(f) Residual")

    R = A @ X - B

    st.write("Residual vector:")
    st.write(R)

    st.write(
        "Euclidean norm of residual:",
        f"{np.linalg.norm(R, ord=2):.10f}"
    )
