import numpy as np
from scipy.integrate import solve_ivp

def ode_system(t, y, a=1.0, b=0.5):
    # Defines a linear ODE: dy/dt = ay + b
    return a * y + b

def solve_ode():
    y0 = [0]  # Initial condition
    t_span = (0, 10)  # Time interval
    t_eval = np.linspace(*t_span, 100)  # Points to evaluate the solution

    solution = solve_ivp(ode_system, t_span, y0, t_eval=t_eval)

    return solution.t, solution.y[0]


# Example usage
t, y = solve_ode()
print("Time values:", t[:5])      # Print first 5 time points
print("ODE values:", y[:5])       # Print first 5 solution values
