#====================================================================================
# SuperDARN Convection Map Downloader for May 2024 Storm
# Saves high-resolution PNGs for 5 key times
#====================================================================================

from pydarn.data import convection
import matplotlib.pyplot as plt
from datetime import datetime

# ------------------------
# 1. Define key times (UT) for the storm
# ------------------------
key_times = [
    datetime(2024, 5, 10, 12, 0),  # Pre-storm
    datetime(2024, 5, 10, 17, 0),  # Shock Arrival / Onset
    datetime(2024, 5, 10, 22, 0),  # Main Phase Peak
    datetime(2024, 5, 11, 2, 0),   # Early Recovery
    datetime(2024, 5, 11, 10, 0)   # Late Recovery
]

# ------------------------
# 2. Folder to save plots
# ------------------------
save_folder = "../Processed_Data/ConvectionMaps_May2024/"
import os
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# ------------------------
# 3. Loop through times, load and plot
# ------------------------
for dt in key_times:
    try:
        # Load SuperDARN convection map
        map_data = convection.load_map(dt)

        # Create figure
        fig, ax = plt.subplots(figsize=(8, 8))
        map_data.plot(ax=ax)

        # Add title
        ax.set_title(f"SuperDARN Convection Map\n{dt.strftime('%d %b %Y %H:%M UT')}")

        # Save as high-resolution PNG
        filename = f"{save_folder}ConvectionMap_{dt.strftime('%Y%m%d_%H%M')}UT.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Saved: {filename}")

        # Show plot (optional)
        # plt.show()
        plt.close(fig)  # Close to free memory

    except Exception as e:
        print(f"Error loading map for {dt}: {e}")
