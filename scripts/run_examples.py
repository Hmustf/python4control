import control
import numpy as np
import matplotlib.pyplot as plt
import os

# Create output directory if it doesn't exist
os.makedirs('docs/images/examples', exist_ok=True)

def print_separator():
    print("\n" + "="*50 + "\n")

# System Responses Examples
print_separator()
print("SYSTEM RESPONSES EXAMPLES")
print_separator()

# Step Response Example
print("1. Step Response Example")
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

print("Transfer Function G(s) = 1/(s + 1)")
print(f"Final Value: {y[-1]:.2f}")
print(f"Rise Time: {t[np.where(y >= 0.9)[0][0]]:.2f} seconds")
print(f"Settling Time: {t[np.where(np.abs(y - y[-1]) <= 0.02*y[-1])[0][0]]:.2f} seconds")

# Impulse Response Example
print_separator()
print("2. Impulse Response Example")
t, y = control.impulse_response(G)

plt.figure()
plt.plot(t, y)
plt.grid(True)
plt.title('Impulse Response')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.savefig('docs/images/examples/impulse_response.png')
plt.close()

print("Transfer Function G(s) = 1/(s + 1)")
print(f"Peak Value: {max(abs(y)):.2f}")
print(f"Peak Time: {t[np.argmax(abs(y))]:.2f} seconds")
print(f"Settling Time: {t[np.where(np.abs(y) <= 0.02*max(abs(y)))[0][0]]:.2f} seconds")

# Ramp Response Example
print_separator()
print("3. Ramp Response Example")
t = np.linspace(0, 10, 1000)
u = t
t_out, y = control.forced_response(G, T=t, U=u)

plt.figure()
plt.plot(t_out, u, '--', label='Input')
plt.plot(t_out, y, label='Output')
plt.grid(True)
plt.title('Ramp Response')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.savefig('docs/images/examples/ramp_response.png')
plt.close()

print("Transfer Function G(s) = 1/(s + 1)")
print(f"Steady-State Error Rate: {abs(u[-1] - y[-1]):.2f}")

# Second-Order System Example
print_separator()
print("4. Second-Order System Example")
wn = 1.0  # Natural frequency
zeta = 0.5  # Damping ratio
G2 = control.TransferFunction([wn**2], [1, 2*zeta*wn, wn**2])
t, y = control.step_response(G2)

plt.figure()
plt.plot(t, y)
plt.grid(True)
plt.title('Second-Order System Step Response')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

info = control.step_info(G2)
plt.annotate(f'Rise Time: {info["RiseTime"]:.2f}s', xy=(info["RiseTime"], 0.5))
plt.annotate(f'Peak Time: {info["PeakTime"]:.2f}s', xy=(info["PeakTime"], info["Peak"]))
plt.annotate(f'Overshoot: {info["Overshoot"]:.1f}%', xy=(info["PeakTime"], info["Peak"]))
plt.annotate(f'Settling Time: {info["SettlingTime"]:.2f}s', xy=(info["SettlingTime"], 1))
plt.savefig('docs/images/examples/second_order_response.png')
plt.close()

print("Transfer Function G(s) = ωn²/(s² + 2ζωn·s + ωn²)")
print(f"Natural Frequency (ωn): {wn:.2f} rad/s")
print(f"Damping Ratio (ζ): {zeta:.2f}")
print(f"Rise Time: {info['RiseTime']:.2f} seconds")
print(f"Peak Time: {info['PeakTime']:.2f} seconds")
print(f"Overshoot: {info['Overshoot']:.1f}%")
print(f"Settling Time: {info['SettlingTime']:.2f} seconds")

# Root Locus Examples
print_separator()
print("ROOT LOCUS EXAMPLES")
print_separator()

# Simple Second-Order System
print("1. Simple Second-Order System")
num = [1]
den = [1, 2, 0]  # s^2 + 2s
G = control.TransferFunction(num, den)

plt.figure(figsize=(10, 8))
rlist, klist = control.root_locus(G, plot=True)
plt.title('Root Locus: G(s) = 1/s(s + 2)')
plt.grid(True)
plt.savefig('docs/images/examples/root_locus_simple.png')
plt.close()

print("Transfer Function G(s) = 1/s(s + 2)")
print("Open-Loop Poles:", control.poles(G))
k_crit = klist[np.where(np.abs(np.real(rlist)) < 0.01)[0][0]]
print(f"Critical Gain (K) at Imaginary Axis: {k_crit:.2f}")

# Multiple Poles System
print_separator()
print("2. Multiple Poles System")
G = control.TransferFunction([1], [1, 6, 11, 6])

plt.figure(figsize=(10, 8))
rlist, klist = control.root_locus(G, plot=True)
plt.title('Root Locus: G(s) = 1/((s+1)(s+2)(s+3))')
plt.grid(True)
plt.savefig('docs/images/examples/root_locus_multiple.png')
plt.close()

print("Transfer Function G(s) = 1/((s+1)(s+2)(s+3))")
print("Open-Loop Poles:", control.poles(G))

# Bode Plot Examples
print_separator()
print("BODE PLOT EXAMPLES")
print_separator()

# First-Order System
print("1. First-Order System")
tau = 1.0
G = control.TransferFunction([1], [tau, 1])

mag, phase, omega = control.bode(G, plot=False)
plt.figure(figsize=(10, 10))
control.bode_plot(G, dB=True)
plt.suptitle('Bode Plot: First-Order System')
plt.savefig('docs/images/examples/bode_first_order.png')
plt.close()

print("Transfer Function G(s) = 1/(τs + 1)")
print(f"Time Constant (τ): {tau:.2f}")
print(f"Corner Frequency: {1/tau:.2f} rad/s")
print(f"Phase at Corner Frequency: {phase[np.argmin(np.abs(omega - 1/tau))]:.1f} degrees")

# Second-Order System
print_separator()
print("2. Second-Order System")
wn = 10.0
zeta = 0.5
num = [wn**2]
den = [1, 2*zeta*wn, wn**2]
G = control.TransferFunction(num, den)

mag, phase, omega = control.bode(G, plot=False)
plt.figure(figsize=(10, 10))
control.bode_plot(G, dB=True)
plt.suptitle('Bode Plot: Second-Order System')
plt.savefig('docs/images/examples/bode_second_order.png')
plt.close()

resonance_idx = np.argmax(mag)
print("Transfer Function G(s) = ωn²/(s² + 2ζωn·s + ωn²)")
print(f"Natural Frequency (ωn): {wn:.2f} rad/s")
print(f"Damping Ratio (ζ): {zeta:.2f}")
print(f"Resonance Peak: {mag[resonance_idx]:.2f} dB")
print(f"Resonance Frequency: {omega[resonance_idx]:.2f} rad/s")

# Band-Pass Filter
print_separator()
print("3. Band-Pass Filter")
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

gm, pm, wg, wp = control.margin(G)
print("Transfer Function G(s) = (w0/Q·s)/(s² + (w0/Q)s + w0²)")
print(f"Center Frequency (f0): {f0:.2f} Hz")
print(f"Quality Factor (Q): {Q:.2f}")
print(f"Gain Margin: {gm:.2f} dB at {wg:.2f} rad/s")
print(f"Phase Margin: {pm:.2f} degrees at {wp:.2f} rad/s")

print_separator()
print("All examples completed successfully!")
print_separator() 