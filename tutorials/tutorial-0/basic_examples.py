import numpy as np

# Basic variable examples
x = 123.3
print("Float:", x)
x = "Some text"
print("String:", x)
x = True
print("Boolean:", x)

print("\n--- Arrays ---")
# NumPy array examples
x = np.array([1, 2, 3, 4])
print("Basic array:", x)

# Creating from variables
x1, x2, x3, x4 = 1, 2, 3, 4
x = np.array([x1, x2, x3, x4])
print("Array from variables:", x)

# NumPy functions
x = np.zeros(4)
print("Zeros array:", x)
y = np.ones((2, 2))
print("Ones matrix:\n", y)
z = np.linspace(0, 1, 5)
print("Linspace array:", z)

print("\n--- Mixed Data ---")
# Lists with mixed types
mixed_data = [123, "some text", True]
print("Mixed data list:", mixed_data)

print("\n--- Control Flow ---")
# If statement example
a = 2
if a > 2:
    print("The given number is bigger than 2")
elif a == 2:
    print("The given number is equal to 2")
else:
    print("The given number is less than 2")

print("\n--- Loops ---")
# Loop examples
print("While loop:")
i = 1
while i < 5:
    print(i)
    i += 1

print("\nFor loop:")
for i in range(1, 5):
    print(i)

print("\n--- Functions ---")
# Function example
def square(x):
    """Square a number."""
    return x * x

x = 2
y = square(x)
print(f"Square of {x} is {y}") 