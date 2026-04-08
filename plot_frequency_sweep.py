import numpy as np
import matplotlib.pyplot as plt
import sys

freq_value = float(sys.argv[1])
freq_label = sys.argv[2]

# Read the output file
with open('temp_freq_output.txt', 'r') as file:
    lines = file.readlines()

# Find data section
data_start = 0
for i, line in enumerate(lines):
    if 'Index' in line and 'time' in line:
        data_start = i + 2
        break

# Parse data
data = []
for line in lines[data_start:]:
    if line.strip() and not line.startswith('----') and 'Index' not in line:
        try:
            values = line.strip().split()
            if len(values) >= 5:
                data.append([
                    float(values[1]),  # time
                    float(values[2]),  # v(vin_sense)
                    float(values[3])   # current
                ])
        except:
            pass

if data:
    data = np.array(data)
    time = data[:, 0]
    v_in = data[:, 1]
    i_in = data[:, 2]
    
    # Calculate flux
    dt = time[1] - time[0]
    flux = np.cumsum(v_in) * dt
    
    # Scale
    flux_uwb = flux * 1e6
    current_pa = i_in * 1e12
    
    # Plot
    plt.figure(figsize=(8, 6))
    plt.plot(flux_uwb, current_pa, 'b-', linewidth=1.5)
    plt.xlabel('Flux φ (μWb)', fontsize=12)
    plt.ylabel('Current I (pA)', fontsize=12)
    plt.title(f'Pinched Hysteresis Loop @ {freq_label}', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.tight_layout()
    plt.savefig(f'phl_{int(freq_value)}Hz.png', dpi=150)
    plt.close()
    print(f"Plot saved for frequency = {freq_label}")
