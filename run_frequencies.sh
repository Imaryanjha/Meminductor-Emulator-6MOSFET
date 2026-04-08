#!/bin/bash

# Create folder for frequency sweep images
mkdir -p /home/araj_7/Desktop/meminductor_project/images/frequency_sweep

# Different frequencies (in Hz)
frequencies=(10000 50000 100000 200000 500000 1000000 2000000 5000000 10000000)

for f in "${frequencies[@]}"
do
    # Convert to kHz for display
    if [ $f -lt 1000 ]; then
        freq_khz="${f} Hz"
    else
        freq_khz="$((f/1000)) kHz"
    fi
    
    echo "Running simulation for frequency = ${freq_khz}"
    
    # Create temporary netlist with new frequency
    sed "s/SIN(0 0.1 10k)/SIN(0 0.1 ${f})/g" /home/araj_7/Desktop/meminductor_project/codes/meminductor_final.cir > temp_freq.cir
    
    # Run simulation
    ngspice -b temp_freq.cir > temp_freq_output.txt
    
    # Plot using Python
    python3 /home/araj_7/Desktop/meminductor_project/codes/plot_frequency_sweep.py ${f} "${freq_khz}"
    
    # Move image to frequency_sweep folder
    mv phl_${f}Hz.png /home/araj_7/Desktop/meminductor_project/images/frequency_sweep/ 2>/dev/null
done

# Cleanup
rm -f temp_freq.cir temp_freq_output.txt

echo "All frequency simulations complete. Images saved in images/frequency_sweep/"
