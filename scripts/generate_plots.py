import control
import numpy as np
import matplotlib.pyplot as plt
import os

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

if __name__ == '__main__':
    print("Generating plots...")
    generate_single_step_response()
    print("✓ Generated step response plot")
    generate_multiple_step_responses()
    print("✓ Generated multiple step responses plot")
    print("Done! Plots have been saved to docs/images/") 