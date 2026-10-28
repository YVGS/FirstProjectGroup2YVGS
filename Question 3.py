#Question 3

import sympy as sp

def function(t):
    return t**3 - 6*t**2 + 9*t + 2

t = sp.symbols('t')
factorized_function = sp.factor(function(t))
print('Factorized function:', factorized_function)

# f(t)=0
solutions = sp.solve(function(t), t)
print('Solutions:', solutions)

#f(t) = 2
solutions_f_t_2 = sp.solve(function(t) - 2, t)
print('Solutions for f(t) = 2:', solutions_f_t_2)

#f'(t)
derivative = sp.diff(function(t), t)
print('Derivative:', derivative)

#f"(t)
second_derivative = sp.diff(derivative, t)
print('Second Derivative:', second_derivative)

#integral of f(t)
integral = sp.integrate(function(t), t)
print('Integral of f(t):', integral)

#integral of f(t) from 0 to 2
integral_0_2 = sp.integrate(function(t), (t, 0, 2))
print('Integral of f(t) from 0 to 2:', integral_0_2)

