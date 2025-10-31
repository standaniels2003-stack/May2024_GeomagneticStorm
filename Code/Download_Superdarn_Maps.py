#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Download / Plot SuperDARN Convection‑Map snapshots for 10‑11 May 2024 storm.
Save high‑resolution PNGs in a folder.
"""

import os
import matplotlib.pyplot as plt
import pydarn
from datetime import datetime

# ------------- CONFIG -------------
# Folder containing the local MAP files (you must have them downloaded).
map_folder = "../Raw_Data_Files/SuperDARN_Maps/"

# Key times (UTC) to snapshot. Adjust filenames/times if needed to match available files.
key_times = [
    datetime(2024, 5, 10, 12, 0),  # Pre‐storm
    datetime(2024, 5, 10, 17, 0),  # Shock Onset
    datetime(2024, 5, 10, 22, 0),  # Main Phase Peak
    datetime(2024, 5, 11, 2, 0),   # Early Recovery
    datetime(2024, 5, 11, 10, 0)   # Late Recovery
]

# Output folder for saved plots
save_folder = "../Processed_Data/ConvectionMaps_May2024"
os.makedirs(save_folder, exist_ok=True)

# ------------- FUNCTION to build filename -------------
def map_filename_for_time(dt):
    # Example naming convention: YYYYMMDD_HHMM.map or .map2
    return os.path.join(map_folder, dt.strftime("%Y%m%d_%H%M") + ".map2")

# ------------- MAIN LOOP -------------
for dt in key_times:
    try:
        fname = map_filename_for_time(dt)
        print(f"Loading map file: {fname}")
        reader = pydarn.SuperDARNRead(fname)
        map_data = reader.read_map()
        
        # Plotting – simple default
        fig, ax = plt.subplots(figsize=(8,8))
        pydarn.Maps.plot_mapdata(map_data,
                                 # Choose a parameter, e.g., fitted velocities or CPCP
                                 parameter=pydarn.MapParams.FITTED_VELOCITIES,
                                 lowlat=60,
                                 ax=ax,
                                 colorbar_label="Velocity (m/s)")
        ax.set_title(f"SuperDARN Convection Map – {dt.strftime('%d %b %Y %H:%M UT')}")
        
        # Save figure
        outname = os.path.join(save_folder, dt.strftime("%Y%m%d_%H%M") + "_Convection.png")
        plt.savefig(outname, dpi=300, bbox_inches='tight')
        plt.close(fig)
        print(f"Saved: {outname}")
        
    except Exception as e:
        print(f"Error processing time {dt}: {e}")
