import numpy as np
import matplotlib.pyplot as plt
import subprocess
import os
import re

os.chdir('/home/araj_7/Desktop/meminductor_project/codes')

num_runs = 30  # Number of Monte Carlo runs
all_flux = []
all_current = []

for run in range(num_runs):
    print(f"Run {run+1}/{num_runs}")
    
    # Generate random variations (5% standard deviation)
    w_var = 1e-6 * (1 + np.random.normal(0, 0.05))
    l_var = 0.18e-6 * (1 + np.random.normal(0, 0.05))
    
    # Read base netlist
    with open('meminductor_mc_simple.cir', 'r') as f:
        netlist = f.read()
    
    # Replace W and L values with variations
    netlist = re.sub(r'w=1u', f'w={w_var:.4e}', netlist)
    netlist = re.sub(r'l=0.18u', f'l={l_var:.4e}', netlist)
    
    # Save modified netlist
    with open(f'temp_mc_{run}.cir', 'w') as f:
        f.write(netlist)
    
    # Run simulation
    result = subprocess.run(f'ngspice -b temp_mc_{run}.cir > mc_out_{run}.txt', 
                           shell=True, capture_output=True, text=True)
    
    # Parse output
    try:
        with open(f'mc_out_{run}.txt', 'r') as f:
            lines = f.readlines()
        
        data_start = 0
        for i, line in enumerate(lines):
            if 'Index' in line and 'time' in line:
                data_start = i + 2
                break
        
        data = []
        for line in lines[data_start:]:
            if line.strip() and not line.startswith('----'):
                try:
                    vals = line.strip().split()
                    if len(vals) >= 4:
                        data.append([float(vals[1]), float(vals[2]), float(vals[3])])
                except:
                    pass
        
        if len(data) > 100:
            data = np.array(data)
            time = data[:, 0]
            v_in = data[:, 1]
            i_in = data[:, 2]
            
            dt = time[1] - time[0]
            flux = np.cumsum(v_in) * dt
            
            flux_uwb = flux * 1e6
            current_pa = i_in * 1e12
            
            all_flux.append(flux_uwb)
            all_current.append(current_pa)
            print(f"  ✓ Success")
    except Exception as e:
        print(f"  ✗ Failed: {e}")
    
    # Cleanup
    os.remove(f'temp_mc_{run}.cir')
    os.remove(f'mc_out_{run}.txt')

# Plot results
plt.figure(figsize=(10, 8))

for i in range(len(all_flux)):
    plt.plot(all_flux[i], all_current[i], 'b-', alpha=0.3, linewidth=0.8)

plt.xlabel('Flux φ (μWb)', fontsize=12)
plt.ylabel('Current I (pA)', fontsize=12)
plt.title(f'Monte Carlo Analysis: {len(all_flux)} Runs with 5% W/L Variation', 
          fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.tight_layout()
plt.savefig('/home/araj_7/Desktop/meminductor_project/images/monte_carlo_simple.png', dpi=150)
plt.show()

print(f"\n✅ Monte Carlo complete! {len(all_flux)} successful runs")
print("Plot saved as monte_carlo_simple.png")
