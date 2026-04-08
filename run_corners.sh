#!/bin/bash

mkdir -p /home/araj_7/Desktop/meminductor_project/images/corner_analysis

corners=("tt" "ff" "ss" "fs" "sf")
corner_names=("Typical_TT" "Fast_Fast_FF" "Slow_Slow_SS" "Fast_Slow_FS" "Slow_Fast_SF")

for i in "${!corners[@]}"; do
    corner=${corners[$i]}
    name=${corner_names[$i]}
    
    echo "Running corner: $name"
    
    # Use appropriate model file
    if [ "$corner" == "tt" ]; then
        cp /home/araj_7/Desktop/meminductor_project/codes/models.mod /home/araj_7/Desktop/meminductor_project/codes/models_current.mod
    else
        cp /home/araj_7/Desktop/meminductor_project/codes/models_${corner}.mod /home/araj_7/Desktop/meminductor_project/codes/models_current.mod
    fi
    
    # Run simulation
    ngspice -b /home/araj_7/Desktop/meminductor_project/codes/meminductor_corner.cir > corner_${corner}.txt
    
    echo "Completed corner: $name"
done

echo "All corners completed"
