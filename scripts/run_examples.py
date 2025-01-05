import control
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns

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

# Set the style to a modern, clean theme
plt.style.use('seaborn-v0_8')
sns.set_style("whitegrid", {'grid.linestyle': ':'})
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']

# Define system parameters
NATURAL_FREQUENCY = 1.0  # Natural frequency (wn)
DAMPING_RATIO = 0.5      # Damping ratio (zeta)

# Create a second-order transfer function
numerator = [NATURAL_FREQUENCY**2]
denominator = [1, 2 * DAMPING_RATIO * NATURAL_FREQUENCY, NATURAL_FREQUENCY**2]
G2 = control.TransferFunction(numerator, denominator)

# Get step response
t, y = control.step_response(G2)

# Get step response characteristics
info = control.step_info(G2)

# Extract key values
rise_time = info['RiseTime']
peak_time = info['PeakTime']
peak_value = info['Peak']
settling_time = info['SettlingTime']
overshoot = info['Overshoot']

# Function to find the nearest index in the time array
def find_nearest(array, value):
    idx = (np.abs(array - value)).argmin()
    return idx

# Create figure with a specific background color
plt.figure(figsize=(14, 8))
ax = plt.gca()
ax.set_facecolor('#ffffff')
plt.gcf().set_facecolor('#ffffff')

# Custom color palette
main_color = '#2E86AB'  # Blue
steady_state_color = '#D64933'  # Red
annotation_color = '#1B1B1E'  # Dark gray
grid_color = '#E5E5E5'  # Light gray
overshoot_color = '#FF6B6B'  # Coral for overshoot arrow
settling_color = '#6C757D'  # Gray for settling bounds

# Plot step response curve with gradient
line, = plt.plot(t, y, label='Step Response', linewidth=3, color=main_color)

# Plot steady-state line
plt.axhline(y=1, color=steady_state_color, linestyle='--', label='Steady-State Value', linewidth=2, alpha=0.8)

# Add ±2% settling time bounds
plt.axhline(y=1.02, color=settling_color, linestyle=':', label='±2% Bounds', linewidth=1.5, alpha=0.6)
plt.axhline(y=0.98, color=settling_color, linestyle=':', linewidth=1.5, alpha=0.6)

# Create shaded regions for better visualization
plt.fill_between(t, y, 1, where=(y > 1), color=main_color, alpha=0.15, interpolate=True, label='Error')
plt.fill_between(t, y, 1, where=(y < 1), color=main_color, alpha=0.1, interpolate=True)

# Plot vertical lines with gradient alpha
for time, label in [(rise_time, 'Rise Time'), (peak_time, 'Peak Time'), (settling_time, 'Settling Time')]:
    plt.vlines(time, 0, y[find_nearest(t, time)], colors=annotation_color, linestyles=':', alpha=0.3)

# Create fancy boxes for annotations with improved styling
def create_annotation_box(text):
    return dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.95, 
               edgecolor=annotation_color, linewidth=1)

# Add overshoot double-headed arrow
plt.annotate('', xy=(peak_time, peak_value), 
            xytext=(peak_time, 1),
            arrowprops=dict(arrowstyle='<->', color=overshoot_color, 
                          linewidth=2, shrinkA=0, shrinkB=0))

# Add overshoot label centered on the double-headed arrow
plt.annotate(f'Overshoot\n{overshoot:.1f}%', 
            xy=(peak_time, (peak_value + 1)/2),  # Middle point of the arrow
            xytext=(peak_time, (peak_value + 1)/2),  # Exactly on the arrow
            fontsize=9,
            color=annotation_color,
            bbox=create_annotation_box(''),
            ha='center',  # Center horizontally
            va='center')  # Center vertically

plt.annotate(f'Rise Time\n{rise_time:.2f} s', 
             xy=(rise_time, y[find_nearest(t, rise_time)]),
             xytext=(rise_time + 1, y[find_nearest(t, rise_time)] - 0.2),
             fontsize=11,
             color=annotation_color,
             bbox=create_annotation_box(''),
             arrowprops=dict(arrowstyle='fancy', color=annotation_color, alpha=0.6),
             ha='center')

plt.annotate(f'Peak Time\n{peak_time:.2f} s', 
             xy=(peak_time, peak_value),
             xytext=(peak_time + 0.5, peak_value + 0.1),
             fontsize=11,
             color=annotation_color,
             bbox=create_annotation_box(''),
             arrowprops=dict(arrowstyle='fancy', color=annotation_color, alpha=0.6),
             ha='center')

# Add settling time annotation with bounds info
plt.annotate(f'Settling Time\n{settling_time:.2f} s\n±2% Bounds', 
             xy=(settling_time, 1),
             xytext=(settling_time + 1.5, 1.1),  # Changed y position from 0.7 to 0.8
             fontsize=11,
             color=annotation_color,
             bbox=create_annotation_box(''),
             arrowprops=dict(arrowstyle='fancy', color=annotation_color, alpha=0.6),
             ha='center')

# Add system parameters annotation
plt.text(0.02, 0.98, f'System Parameters:\nωn = {NATURAL_FREQUENCY} rad/s\nζ = {DAMPING_RATIO}',
         transform=ax.transAxes,
         bbox=dict(facecolor='white', alpha=0.95, edgecolor=annotation_color, 
                  boxstyle='round,pad=0.5', linewidth=1),
         fontsize=11,
         color=annotation_color,
         verticalalignment='top')

# Enhance grid with custom styling
ax.grid(True, which='major', color=grid_color, linewidth=1.2, alpha=0.8)
ax.grid(True, which='minor', color=grid_color, linewidth=0.8, alpha=0.5)

# Set axis limits with padding to ensure annotations are visible
plt.xlim(-0.2, max(t) + 0.5)
plt.ylim(-0.1, max(y) + 0.3)

# Title and labels with enhanced styling
plt.title('Second-Order System Step Response', fontsize=16, pad=20, 
          color=annotation_color, fontweight='bold')
plt.xlabel('Time (s)', fontsize=12, labelpad=10, color=annotation_color)
plt.ylabel('Amplitude', fontsize=12, labelpad=10, color=annotation_color)

# Customize ticks
plt.xticks(fontsize=10, color=annotation_color)
plt.yticks(fontsize=10, color=annotation_color)

# Enhanced legend with new styling
plt.legend(loc='upper right', fontsize=11, fancybox=True, 
          framealpha=0.95, edgecolor=annotation_color)

# Adjust layout and save with high DPI
plt.tight_layout()
plt.savefig('docs/images/examples/second_order_response.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.close()

print("Transfer Function G(s) = ωn²/(s² + 2ζωn·s + ωn²)")
print(f"Natural Frequency (ωn): {NATURAL_FREQUENCY:.2f} rad/s")
print(f"Damping Ratio (ζ): {DAMPING_RATIO:.2f}")
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