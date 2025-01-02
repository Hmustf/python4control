import control
import numpy as np
import matplotlib.pyplot as plt

def basic_control_example():
    """Basic transfer function and step response example."""
    # Create transfer function: G(s) = 1/(s^2 + 2s + 1)
    num = [1]
    den = [1, 2, 1]
    G = control.TransferFunction(num, den)
    print("Transfer function G(s):")
    print(G)

    # Plot step response
    plt.figure(figsize=(10, 6))
    t = np.linspace(0, 10, 1000)
    t, y = control.step_response(G, t)
    plt.plot(t, y)
    plt.grid(True)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title('Step Response of Second-Order System')
    plt.savefig('plots/basic_response.png')
    plt.close()

def compare_first_order_systems():
    """Compare different first-order systems."""
    plt.figure(figsize=(10, 6))
    t = np.linspace(0, 5, 1000)

    # Compare different time constants
    for a in range(1, 6):
        # Create transfer function G(s) = a/(s + a)
        G = control.TransferFunction([a], [1, a])
        
        # Get step response
        t, y = control.step_response(G, t)
        
        # Plot with label
        plt.plot(t, y, linewidth=2, label=f'a = {a}')

    plt.grid(True)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title('Step Responses of First-Order Systems')
    plt.legend()
    plt.savefig('plots/first_order_comparison.png')
    plt.close()

if __name__ == "__main__":
    # Create plots directory if it doesn't exist
    import os
    os.makedirs('plots', exist_ok=True)
    
    print("Running control system examples...")
    basic_control_example()
    compare_first_order_systems()
    print("Examples completed. Check the 'plots' directory for results.") 