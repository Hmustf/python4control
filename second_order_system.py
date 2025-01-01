import numpy as np
import matplotlib.pyplot as plt
from control import TransferFunction, step_response
import os

# Set style for modern, clean look
plt.style.use('bmh')
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 10,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'lines.linewidth': 2,
    'grid.linestyle': ':',
    'grid.alpha': 0.5,
})

def find_settling_band(t, y, steady_state, tolerance=0.02):
    """
    Find the settling band indices more accurately
    """
    error = np.abs(y - steady_state)
    settling_threshold = steady_state * tolerance
    
    # Find where response enters and stays within the band
    within_band = error <= settling_threshold
    
    # Use windowed check to ensure it stays within band
    window_size = 100
    for i in range(len(within_band) - window_size):
        if all(within_band[i:i+window_size]):
            return t[i], y[i]
    
    return None, None

def plot_elegant_response(sys, t_max=10, title="System Response", filename=None):
    """
    Create an elegant plot of system response with accurate settling time
    """
    # Generate time points with higher resolution
    t = np.linspace(0, t_max, 2000)
    
    # Get step response
    t, y = step_response(sys, t)
    
    # Calculate steady state value more accurately
    steady_state = y[-1]
    
    # Find settling point
    t_settling, y_settling = find_settling_band(t, y, steady_state)
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot step response
    ax.plot(t, y, 
            color='#1f77b4',  # Modern blue
            label='System Response',
            zorder=3)
    
    # Add reference line
    ax.plot([0, t_max], [steady_state, steady_state], 
            '--', 
            color='#d62728',  # Modern red
            alpha=0.7,
            label='Steady State',
            zorder=2)
    
    # Add settling boundaries
    ax.fill_between(t, 
                    steady_state * 0.98, 
                    steady_state * 1.02,
                    color='#2ca02c',  # Modern green
                    alpha=0.1,
                    label='±2% Settling Band',
                    zorder=1)
    
    # Mark settling point if found
    if t_settling is not None:
        ax.plot(t_settling, y_settling, 
                'o',
                color='#2ca02c',
                markersize=8,
                label=f'Settling Time: {t_settling:.2f}s')
    
    # Customize grid and spines
    ax.grid(True, alpha=0.3)
    for spine in ax.spines.values():
        spine.set_linewidth(0.5)
    
    # Customize labels
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Amplitude')
    ax.set_title(title, pad=20)
    
    # Add legend
    ax.legend(loc='best', 
             framealpha=0.9,
             fancybox=True)
    
    # Set axis limits with padding
    ax.set_xlim(-t_max*0.02, t_max*1.02)
    ymin, ymax = min(min(y), 0), max(max(y), steady_state*1.1)
    ax.set_ylim(ymin - 0.1*(ymax-ymin), ymax + 0.1*(ymax-ymin))
    
    # Adjust layout
    plt.tight_layout()
    
    # Save if filename provided
    if filename:
        os.makedirs('plots', exist_ok=True)
        plt.savefig(os.path.join('plots', filename), 
                   dpi=300,
                   bbox_inches='tight',
                   facecolor='white')
    
    plt.show()

def create_second_order_tf(wn, zeta):
    """
    Create a second order transfer function
    """
    num = [wn**2]
    den = [1, 2*zeta*wn, wn**2]
    return TransferFunction(num, den)

# Example usage
if __name__ == "__main__":
    # Create an interesting second-order system
    wn = 2.5
    zeta = 0.4
    sys = create_second_order_tf(wn, zeta)
    
    # Plot elegant response
    plot_elegant_response(
        sys,
        t_max=8,
        title=f"Step Response (ωn={wn}, ζ={zeta})",
        filename="elegant_response.png"
    )
    
    # Example of a more complex system
    # Transfer function: G(s) = 10(s + 2) / (s^2 + 2s + 10)
    num = [10, 20]
    den = [1, 2, 10]
    sys_complex = TransferFunction(num, den)
    
    plot_elegant_response(
        sys_complex,
        t_max=8,
        title="Step Response",
        filename="elegant_complex_response.png"
    ) 