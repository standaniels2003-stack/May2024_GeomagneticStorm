#====================================================================================
# SuperDARN Data Processing
#====================================================================================
import os
import shutil
from glob import glob
from PIL import Image
import matplotlib.pyplot as plt
#------------------------------------------------------------------------------------
# Paths
#------------------------------------------------------------------------------------
source_folder = "../Raw_Data_Files/SuperDARN_Data"
destination_folder = "../Processed_Data/SuperDARN"
#------------------------------------------------------------------------------------
# Create destination folder if it doesn't exist
#------------------------------------------------------------------------------------
os.makedirs(destination_folder, exist_ok=True)
#------------------------------------------------------------------------------------
# Define crop coordinates
#------------------------------------------------------------------------------------
left = 0
upper = 0
right = 850
lower = 750
#------------------------------------------------------------------------------------
# Process all PNG files in source folder
#------------------------------------------------------------------------------------
png_files = glob(os.path.join(source_folder, "*.png"))

for file_path in png_files:
    # Load image
    img = Image.open(file_path)
    
    # Crop image
    cropped_img = img.crop((left, upper, right, lower))
    
    # Get filename without folder
    filename = os.path.basename(file_path)
    
    # Save cropped image to destination folder
    save_path = os.path.join(destination_folder, filename)
    cropped_img.save(save_path)
    
    # Optional: display confirmation
    print(f"Cropped and saved: {filename}")

print("All SuperDARN PNG files processed successfully!")