#====================================================================================
# This File is used for the reading and prosessing of the OMNI_HRO2_1MIN Data File
#====================================================================================
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -----------------------
# 1. Load CSV
# -----------------------
df = pd.read_csv(
    "../Raw_Data_Files/OMNI_HRO2_1MIN.csv",
    skiprows=93,      # Skip header lines if needed
    skipfooter=3,     # Skip footer lines if needed
    engine='python'   # Required for skipfooter
)

# -----------------------
# 2. Clean column names
# -----------------------
df.columns = df.columns.str.strip()  # remove extra spaces

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

# Verify renaming
print("Columns after rename:", df.columns.tolist())

# -----------------------
# 3. Convert timestamp
# -----------------------
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

# -----------------------
# 4. Convert numeric columns & handle fill values
# -----------------------
numeric_cols = ['Bx', 'By', 'Bz', 'flow_speed', 'proton_density', 
                'flow_pressure', 'one_minus_M_AE', 'SYM_H_index']

# Convert to numeric (any non-numeric becomes NaN)
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Replace common OMNI fill values with NaN
fill_values = [9999.99, 99999.9, 999.990, 99.9900, -999.9]
df.replace(fill_values, np.nan, inplace=True)

# -----------------------
# 5. Compute B-field magnitude
# -----------------------
df['B_magnitude'] = np.sqrt(df['Bx']**2 + df['By']**2 + df['Bz']**2)

# -----------------------
# 6. Set timestamp as index
# -----------------------
df.set_index('timestamp', inplace=True)

# -----------------------
# 7. Save each column as its own CSV for LaTeX plotting
# -----------------------
output_folder = "../Processed_Data/OMNI_Data/"

import os
os.makedirs(output_folder, exist_ok=True)

columns_to_plot = numeric_cols + ['B_magnitude']

for col in columns_to_plot:
    out_df = df[[col]].dropna()  # keep timestamp + one variable
    out_df.to_csv(f"{output_folder}{col}.csv", index=True)
    print(f"Saved: {output_folder}{col}.csv")


# -----------------------
# 8. Plot all numeric columns
# -----------------------
columns_to_plot = numeric_cols + ['B_magnitude']

fig, axes = plt.subplots(len(columns_to_plot), 1, figsize=(14, 3*len(columns_to_plot)), sharex=True)

for i, col in enumerate(columns_to_plot):
    axes[i].plot(df.index, df[col])
    axes[i].set_ylabel(col)
    axes[i].grid(True)

axes[-1].set_xlabel('Time')
plt.tight_layout()
plt.show()