# Control System Design with Python

### Introduction to Python for Control Systems

Python is a versatile programming language that's excellent for control systems engineering. We'll use several key libraries:

* `numpy` for numerical computations
    * Efficient array operations
    * Linear algebra functions
    * Mathematical functions
* `control` for control systems analysis
    * Transfer function creation and manipulation
    * System analysis tools
    * Control design methods
* `matplotlib` for plotting
    * 2D and 3D plotting
    * Multiple plot types
    * Customizable visualizations
* `sympy` for symbolic mathematics
    * Symbolic calculations
    * Equation solving
    * Laplace transforms
* `scipy` for scientific computing and differential equations
    * Differential equation solvers
    * Optimization tools
    * Signal processing functions

### Basic Python Concepts

Python's syntax is clean and readable. Here are some basic examples:

```python
# Basic variable assignments
x = 123.3
text = "Some text"
flag = True
print(f"x = {x}, text = {text}, flag = {flag}")

# Lists (similar to arrays in other languages)
x = [1, 2, 3, 4]
print("List x:", x)

# Using NumPy for numerical arrays
import numpy as np
x = np.array([1, 2, 3, 4])
print("NumPy array x:", x)

# Creating arrays of zeros and ones
x = np.zeros(4)
y = np.ones((2, 2))
print("Array of zeros:", x)
print("2x2 array of ones:\n", y)

# Array operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("\nArray operations:")
print("a + b =", a + b)
print("a * b =", a * b)
print("a dot b =", np.dot(a, b))
```
```
Output:
x = 123.3, text = Some text, flag = True
List x: [1, 2, 3, 4]
NumPy array x: [1 2 3 4]
Array of zeros: [0. 0. 0. 0.]
2x2 array of ones:
 [[1. 1.]
  [1. 1.]]

Array operations:
a + b = [5 7 9]
a * b = [ 4 10 18]
a dot b = 32
```

### Symbolic Mathematics with SymPy

SymPy is a powerful library for symbolic mathematics. Here's how to use it:

```python
import sympy as sp

# Define symbolic variables
t = sp.Symbol('t')
s = sp.Symbol('s')
x = sp.Symbol('x')

# Create and manipulate expressions
expr = x**2 + 2*x + 1
print("Original expression:", expr)
print("Derivative:", sp.diff(expr, x))
print("Integral:", sp.integrate(expr, x))

# Solve equations
eq = sp.Eq(x**2 + 2*x + 1, 0)
solution = sp.solve(eq, x)
print("\nSolving x^2 + 2x + 1 = 0:")
print("x =", solution)

# Laplace transforms
f_t = t**2 * sp.exp(-t)
F_s = sp.laplace_transform(f_t, t, s)
print("\nLaplace transform of t^2 * e^(-t):")
print("F(s) =", F_s[0])

# Matrix operations
M = sp.Matrix([[1, 2], [3, 4]])
print("\nMatrix operations:")
print("Matrix M:\n", M)
print("Determinant:", M.det())
print("Inverse:\n", M.inv())
```
```
Output:
Original expression: x**2 + 2*x + 1
Derivative: 2*x + 2
Integral: x**3/3 + x**2 + x

Solving x^2 + 2x + 1 = 0:
x = [-1]

Laplace transform of t^2 * e^(-t):
F(s) = 2/(s + 1)**3

Matrix operations:
Matrix M:
 Matrix([[1, 2], [3, 4]])
Determinant: -2
Inverse:
 Matrix([[-2, 1], [3/2, -1/2]])
```

### Solving Differential Equations

Python offers multiple ways to solve differential equations. Here's an example solving dy/dt = -y:

```python
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the differential equation dy/dt = -y
def model(y, t):
    return -y

# Time points
t = np.linspace(0, 5, 100)
y0 = 1  # Initial condition

# Solve ODE
solution = odeint(model, y0, t)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(t, solution, 'b-', label='y(t)')
plt.plot(t, np.exp(-t), 'r--', label='Analytical: e^(-t)')
plt.grid(True)
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.title('Solution of dy/dt = -y')
plt.legend()
plt.show()

# Print solution values
print("Solution values at t = [0, 1, 2, 3, 4, 5]:")
t_points = [0, 1, 2, 3, 4, 5]
y_points = np.interp(t_points, t, solution.flatten())
for t_val, y_val in zip(t_points, y_points):
    print(f"t = {t_val:.1f}, y = {y_val:.4f}")
```
```
Output:
Solution values at t = [0, 1, 2, 3, 4, 5]:
t = 0.0, y = 1.0000
t = 1.0, y = 0.3680
t = 2.0, y = 0.1354
t = 3.0, y = 0.0498
t = 4.0, y = 0.0183
t = 5.0, y = 0.0067
```

![Differential Equation Solution](../images/examples/differential_equation.png){: .responsive-image }

### Advanced Plotting Techniques

#### Multiple Plots and Subplots

Here's how to create multiple plots with different y-axes:

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate data
t = np.linspace(0, 10, 1000)
f1 = np.sin(t)
f2 = np.cos(t)
f3 = np.exp(-0.1*t)*np.sin(t)

# Create figure with subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# First subplot: Multiple functions
ax1.plot(t, f1, 'b-', label='sin(t)')
ax1.plot(t, f2, 'r--', label='cos(t)')
ax1.grid(True)
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax1.set_title('Trigonometric Functions')
ax1.legend()

# Second subplot: Damped oscillation with two y-axes
ax2.plot(t, f3, 'g-', label='Damped oscillation')
ax2.set_xlabel('Time')
ax2.set_ylabel('Amplitude', color='g')
ax2.tick_params(axis='y', labelcolor='g')
ax2.grid(True)

# Add second y-axis
ax3 = ax2.twinx()
ax3.plot(t, np.exp(-0.1*t), 'b--', label='Envelope')
ax3.set_ylabel('Envelope', color='b')
ax3.tick_params(axis='y', labelcolor='b')

# Add combined legend
lines1, labels1 = ax2.get_legend_handles_labels()
lines2, labels2 = ax3.get_legend_handles_labels()
ax3.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

plt.tight_layout()
plt.show()

# Print some data points
print("Data points at t = [0, π/2, π]:")
t_points = [0, np.pi/2, np.pi]
for t_val in t_points:
    idx = np.abs(t - t_val).argmin()
    print(f"t = {t_val:.4f}:")
    print(f"  sin(t) = {f1[idx]:.4f}")
    print(f"  cos(t) = {f2[idx]:.4f}")
    print(f"  damped sin(t) = {f3[idx]:.4f}")
```
```
Output:
Data points at t = [0, π/2, π]:
t = 0.0000:
  sin(t) = 0.0000
  cos(t) = 1.0000
  damped sin(t) = 0.0000
t = 1.5708:
  sin(t) = 1.0000
  cos(t) = -0.0008
  damped sin(t) = 0.8546
t = 3.1416:
  sin(t) = -0.0016
  cos(t) = -1.0000
  damped sin(t) = -0.0011
```

![Multiple Plots Example](../images/examples/multiple_plots.png){: .responsive-image }

#### Scatter Plots with Color Mapping

Here's how to create a scatter plot with color mapping:

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(42)
x = np.random.normal(0, 1, 1000)
y = np.random.normal(0, 1, 1000)
z = np.sqrt(x**2 + y**2)  # Distance from origin

# Create scatter plot
plt.figure(figsize=(10, 8))
scatter = plt.scatter(x, y, c=z, cmap='viridis', 
                     s=50, alpha=0.5)
plt.colorbar(scatter, label='Distance from origin')
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot with Color Mapping')
plt.axis('equal')
plt.show()

# Print statistics
print("Data statistics:")
print(f"X mean: {np.mean(x):.4f}, std: {np.std(x):.4f}")
print(f"Y mean: {np.mean(y):.4f}, std: {np.std(y):.4f}")
print(f"Average distance from origin: {np.mean(z):.4f}")
print(f"Maximum distance from origin: {np.max(z):.4f}")
```
```
Output:
Data statistics:
X mean: 0.0193, std: 0.9787
Y mean: 0.0708, std: 0.9970
Average distance from origin: 1.2327
Maximum distance from origin: 4.2314
```

![Scatter Plot Example](../images/examples/scatter_plot.png){: .responsive-image }

### Control Systems with Python Control

The `control` library provides powerful tools for control systems analysis. Let's look at some basic examples:

#### Single Step Response
Here's how to create a transfer function and plot its step response:

```python
import control
import numpy as np
import matplotlib.pyplot as plt

# Create a transfer function G(s) = (s + 2)/(s^2 + 2s + 1)
s = control.TransferFunction.s
G = control.TransferFunction([1, 2], [1, 2, 1])

# Print transfer function
print("Transfer function G(s):")
print(G)

# Generate and plot step response
t, y = control.step_response(G)
plt.figure(figsize=(10, 6))
plt.plot(t, y, linewidth=2)
plt.grid(True)
plt.title('Step Response')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()
```
```
Output:
Transfer function G(s):
       s + 2
-------------------
s^2 + 2 s + 1
```

![Step Response](../images/examples/step_response.png){: .responsive-image }

#### Multiple Step Responses
We can also compare step responses of different systems:

```python
import control
import numpy as np
import matplotlib.pyplot as plt

# Create figure
plt.figure(figsize=(10, 6))
t = np.linspace(0, 5, 500)

# Generate step responses for different systems
for a in range(1, 6):
    # Create transfer function G(s) = a/(s + a)
    G = control.TransferFunction([a], [1, a])
    print(f"\nTransfer function for a={a}:")
    print(G)
    
    # Get and plot step response
    t, y = control.step_response(G, t)
    plt.plot(t, y, linewidth=2, label=f'a={a}')

plt.grid(True)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Step Responses for Different Systems')
plt.legend(loc='lower right')
plt.show()
```
```
Output:
Transfer function for a=1:
  1
-----
s + 1

Transfer function for a=2:
  2
-----
s + 2

Transfer function for a=3:
  3
-----
s + 3

Transfer function for a=4:
  4
-----
s + 4

Transfer function for a=5:
  5
-----
s + 5
```

![Multiple Step Responses](../images/examples/multiple_step_responses.png){: .responsive-image }

This example shows how to:
1. Create transfer functions with different parameters
2. Generate step responses
3. Plot multiple responses on the same graph
4. Add proper labels and legends

The Python ecosystem provides these powerful tools for control systems analysis, making it an excellent choice for control system design and analysis.
