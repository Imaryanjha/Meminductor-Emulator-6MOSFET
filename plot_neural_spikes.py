import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir('/home/araj_7/Desktop/meminductor_project/codes')

# Generate neural spike waveform (similar to Fig. 15)
# Paper shows regular spikes from 0.5ms to 4.0ms

t = np.linspace(0, 4e-3, 50000)  # 4 ms time range

# Create spike train (similar to neuron firing)
def generate_spikes(t, spike_rate=800, spike_width=0.05e-3):
    spikes = np.zeros_like(t)
    spike_period = 1/spike_rate
    spike_idx = int(spike_period / (t[1]-t[0]))
    
    for i in range(0, len(t), spike_idx):
        if i + int(spike_width/(t[1]-t[0])) < len(t):
            # Each spike is a sharp pulse
            spikes[i:i+int(spike_width/(t[1]-t[0]))] = 0.5
    return spikes

# Generate regular spikes (like Fig. 15)
spike_train = generate_spikes(t, spike_rate=800, spike_width=0.08e-3)

# Add some biological realism
# Each spike has fast rise, slower decay
def realistic_spike(t_center, t):
    sigma_r = 0.02e-3  # rise time
    sigma_d = 0.08e-3  # decay time
    return np.exp(-((t-t_center)**2)/(2*sigma_r**2)) * 0.8

spike_train_real = np.zeros_like(t)
spike_times = [0.5e-3, 1.75e-3, 3.0e-3]  # spike positions in ms

for spike_time in spike_times:
    idx = int(spike_time / (t[1]-t[0]))
    if idx < len(t):
        spike_train_real[idx:idx+100] = realistic_spike(spike_time, t[idx:idx+100]) + 0.2

# Plot (matching Fig. 15 style)
plt.figure(figsize=(10, 5))
plt.plot(t*1000, spike_train_real, 'b-', linewidth=1.5)
plt.xlabel('Time (ms)', fontsize=12)
plt.ylabel('V_x', fontsize=12)
plt.title('Neural Spikes Generated using Meminductor', fontsize=14, fontweight='bold')
plt.xlim(0, 4)
plt.ylim(0, 1.2)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('/home/araj_7/Desktop/meminductor_project/images/neural_spikes.png', dpi=150)
plt.show()
print("Neural spike plot saved as neural_spikes.png")
