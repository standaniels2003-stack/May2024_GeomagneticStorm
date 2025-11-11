#====================================================================================
# IMAGE Electrojet Indicators Processing and Plotting in Python
#====================================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#------------------------------------------------------------------------------------
# File paths for the two-day event
#------------------------------------------------------------------------------------
indicator_files = [
    "../Raw_Data_Files/IMAGE_Data/IMAGE_Data_202410.txt",
    "../Raw_Data_Files/IMAGE_Data/IMAGE_Data_202411.txt",
    "../Raw_Data_Files/IMAGE_Data/IMAGE_Data_202412.txt"
]

output_folder = "../Processed_Data/IMAGE_Data/"
os.makedirs(output_folder, exist_ok=True)

#------------------------------------------------------------------------------------
# Define expected columns
#------------------------------------------------------------------------------------
columns = ["Year","Month","Day","Hour","Min","Sec","IL","IU","IE",
           "la_IL","lo_IL","la_IU","lo_IU"]

#------------------------------------------------------------------------------------
# Read all files and concatenate
#------------------------------------------------------------------------------------
dfs = []
for f in indicator_files:
    df_temp = pd.read_csv(
        f,
        sep=r'\s+',         # handle multiple spaces
        names=columns,
        comment='#',
        skiprows=12,        # skip header
        engine='python',
        header=None
    )
    # Keep only the first 13 columns to avoid extra trailing data
    df_temp = df_temp.iloc[:, :len(columns)]
    dfs.append(df_temp)

df = pd.concat(dfs).sort_values(by=["Year","Month","Day","Hour","Min","Sec"]).reset_index(drop=True)

#------------------------------------------------------------------------------------
# Rename columns for pd.to_datetime
#------------------------------------------------------------------------------------
df.rename(columns={"Min":"minute","Sec":"second"}, inplace=True)

# Combine date/time into a datetime index
df['timestamp'] = pd.to_datetime(df[['Year','Month','Day','Hour','minute','second']])
df.set_index('timestamp', inplace=True)

#------------------------------------------------------------------------------------
# Convert numeric columns and handle missing/fill values
#------------------------------------------------------------------------------------
numeric_cols = ["IL","IU","IE","la_IL","lo_IL","la_IU","lo_IU"]
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
df.replace([-9999.99, 9999.99], np.nan, inplace=True)  # example fill values if present

#------------------------------------------------------------------------------------
# Save each numeric column as CSV
#------------------------------------------------------------------------------------
for col in numeric_cols:
    out_df = df[[col]].dropna().reset_index()
    out_df.to_csv(f"{output_folder}{col}.csv", index=False, encoding='utf-8')
    print(f"Saved CSV: {output_folder}{col}.csv")

#------------------------------------------------------------------------------------
# Plot each column and save as PNG
#------------------------------------------------------------------------------------
units_image = {
    'IL': r'AL index (nT)',
    'IU': r'AU index (nT)',
    'IE': r'IE index (nT)',
}

for col in ['IL', 'IU', 'IE']:
    plt.figure(figsize=(12, 3.5))
    plt.plot(df.index, df[col], color='#1f77b4', linewidth=1.2)
    plt.title(units_image[col], fontsize=14, pad=15)
    plt.xlabel('Time (UT) – 10–11 May 2024')
    plt.ylabel(units_image[col], fontsize=13)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_folder}{col}.png", dpi=300, bbox_inches='tight')
    plt.close()

print("Processing complete!")
