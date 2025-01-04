import control
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.signal import lti, step, impulse

# Create the images directory if it doesn't exist
os.makedirs('docs/images', exist_ok=True)

# Set the default figure size
plt.rcParams['figure.figsize'] = [10, 8]
plt.style.use('seaborn-v0_8-darkgrid')

def generate_single_step_response():
    # Create a transfer function G(s) = (s + 2)/(s^2 + 2s + 1)
    s = control.TransferFunction.s
    G = control.TransferFunction([1, 2], [1, 2, 1])
    
    # Generate and plot step response
    t, y = control.step_response(G)
    plt.figure()
    plt.plot(t, y, linewidth=2)
    plt.grid(True)
    plt.title('Step Response')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    
    # Save the plot
    plt.savefig('docs/images/step_response.png', dpi=300, bbox_inches='tight')
    plt.close()

def generate_multiple_step_responses():
    # Create figure
    plt.figure()
    t = np.linspace(0, 5, 500)
    
    # Generate step responses for different systems
    for a in range(1, 6):
        # Create transfer function G(s) = a/(s + a)
        G = control.TransferFunction([a], [1, a])
        
        # Get and plot step response
        t, y = control.step_response(G, t)
        plt.plot(t, y, linewidth=2, label=f'a={a}')
    
    plt.grid(True)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Step Responses for Different Systems')
    plt.legend(loc='lower right')
    
    # Save the plot
    plt.savefig('docs/images/multiple_step_responses.png', dpi=300, bbox_inches='tight')
    plt.close()

def generate_root_locus():
    # Create transfer function G(s) = 1/((s+1)(s+2)(s+3))
    G = control.TransferFunction([1], [1, 6, 11, 6])
    
    # Generate root locus plot
    plt.figure()
    control.root_locus(G)
    plt.title('Root Locus Plot')
    
    # Save the plot
    plt.savefig('docs/images/root_locus.png', dpi=300, bbox_inches='tight')
    plt.close()

def generate_bandpass_bode():
    # Define parameters
    f0 = 100
    df = 10
    w0 = 2 * np.pi * f0
    fl = f0 - df
    fh = f0 + df
    Q = f0 / (fh - fl)
    
    # Create transfer function
    num = [w0**2 / Q]
    den = [1, w0/Q, w0**2]
    system = control.TransferFunction(num, den)
    
    # Generate Bode plot
    plt.figure(figsize=(8, 12))
    control.bode_plot(system, dB=True)
    
    # Save the plot
    plt.savefig('docs/images/bandpass_bode.png', dpi=300, bbox_inches='tight')
    plt.close()

def generate_system_responses():
    # Define transfer function G(s) = 1/(s+1)
    num = [1]
    den = [1, 1]
    system = lti(num, den)
    
    # Time vector
    t = np.linspace(0, 10, 500)
    
    # Get responses
    t_step, y_step = step(system, T=t)
    t_impulse, y_impulse = impulse(system, T=t)
    ramp_input = t
    _, y_ramp, _ = system.output(ramp_input, T=t)
    
    # Plot responses
    plt.figure(figsize=(10, 12))
    
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
    plt.savefig('docs/images/system_responses.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    print("Generating plots...")
    generate_single_step_response()
    print("✓ Generated step response plot")
    generate_multiple_step_responses()
    print("✓ Generated multiple step responses plot")
    generate_root_locus()
    print("✓ Generated root locus plot")
    generate_bandpass_bode()
    print("✓ Generated bandpass bode plot")
    generate_system_responses()
    print("✓ Generated system responses plot")
    print("Done! Plots have been saved to docs/images/") 