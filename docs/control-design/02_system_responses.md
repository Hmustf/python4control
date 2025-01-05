# System Responses in Control Systems

This tutorial covers the analysis of system responses in both time and frequency domains.

## Time Domain Responses

### Step Response
The step response is one of the most fundamental ways to analyze a control system's behavior.

```python
import control
import numpy as np
import matplotlib.pyplot as plt

# Create a transfer function G(s) = 1/(s + 1)
G = control.TransferFunction([1], [1, 1])

# Generate step response
t, y = control.step_response(G)

plt.figure()
plt.plot(t, y)
plt.grid(True)
plt.title('Step Response')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()
```

Output:
```
Step Response Output:
Final Value: 1.00
Rise Time: 2.30 seconds
```

![Step Response](../images/examples/step_response.png)

### Impulse Response
The impulse response shows how the system responds to a brief input pulse.

```python
# Generate impulse response
t, y = control.impulse_response(G)

plt.figure()
plt.plot(t, y)
plt.grid(True)
plt.title('Impulse Response')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()
```

Output:
```
Impulse Response Output:
Peak Value: 1.00
```

![Impulse Response](../images/examples/impulse_response.png)

### Ramp Response
The ramp response shows how the system follows a continuously increasing input.

```python
# Create time vector
t = np.linspace(0, 10, 1000)

# Create ramp input
u = t

# Simulate system response to ramp input
t, y, _ = control.forced_response(G, t, u)

plt.figure()
plt.plot(t, u, '--', label='Input')
plt.plot(t, y, label='Output')
plt.grid(True)
plt.title('Ramp Response')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
```

## Response Characteristics

### Rise Time
The time required for the system output to rise from 10% to 90% of its final value.
- In our example: 2.30 seconds

### Settling Time
The time required for the system to settle within ±2% of its final value.
- For our first-order system: approximately 4 time constants (4τ)

### Overshoot
The maximum peak value of the response curve measured from the desired response of the system.
- Our first-order system has no overshoot

### Steady-State Error
The difference between the desired output and the actual output as time approaches infinity.
- In our step response example: 0 (Final value = 1.00)

## Example: Analyzing System Characteristics

```python
# Create a second-order system
wn = 1.0  # Natural frequency
zeta = 0.5  # Damping ratio
G = control.TransferFunction([wn**2], [1, 2*zeta*wn, wn**2])

# Get step response
t, y = control.step_response(G)

# Plot response with characteristics
plt.figure()
plt.plot(t, y)
plt.grid(True)
plt.title('Second-Order System Step Response')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Add annotations for characteristics
info = control.step_info(G)
plt.annotate(f'Rise Time: {info["RiseTime"]:.2f}s', xy=(info["RiseTime"], 0.5))
plt.annotate(f'Peak Time: {info["PeakTime"]:.2f}s', xy=(info["PeakTime"], info["Peak"]))
plt.annotate(f'Overshoot: {info["Overshoot"]:.1f}%', xy=(info["PeakTime"], info["Peak"]))
plt.annotate(f'Settling Time: {info["SettlingTime"]:.2f}s', xy=(info["SettlingTime"], 1))

plt.show()
```

## Exercises

1. Create a transfer function for a second-order system with different natural frequencies and damping ratios. Compare their step responses.
2. Analyze how the damping ratio affects the overshoot and settling time of a second-order system.
3. Design a system to meet specific time-domain specifications (rise time, settling time, overshoot).
