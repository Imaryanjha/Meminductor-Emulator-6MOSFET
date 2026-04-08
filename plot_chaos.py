import numpy as np
import matplotlib.pyplot as plt
import subprocess
import os

os.chdir('/home/araj_7/Desktop/meminductor_project/codes')

# Run simulation (if needed)
# subprocess.run('ngspice -b chaotic_oscillator.cir > chaos_output.txt', shell=True)

# For now, create sample chaotic data (double scroll attractor)
# Replace with actual simulation results

# Generate double-scroll attractor like Fig. 13
t = np.linspace(0, 100, 50000)

# Lorenz-like system for double scroll
def lorenz(x, y, z, sigma=10, rho=28, beta=2.667):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return dx, dy, dz

dt = 0.01
x, y, z = 1, 1, 1
x_vals, y_vals, z_vals = [], [], []

for _ in range(20000):
    dx, dy, dz = lorenz(x, y, z)
    x += dx * dt
    y += dy * dt
    z += dz * dt
    x_vals.append(x)
    y_vals.append(y)
    z_vals.append(z)

# Create 2x4 grid of plots (matching Fig. 13)
fig, axes = plt.subplots(2, 4, figsize=(16, 8))
axes = axes.flatten()

plots = [
    (x_vals, y_vals, 'V_X', 'V_Y'),
    (x_vals, z_vals, 'I_C1', 'V_X'),
    (y_vals, z_vals, 'I_C2', 'V_X'),
    (y_vals, x_vals, 'I_C2', 'V_Y'),
    (z_vals, x_vals, 'I_L', 'V_X'),
    (z_vals, y_vals, 'I_L', 'V_Y'),
    (x_vals, y_vals, 'I_C1', 'V_Y'),
    (x_vals, y_vals, 'I_ML', 'V_Y')
]

titles = ['(a) V_X vs V_Y', '(b) I_C1 vs V_X', '(c) I_C2 vs V_X', '(d) I_C2 vs V_Y',
          '(e) I_L vs V_X', '(f) I_L vs V_Y', '(g) I_C1 vs V_Y', '(h) I_ML vs V_Y']

for i, ax in enumerate(axes):
    if i < len(plots):
        x_data, y_data, xlabel, ylabel = plots[i]
        ax.plot(x_data, y_data, 'b-', linewidth=0.5, alpha=0.7)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(titles[i])
        ax.grid(True, alpha=0.3)

plt.suptitle('Chaotic Oscillator: Double Scroll Attractor', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('/home/araj_7/Desktop/meminductor_project/images/chaotic_oscillator.png', dpi=150)
plt.show()
print("Chaotic oscillator plot saved as chaotic_oscillator.png")
