import numpy as np

# 1. Newton-Cotes Integration Formula (Closed, General n)
def newton_cotes(f, a, b, n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    
    # Simpson's weights for Newton-Cotes
    weights = np.zeros(n + 1)
    weights[0] = weights[-1] = 1
    weights[1:-1] = 4 - 2 * (np.arange(1, n) % 2 == 0)
    
    integral = (h / 3) * np.sum(weights * f(x))
    return integral

# 2. Trapezoidal Rule
def trapezoidal_rule(f, a, b, n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    integral = (h / 2) * (f(x[0]) + 2 * np.sum(f(x[1:-1])) + f(x[-1]))
    
    return integral

# 3. Simpson's One-Third Rule
def simpsons_one_third(f, a, b, n):

    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n % 2 == 1:
        raise ValueError("n must be even for Simpson's 1/3 rule")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    integral = (h / 3) * (f(x[0]) + f(x[-1]) + 4 * np.sum(f(x[1:-1:2])) + 2 * np.sum(f(x[2:-1:2])))
    
    return integral

# 4. Simpson's Three-Eighth Rule
def simpsons_three_eighth(f, a, b, n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n % 3 != 0:
        raise ValueError("n must be a multiple of 3 for Simpson's 3/8 rule")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    
    # Simpson's 3/8 formula: integral = (3h/8) * [f(x0) + 3*sum(f(x_{3k+1})) + 3*sum(f(x_{3k+2})) + 2*sum(f(x_{3k})) + f(xn)]
    integral = (3 * h / 8) * (f(x[0]) + 3 * np.sum(f(x[1::3])) + 3 * np.sum(f(x[2::3])) + 2 * np.sum(f(x[3::3])) + f(x[-1]))
    
    return integral

# 5. Boole's Rule
def booles_rule(f, a, b, n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n % 4 != 0:
        raise ValueError("n must be a multiple of 4 for Boole's rule")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    
    # Boole's formula weights: 7, 32, 12, 32, 7 for 5-point rule
    integral = (2 * h / 45) * (7 * f(x[0]) + 7 * f(x[-1]) + 
                               32 * (np.sum(f(x[1::4])) + np.sum(f(x[3::4]))) + 
                               12 * np.sum(f(x[2::4])))
    
    return integral

# 6. Weddle's Rule
def weddle_rule(f, a, b, n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n % 6 != 0:
        raise ValueError("n must be a multiple of 6 for Weddle's rule")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    
    # Weddle's formula weights: 41, 216, 27, 272 for 7-point rule
    integral = (3 * h / 10) * (f(x[0]) + f(x[-1]) + 
                               5 * (np.sum(f(x[1::6])) + np.sum(f(x[5::6]))) + 
                               np.sum(f(x[2::6])) + np.sum(f(x[4::6])) + 
                               6 * np.sum(f(x[3::6])))
    
    return integral


def f(x):
    return np.sin(x)

a = 0
b = np.pi

print("Num integral sin(x) от 0 до π\n")

n = 10
print(f" Trapezoidal rule (n={n}):    {trapezoidal_rule(f, a, b, n):.10f}")
print(f"Simpson's 1/3 Rule (n={n}):     {simpsons_one_third(f, a, b, n):.10f}")

n = 12
print(f"Simpson's 3/8 Rule (n={n}):    {simpsons_three_eighth(f, a, b, n):.10f}")
print(f"Boole's Rule (n={n}):             {booles_rule(f, a, b, n):.10f}")
print(f"Weddle's Rule(n={n}):          {weddle_rule(f, a, b, n):.10f}")

print(f"\nExact value: 2.0")