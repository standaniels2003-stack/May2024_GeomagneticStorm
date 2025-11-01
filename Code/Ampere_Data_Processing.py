#====================================================================================
# Ampere Data Processing(It just coppies from the Raw Data to the Processed Data)
#====================================================================================
import os
import shutil
from glob import glob

#------------------------------------------------------------------------------------
# Paths
#------------------------------------------------------------------------------------
source_folder = "../Raw_Data_Files/Ampere_Data"  # where Ampere_Figure*.png are
destination_folder = "../Processed_Data/Ampere"

#------------------------------------------------------------------------------------
# Create destination folder if it doesn't exist
#------------------------------------------------------------------------------------
os.makedirs(destination_folder, exist_ok=True)

#------------------------------------------------------------------------------------
# Find all Ampere PNG files in the source folder
#------------------------------------------------------------------------------------
ampere_pngs = glob(os.path.join(source_folder, "Ampere_*.png"))

#------------------------------------------------------------------------------------
# Copy each file
#------------------------------------------------------------------------------------
for filename in os.listdir(source_folder):
    # Only copy PNG files that start with "Ampere_"
    if filename.startswith("Ampere_") and filename.endswith(".png"):
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(destination_folder, filename)
        shutil.copy2(src_path, dst_path)  # copy2 preserves metadata
        print(f"Copied {filename} to {destination_folder}")

print("All Ampere PNGs copied successfully.")
