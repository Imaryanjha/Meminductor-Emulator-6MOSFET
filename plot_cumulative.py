import numpy as np
import matplotlib.pyplot as plt

# Data for different voltages (from your simulations)
# You can replace these with actual data from your simulations
voltages = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5]
colors = ['purple', 'blue', 'green', 'orange', 'red', 'brown']

plt.figure(figsize=(10, 8))

for i, Vm in enumerate(voltages):
    # Load data from your simulation results for each voltage
    # For now, creating sample data - REPLACE with actual data
    f = 10000  # 10 kHz
    w = 2 * np.pi * f
    t = np.linspace(0, 2/f, 5000)
    
    phi = -Vm/w * np.cos(w * t)
    # Sample current - replace with actual data
    current = Vm * 1e-9 * np.sin(w * t) * phi * 1e5
    
    plt.plot(phi * 1e6, current * 1e12, colors[i], linewidth=1.5, label=f'{Vm} V')

plt.xlabel('Flux φ (μWb)', fontsize=12)
plt.ylabel('Current I (pA)', fontsize=12)
plt.title('Pinched Hysteresis Loops at Different Voltages (10 kHz)', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.savefig('cumulative_phl.png', dpi=150)
plt.show()
print("Cumulative plot saved as cumulative_phl.png")
