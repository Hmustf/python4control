# Control System Design - Week 1

## Root Locus Plot

An example transfer function is given:

\[
G(s) = \frac{1}{(s+1)(s+2)(s+3)}
\]

Using symbolic calculations:

```python
from sympy import symbols, solve, simplify
import matplotlib.pyplot as plt
import numpy as np

# Define the symbolic variables
s, k = symbols('s k')

# Define the transfer function
Gs = 1 / ((s + 1) * (s + 2) * (s + 3))

# Closed-loop transfer function
Ts = k * Gs / (1 + k * Gs)

# Numerator and denominator
numerator, denominator = simplify(Ts).as_numer_denom()

# Plot the root locus
real_parts = []
imag_parts = []

k_values = np.linspace(0, 20, 100)

for kv in k_values:
    d_subs = denominator.subs(k, kv)
    poles = solve(d_subs, s)
    for pole in poles:
        real_parts.append(pole.as_real_imag()[0])
        imag_parts.append(pole.as_real_imag()[1])

plt.figure(figsize=(8, 6))
plt.scatter(real_parts, imag_parts, color='blue', label='Poles')
plt.axhline(0, color='black', linestyle='--')
plt.axvline(0, color='black', linestyle='--')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.title('Root Locus Plot')
plt.legend()
plt.grid()
plt.show()
```

<p align="center">
<img src="../images/root_locus.png" width="60%">
</p>

## Bode Plot for a Band-Pass Filter

Given the band-pass filter:

\[
G(s) = \frac{1}{Q w_0^2} \frac{1}{s^2 + \frac{w_0}{Q} s + w_0^2}
\]

Using Python:

```python
from sympy import I, pi, lambdify

# Define parameters
df = 10
f0 = 100
w0 = 2 * pi * f0
fl = f0 - df
fh = f0 + df
Q = f0 / (fh - fl)

# Define the transfer function
Gs = (1 / Q) * w0**2 / (s**2 + (w0 / Q) * s + w0**2)

# Substitute s with jw
w = symbols('w')
Gjw = Gs.subs(s, I * w)

# Create frequency values
w_values = np.linspace(0, 1000, 1000)
Gjw_func = lambdify(w, Gjw, 'numpy')

# Calculate gain and phase
gain = np.abs(Gjw_func(w_values))
phase = np.angle(Gjw_func(w_values), deg=True)

# Plot Bode Plot
plt.figure(figsize=(8, 12))

plt.subplot(2, 1, 1)
plt.plot(w_values / (2 * np.pi), 20 * np.log10(gain), label='Gain')
plt.xscale('log')
plt.grid(True, which="both", linestyle='--')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.title('Bode Plot - Gain')

plt.subplot(2, 1, 2)
plt.plot(w_values / (2 * np.pi), phase, label='Phase', color='orange')
plt.xscale('log')
plt.grid(True, which="both", linestyle='--')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (degrees)')
plt.title('Bode Plot - Phase')

plt.tight_layout()
plt.show()
```

<p align="center">
<img src="../images/bandpass_bode.png" width="60%">
</p>

## Impulse, Step, and Ramp Responses

For a given transfer function:

\[
G(s) = \frac{1}{s+1}
\]

Calculate the impulse, step, and ramp responses:

```python
from scipy.signal import lti, step, impulse

# Define transfer function numerator and denominator
num = [1]
den = [1, 1]

# Define LTI system
system = lti(num, den)

# Time vector
t = np.linspace(0, 10, 500)

# Step response
t_step, y_step = step(system, T=t)

# Impulse response
t_impulse, y_impulse = impulse(system, T=t)

# Ramp response
ramp_input = t
_, y_ramp, _ = lti(num, den).output(ramp_input, T=t)

# Plot responses
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(t_impulse, y_impulse, label='Impulse Response')
plt.grid(True)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Impulse Response')

plt.subplot(3, 1, 2)
plt.plot(t_step, y_step, label='Step Response', color='green')
plt.grid(True)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Step Response')

plt.subplot(3, 1, 3)
plt.plot(t, y_ramp, label='Ramp Response', color='red')
plt.grid(True)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Ramp Response')

plt.tight_layout()
plt.show()
```

<p align="center">
<img src="../images/system_responses.png" width="60%">
</p>
