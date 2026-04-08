import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# Image files in order
files = [
    "phl_0.05V.png",
    "phl_0.1V.png",
    "phl_0.2V.png",
    "phl_0.3V.png",
    "phl_0.4V.png",
    "phl_0.5V.png"
]

# Create 2x3 grid
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

voltages = ["0.05 V", "0.1 V", "0.2 V", "0.3 V", "0.4 V", "0.5 V"]

for i, (ax, file, volt) in enumerate(zip(axes, files, voltages)):
    img = mpimg.imread(file)
    ax.imshow(img)
    ax.set_title(f"Vm = {volt}", fontsize=14, fontweight='bold')
    ax.axis('off')

plt.suptitle("Pinched Hysteresis Loops at Different Input Voltages (10 kHz)", fontsize=18, fontweight='bold')
plt.tight_layout()
plt.savefig("cumulative_collage.png", dpi=150)
plt.show()
print("Collage saved as cumulative_collage.png")
