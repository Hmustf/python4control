import control
import numpy as np
import matplotlib.pyplot as plt

# Generate single step response plot
def generate_single_step_response():
    s = control.TransferFunction.s
    G = control.TransferFunction([1, 2], [1, 2, 1])
    
    t, y = control.step_response(G)
    plt.figure()
    plt.plot(t, y, linewidth=2)
    plt.grid(True)
    plt.title('Step Response')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.savefig('docs/images/step_response.png', bbox_inches='tight', dpi=300)
    plt.close()

# Generate multiple step responses plot
def generate_multiple_step_responses():
    plt.figure()
    t = np.linspace(0, 5, 500)
    
    for a in range(1, 6):
        G = control.TransferFunction([a], [1, a])
        t, y = control.step_response(G, t)
        plt.plot(t, y, linewidth=2, label=f'a={a}')
    
    plt.grid(True)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Step Responses for Different Systems')
    plt.legend(loc='lower right')
    plt.savefig('docs/images/multiple_step_responses.png', bbox_inches='tight', dpi=300)
    plt.close()

if __name__ == "__main__":
    generate_single_step_response()
    generate_multiple_step_responses()
    print("Plots generated successfully!") 