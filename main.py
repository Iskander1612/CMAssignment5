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


def test_function(x):
    """Test function: sin(x)"""
    return np.sin(x)

a = 0
b = np.pi
n = 10

print("Integration of sin(x) from 0 to π")
print("=================================")
print(f"Number of intervals: {n}")
print(f"Exact value (analytical): {2.0:.10f}")
print(("================================="))

try:
    result = newton_cotes(test_function, a, b, n)
    print(f"Newton-Cotes:              {result:.10f}")
except Exception as e:
    print(f"Newton-Cotes:              Error - {e}")

try:
    result = trapezoidal_rule(test_function, a, b, n)
    print(f"Trapezoidal Rule:          {result:.10f}")
except Exception as e:
    print(f"Trapezoidal Rule:          Error - {e}")

try:
    result = simpsons_one_third(test_function, a, b, n)
    print(f"Simpson's 1/3 Rule:        {result:.10f}")
except Exception as e:
    print(f"Simpson's 1/3 Rule:        Error - {e}")

try:
    n_simp3 = 12  # Must be multiple of 3
    result = simpsons_three_eighth(test_function, a, b, n_simp3)
    print(f"Simpson's 3/8 Rule (n=12): {result:.10f}")
except Exception as e:
    print(f"Simpson's 3/8 Rule:        Error - {e}")

try:
    n_boole = 12  # Must be multiple of 4
    result = booles_rule(test_function, a, b, n_boole)
    print(f"Boole's Rule (n=12):       {result:.10f}")
except Exception as e:
    print(f"Boole's Rule:              Error - {e}")

try:
    n_weddle = 12  # Must be multiple of 6
    result = weddle_rule(test_function, a, b, n_weddle)
    print(f"Weddle's Rule (n=12):      {result:.10f}")
except Exception as e:
    print(f"Weddle's Rule:             Error - {e}")

print("=================================")