#Question 3

import streamlit as st
import sympy as sp


def show():
    st.header("Question 3: Polynomial Calculus")

    # Define the function
    t = sp.symbols('t')
    f = t**3 - 6*t**2 + 9*t + 2

    st.subheader("Given function")
    st.latex("f(t) = t^3 - 6t^2 + 9t + 2")

    # Factorization
    st.subheader("(a) Factorized function")
    factorized_function = sp.factor(f)
    st.latex(sp.latex(factorized_function))

    # Solve f(t) = 0
    st.subheader("(b) Solve f(t) = 0")
    solutions = sp.solve(f, t)
    st.write("Solutions:")
    st.latex(sp.latex(solutions))

    # Solve f(t) = 2
    st.subheader("(c) Solve f(t) = 2")
    solutions_f_t_2 = sp.solve(f - 2, t)
    st.write("Solutions:")
    st.latex(sp.latex(solutions_f_t_2))

    # First derivative
    st.subheader("(d) First derivative")
    derivative = sp.diff(f, t)
    st.latex("f'(t) = " + sp.latex(derivative))

    # Second derivative
    st.subheader("(e) Second derivative")
    second_derivative = sp.diff(derivative, t)
    st.latex("f''(t) = " + sp.latex(second_derivative))

    # Indefinite integral
    st.subheader("(f) Indefinite integral")
    integral = sp.integrate(f, t)
    st.latex(r"\int f(t)\,dt = " + sp.latex(integral) + " + C")

    # Definite integral from 0 to 2
    st.subheader("(g) Definite integral from 0 to 2")
    integral_0_2 = sp.integrate(f, (t, 0, 2))
    st.latex(
        r"\int_0^2 f(t)\,dt = " + sp.latex(integral_0_2)
    )
