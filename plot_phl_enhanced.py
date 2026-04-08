import numpy as np
import matplotlib.pyplot as plt

with open('mem_final.txt', 'r') as f:
    lines = f.readlines()

data_start = 0
for i, line in enumerate(lines):
    if 'Index' in line and 'time' in line:
        data_start = i + 2
        break

data = []
for line in lines[data_start:]:
    if line.strip() and not line.startswith('----') and 'Index' not in line:
        try:
            values = line.strip().split()
            if len(values) >= 5:
                data.append([
                    float(values[1]),
                    float(values[2]),
                    float(values[3]),
                ])
        except:
            pass

data = np.array(data)
time = data[:, 0]
v_in = data[:, 1]
i_in = data[:, 2]

dt = time[1] - time[0]
flux = np.cumsum(v_in) * dt

flux_uwb = flux * 1e6
current_pa = i_in * 1e12

print(f"Flux range: {flux_uwb.min():.4f} to {flux_uwb.max():.4f} μWb")
print(f"Current range: {current_pa.min():.4f} to {current_pa.max():.4f} pA")

plt.figure(figsize=(8, 6))
plt.plot(flux_uwb, current_pa, 'b-', linewidth=1.5)
plt.xlabel('Flux φ (μWb)', fontsize=12)
plt.ylabel('Current I (pA)', fontsize=12)
plt.title('Pinched Hysteresis Loop @ 10 kHz', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.tight_layout()
plt.savefig('phl_10khz_pa.png', dpi=150)
plt.show()
print("Plot saved as phl_10khz_pa.png")
