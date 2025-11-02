#====================================================================================
# OMNI Data Processing and Plotting in Python
#====================================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
#------------------------------------------------------------------------------------
# Load CSV
#------------------------------------------------------------------------------------
df = pd.read_csv(
    "../Raw_Data_Files/OMNI_HRO2_1MIN.csv",
    skiprows=93,
    skipfooter=3,
    engine='python'
)

#------------------------------------------------------------------------------------
# Clean column names
#------------------------------------------------------------------------------------
df.columns = df.columns.str.strip()
df.rename(columns={
    'EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ': 'timestamp',
    'BX__GSE_nT': 'Bx',
    'BY__GSE_nT': 'By',
    'BZ__GSE_nT': 'Bz',
    'FLOW_SPEED__GSE_km/s': 'flow_speed',
    'PROTON_DENSITY_n/cc': 'proton_density',
    'FLOW_PRESSURE_nPa': 'flow_pressure',
    '1-M_AE_nT': 'one_minus_M_AE',
    'SYM/H_INDEX_nT': 'SYM_H_index'
}, inplace=True)

#------------------------------------------------------------------------------------
# Convert timestamp
#------------------------------------------------------------------------------------
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

#------------------------------------------------------------------------------------
# Convert numeric columns & handle fill values
#------------------------------------------------------------------------------------
numeric_cols = ['Bx', 'By', 'Bz', 'flow_speed', 'proton_density', 
                'flow_pressure', 'one_minus_M_AE', 'SYM_H_index']

df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
fill_values = [9999.99, 99999.9, 999.990, 99.9900, -999.9]
df.replace(fill_values, np.nan, inplace=True)

#------------------------------------------------------------------------------------
# Compute B-field magnitude
#------------------------------------------------------------------------------------
df['B_magnitude'] = np.sqrt(df['Bx']**2 + df['By']**2 + df['Bz']**2)

#------------------------------------------------------------------------------------
# Set timestamp as index
#------------------------------------------------------------------------------------
df.set_index('timestamp', inplace=True)

#------------------------------------------------------------------------------------
# Save CSVs (optional)
#------------------------------------------------------------------------------------
output_folder = "../Processed_Data/OMNI_Data/"
os.makedirs(output_folder, exist_ok=True)

columns_to_plot = numeric_cols + ['B_magnitude']

for col in columns_to_plot:
    out_df = df[[col]].dropna().reset_index()
    out_df.to_csv(f"{output_folder}{col}.csv", index=False, encoding='utf-8')
    print(f"Saved CSV: {output_folder}{col}.csv")

#------------------------------------------------------------------------------------
# Plot each column and save as PNG
#------------------------------------------------------------------------------------
for col in columns_to_plot:
    plt.figure(figsize=(12, 4))
    plt.plot(df.index, df[col], color='tab:blue')
    plt.title(col)
    plt.xlabel('Time')
    plt.ylabel(col)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_folder}{col}.png", dpi=300)
    plt.close()
    print(f"Saved PNG: {output_folder}{col}.png")
