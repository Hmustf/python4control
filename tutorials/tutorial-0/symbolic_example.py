from sympy import symbols, solve, simplify, cos, sin

print("--- Symbolic Mathematics Examples ---")

# Define symbolic variables
x, y = symbols('x y')
print("Defined symbols:", x, y)

# Work with polynomials
pol = x**2 + 2*x + 1
print("\nPolynomial:", pol)
coeffs = pol.as_poly().all_coeffs()
print("Coefficients:", coeffs)

# Solve equations
solution = solve(pol, x)
print("\nSolutions to", pol, "= 0:")
print(solution)

# Simplify expressions
expr = cos(x)**2 + sin(x)**2
result = simplify(expr)
print("\nSimplifying", expr)
print("Result:", result) 