import control
import numpy as np
import matplotlib.pyplot as plt
import os

# Create output directory if it doesn't exist
os.makedirs('docs/images/examples', exist_ok=True)

# System Responses Examples
print("\nRunning System Responses Examples...")

# Step Response Example
G = control.TransferFunction([1], [1, 1])
t, y = control.step_response(G)

plt.figure()
plt.plot(t, y)
plt.grid(True)
plt.title('Step Response')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.savefig('docs/images/examples/step_response.png')
plt.close()

print("Step Response Output:")
print(f"Final Value: {y[-1]:.2f}")
print(f"Rise Time: {t[np.where(y >= 0.9)[0][0]]:.2f} seconds")

# Impulse Response Example
t, y = control.impulse_response(G)

plt.figure()
plt.plot(t, y)
plt.grid(True)
plt.title('Impulse Response')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.savefig('docs/images/examples/impulse_response.png')
plt.close()

print("\nImpulse Response Output:")
print(f"Peak Value: {max(abs(y)):.2f}")

# Root Locus Examples
print("\nRunning Root Locus Examples...")

# Simple Second-Order System
num = [1]
den = [1, 2, 0]  # s^2 + 2s
G = control.TransferFunction(num, den)

plt.figure(figsize=(10, 8))
control.root_locus(G)
plt.title('Root Locus: G(s) = 1/s(s + 2)')
plt.grid(True)
plt.savefig('docs/images/examples/root_locus_simple.png')
plt.close()

# Multiple Poles System
G = control.TransferFunction([1], [1, 6, 11, 6])

plt.figure(figsize=(10, 8))
control.root_locus(G)
plt.title('Root Locus: G(s) = 1/((s+1)(s+2)(s+3))')
plt.grid(True)
plt.savefig('docs/images/examples/root_locus_multiple.png')
plt.close()

# Bode Plot Examples
print("\nRunning Bode Plot Examples...")

# First-Order System
tau = 1.0
G = control.TransferFunction([1], [tau, 1])

plt.figure(figsize=(10, 10))
control.bode_plot(G, dB=True)
plt.suptitle('Bode Plot: First-Order System')
plt.savefig('docs/images/examples/bode_first_order.png')
plt.close()

# Second-Order System
wn = 10.0
zeta = 0.5
num = [wn**2]
den = [1, 2*zeta*wn, wn**2]
G = control.TransferFunction(num, den)

plt.figure(figsize=(10, 10))
control.bode_plot(G, dB=True)
plt.suptitle('Bode Plot: Second-Order System')
plt.savefig('docs/images/examples/bode_second_order.png')
plt.close()

# Band-Pass Filter
f0 = 100
Q = 10
w0 = 2 * np.pi * f0

num = [w0/Q, 0]
den = [1, w0/Q, w0**2]
G = control.TransferFunction(num, den)

plt.figure(figsize=(10, 10))
control.bode_plot(G, dB=True)
plt.suptitle('Bode Plot: Band-Pass Filter')
plt.savefig('docs/images/examples/bode_bandpass.png')
plt.close()

# Calculate stability margins
gm, pm, wg, wp = control.margin(G)
print("\nStability Margins for Band-Pass Filter:")
print(f"Gain Margin: {gm:.2f} dB at {wg:.2f} rad/s")
print(f"Phase Margin: {pm:.2f} degrees at {wp:.2f} rad/s")

print("\nAll examples completed successfully!") 