#!/bin/bash

# Create images folder for voltage sweep
mkdir -p /home/araj_7/Desktop/meminductor_project/images/voltage_sweep

# Different voltage amplitudes
voltages=(0.05 0.1 0.2 0.3 0.4 0.5)

for Vm in "${voltages[@]}"
do
    echo "Running simulation for Vm = ${Vm}V"
    
    # Create temporary netlist with new amplitude
    sed "s/SIN(0 0.1 10k)/SIN(0 ${Vm} 10k)/g" /home/araj_7/Desktop/meminductor_project/codes/meminductor_final.cir > temp.cir
    
    # Run simulation
    ngspice -b temp.cir > temp_output.txt
    
    # Extract data and plot using Python
    python3 /home/araj_7/Desktop/meminductor_project/codes/plot_voltage_sweep.py ${Vm}
    
    # Move image to voltage_sweep folder
    mv phl_${Vm}V.png /home/araj_7/Desktop/meminductor_project/images/voltage_sweep/
done

# Cleanup
rm temp.cir temp_output.txt

echo "All simulations complete. Images saved in images/voltage_sweep/"
