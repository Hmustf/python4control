import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.integrate import odeint
import control

# Set random seed for reproducibility
np.random.seed(42)

# Set default figure size and style
plt.style.use('default')  # Use default clean style
plt.rcParams.update({
    'figure.figsize': [10, 6],
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'font.size': 12,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'lines.linewidth': 2,
    'grid.linestyle': '--',
    'grid.alpha': 0.7,
    'axes.grid': True,
    'axes.axisbelow': True,
    'axes.labelpad': 10,
    'axes.spines.top': False,
    'axes.spines.right': False
})

def save_basic_examples():
    """Generate and save outputs for basic Python examples"""
    print("\n=== Basic Python Examples ===")
    # Basic variable assignments
    x = 123.3
    text = "Some text"
    flag = True
    print(f"x = {x}, text = {text}, flag = {flag}")

    # Lists
    x = [1, 2, 3, 4]
    print("List x:", x)

    # NumPy arrays
    x = np.array([1, 2, 3, 4])
    print("NumPy array x:", x)

    # Arrays of zeros and ones
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

def save_symbolic_math():
    """Generate and save outputs for symbolic mathematics examples"""
    print("\n=== Symbolic Mathematics with SymPy ===")
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

def save_differential_equations():
    """Generate and save outputs for differential equations examples"""
    print("\n=== Solving Differential Equations ===")
    
    # Define the differential equation dy/dt = -y
    def model(y, t):
        return -y

    # Time points
    t = np.linspace(0, 5, 100)
    y0 = 1  # Initial condition
    
    # Solve ODE
    solution = odeint(model, y0, t)
    
    # Plot results
    plt.figure()
    plt.plot(t, solution, color='#1f77b4', label='y(t)')
    plt.plot(t, np.exp(-t), '--', color='#d62728', label='Analytical: e^(-t)')
    plt.xlabel('Time')
    plt.ylabel('y(t)')
    plt.title('Solution of dy/dt = -y')
    plt.legend()
    plt.savefig('docs/images/examples/differential_equation.png')
    plt.close()

    # Print solution values
    print("Solution values at t = [0, 1, 2, 3, 4, 5]:")
    t_points = [0, 1, 2, 3, 4, 5]
    y_points = np.interp(t_points, t, solution.flatten())
    for t_val, y_val in zip(t_points, y_points):
        print(f"t = {t_val:.1f}, y = {y_val:.4f}")

def save_advanced_plotting():
    """Generate and save outputs for advanced plotting examples"""
    print("\n=== Advanced Plotting Examples ===")
    
    # Multiple plots and subplots
    t = np.linspace(0, 10, 1000)
    f1 = np.sin(t)
    f2 = np.cos(t)
    f3 = np.exp(-0.1*t)*np.sin(t)

    # Create figure with subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    # First subplot: Multiple functions
    ax1.plot(t, f1, '-', label='sin(t)', color='#1f77b4')
    ax1.plot(t, f2, '--', label='cos(t)', color='#d62728')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Amplitude')
    ax1.set_title('Trigonometric Functions')
    ax1.legend()

    # Second subplot: Damped oscillation with two y-axes
    ax2.plot(t, f3, '-', label='Damped oscillation', color='#2ca02c')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Amplitude', color='#2ca02c')
    ax2.tick_params(axis='y', labelcolor='#2ca02c')

    # Add second y-axis
    ax3 = ax2.twinx()
    ax3.plot(t, np.exp(-0.1*t), '--', label='Envelope', color='#1f77b4')
    ax3.set_ylabel('Envelope', color='#1f77b4')
    ax3.tick_params(axis='y', labelcolor='#1f77b4')
    ax3.spines['right'].set_visible(True)
    ax3.spines['right'].set_color('#1f77b4')
    ax2.spines['left'].set_color('#2ca02c')

    # Add combined legend
    lines1, labels1 = ax2.get_legend_handles_labels()
    lines2, labels2 = ax3.get_legend_handles_labels()
    ax3.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

    plt.tight_layout()
    plt.savefig('docs/images/examples/multiple_plots.png')
    plt.close()

    # Print some data points
    print("Data points at t = [0, π/2, π]:")
    t_points = [0, np.pi/2, np.pi]
    for t_val in t_points:
        idx = np.abs(t - t_val).argmin()
        print(f"t = {t_val:.4f}:")
        print(f"  sin(t) = {f1[idx]:.4f}")
        print(f"  cos(t) = {f2[idx]:.4f}")
        print(f"  damped sin(t) = {f3[idx]:.4f}")

    # Scatter plot with color mapping
    plt.figure(figsize=(10, 8))
    x = np.random.normal(0, 1, 1000)
    y = np.random.normal(0, 1, 1000)
    z = np.sqrt(x**2 + y**2)

    scatter = plt.scatter(x, y, c=z, cmap='viridis', s=50, alpha=0.6)
    plt.colorbar(scatter, label='Distance from origin')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter Plot with Color Mapping')
    plt.axis('equal')
    plt.savefig('docs/images/examples/scatter_plot.png')
    plt.close()

    # Print statistics
    print("\nData statistics:")
    print(f"X mean: {np.mean(x):.4f}, std: {np.std(x):.4f}")
    print(f"Y mean: {np.mean(y):.4f}, std: {np.std(y):.4f}")
    print(f"Average distance from origin: {np.mean(z):.4f}")
    print(f"Maximum distance from origin: {np.max(z):.4f}")

def save_control_examples():
    """Generate and save outputs for control systems examples"""
    print("\n=== Control Systems Examples ===")
    
    # Single step response
    s = control.TransferFunction.s
    G = control.TransferFunction([1, 2], [1, 2, 1])
    print("Transfer function G(s):")
    print(G)

    t, y = control.step_response(G)
    plt.figure()
    plt.plot(t, y, '-', color='#1f77b4')
    plt.title('Step Response')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.savefig('docs/images/examples/step_response.png')
    plt.close()

    # Multiple step responses
    plt.figure()
    t = np.linspace(0, 5, 500)
    
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    for i, a in enumerate(range(1, 6)):
        G = control.TransferFunction([a], [1, a])
        print(f"\nTransfer function for a={a}:")
        print(G)
        
        t, y = control.step_response(G, t)
        plt.plot(t, y, '-', label=f'a={a}', color=colors[i])

    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Step Responses for Different Systems')
    plt.legend(loc='lower right')
    plt.savefig('docs/images/examples/multiple_step_responses.png')
    plt.close()

if __name__ == "__main__":
    # Run all examples and save outputs
    save_basic_examples()
    save_symbolic_math()
    save_differential_equations()
    save_advanced_plotting()
    save_control_examples() 