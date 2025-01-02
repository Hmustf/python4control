# 🐍 Control System Design with Python

## Introduction to Python for Control Systems

Python is a versatile programming language widely used in scientific computing and engineering. With libraries like [NumPy](https://numpy.org/), [Control](https://python-control.org/), and [Matplotlib](https://matplotlib.org/), it provides powerful tools for control system analysis and design.

This tutorial will guide you through:
- Basic Python concepts for control systems
- Symbolic mathematics with SymPy
- Transfer function analysis
- System response visualization

> 💡 All code examples can be found in the following files:
> - [basic_examples.py](basic_examples.py)
> - [symbolic_example.py](symbolic_example.py)
> - [control_examples.py](control_examples.py)

### 🔧 Basic Python Concepts

Variables in Python are dynamically typed and easy to work with:

```python
x = 123.3        # float
x = "Some text"  # string
x = True         # boolean
```
Output:
```
Float: 123.3
String: Some text
Boolean: True
```

Engineers often work with signals (arrays), which are handled efficiently using NumPy:

```python
import numpy as np

x = np.array([1, 2, 3, 4])  # Create a numpy array
```
Output:
```
Basic array: [1 2 3 4]
```

Arrays can be created from individual variables:

```python
x1, x2, x3, x4 = 1, 2, 3, 4
x = np.array([x1, x2, x3, x4])
```
Output:
```
Array from variables: [1 2 3 4]
```

NumPy provides convenient functions for creating arrays:

```python
x = np.zeros(4)          # Array of zeros
y = np.ones((2, 2))      # 2x2 matrix of ones
z = np.linspace(0, 1, 5) # 5 evenly spaced points from 0 to 1
```
Output:
```
Zeros array: [0. 0. 0. 0.]
Ones matrix:
[[1. 1.]
 [1. 1.]]
Linspace array: [0.   0.25 0.5  0.75 1.  ]
```

### 🔄 Control Flow and Functions

Python's clean syntax makes control flow and functions intuitive:

```python
def square(x):
    """Square a number."""
    return x * x

x = 2
y = square(x)  # y = 4
```
Output:
```
Square of 2 is 4
```

### ➗ Symbolic Mathematics with SymPy

SymPy enables symbolic mathematics, which is crucial for control system analysis. For example, we can solve the quadratic equation:

$ax^2 + bx + c = 0$

Or simplify trigonometric identities like:

$\sin^2(x) + \cos^2(x) = 1$

Here's how to do it in code:

```python
from sympy import symbols, solve, simplify, cos, sin

# Define symbolic variables
x, y = symbols('x y')

# Work with polynomials
pol = x**2 + 2*x + 1  # Represents (x + 1)²
coeffs = pol.as_poly().all_coeffs()

# Solve equations
solution = solve(pol, x)

# Simplify expressions
result = simplify(cos(x)**2 + sin(x)**2)
```
Output:
```
--- Symbolic Mathematics Examples ---
Defined symbols: x y

Polynomial: x**2 + 2*x + 1
Coefficients: [1, 2, 1]

Solutions to x**2 + 2*x + 1 = 0:
[-1]

Simplifying sin(x)**2 + cos(x)**2
Result: 1
```

### 🎛️ Control Systems with Python Control

The `control` library lets us work with transfer functions and analyze system responses. For example, consider a second-order system:

$G(s) = \frac{1}{s^2 + 2s + 1}$

```python
import control
import numpy as np
import matplotlib.pyplot as plt

# Create transfer function
num = [1]
den = [1, 2, 1]
G = control.TransferFunction(num, den)

# Get system information
zeros, poles, gain = control.zero_pole_gain(G)

# Plot step response
t = np.linspace(0, 10, 1000)
t, y = control.step_response(G, t)
plt.plot(t, y)
plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Step Response')
plt.show()
```

The resulting step response plot:

![Basic Step Response](plots/basic_response.png)

### 📊 First-Order System Comparison

Let's compare first-order systems with different time constants. The transfer function form is:

$G(s) = \frac{a}{s + a}$

where $a$ is the inverse of the time constant $\tau = \frac{1}{a}$.

```python
import numpy as np
import matplotlib.pyplot as plt
from control import TransferFunction, step_response

plt.figure(figsize=(10, 6))
t = np.linspace(0, 5, 1000)

for a in range(1, 6):
    G = TransferFunction([a], [1, a])
    t, y = step_response(G, t)
    plt.plot(t, y, linewidth=2, label=f'a = {a}')

plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Step Responses of First-Order Systems')
plt.legend()
plt.show()
```

The resulting comparison plot:

![First Order System Comparison](plots/first_order_comparison.png)

---

This tutorial demonstrates how Python can be used effectively for control system analysis and design. The combination of NumPy for numerical computations, Control for system analysis, and Matplotlib for visualization makes Python a powerful tool for control engineering. 

📚 **Further Reading**:
- [Python Control Systems Library Documentation](https://python-control.readthedocs.io/)
- [NumPy Documentation](https://numpy.org/doc/)
- [SymPy Tutorial](https://docs.sympy.org/latest/tutorial/) 