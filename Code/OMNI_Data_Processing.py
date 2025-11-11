#====================================================================================
# OMNI Data Processing and Plotting – FINAL VERSION WITH PROPER UNITS (2025)
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
# Convert timestamp + numeric columns
#------------------------------------------------------------------------------------
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
numeric_cols = ['Bx', 'By', 'Bz', 'flow_speed', 'proton_density', 
                'flow_pressure', 'one_minus_M_AE', 'SYM_H_index']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
df.replace([9999.99, 99999.9, 999.990, 99.9900, -999.9], np.nan, inplace=True)

# B magnitude
df['B_magnitude'] = np.sqrt(df['Bx']**2 + df['By']**2 + df['Bz']**2)
df.set_index('timestamp', inplace=True)

#------------------------------------------------------------------------------------
# OUTPUT FOLDER
#------------------------------------------------------------------------------------
output_folder = "../Processed_Data/OMNI_Data/"
os.makedirs(output_folder, exist_ok=True)

#------------------------------------------------------------------------------------
# DICTIONARY MET MOOIE LABELS + EENHEDEN (dit is de magie)
#------------------------------------------------------------------------------------
units_dict = {
    'Bx':            r'$B_x$ (nT)',
    'By':            r'$B_y$ (nT)',
    'Bz':            r'$B_z$ (nT)',
    'B_magnitude':   r'$|B|$ (nT)',
    'flow_speed':    r'Flow speed (km s$^{-1}$)',
    'proton_density':r'Proton density (cm$^{-3}$)',
    'flow_pressure': r'Dynamic pressure (nPa)',
    'one_minus_M_AE':r'AE (nT)',           # dit is eigenlijk -M_AE, maar zo heet het in OMNI
    'SYM_H_index':   r'SYM-H (nT)'
}

#------------------------------------------------------------------------------------
# SAVE CSVs (optioneel, blijft hetzelfde)
#------------------------------------------------------------------------------------
columns_to_plot = list(units_dict.keys())
for col in columns_to_plot:
    out_df = df[[col]].dropna().reset_index()
    out_df.to_csv(f"{output_folder}{col}.csv", index=False, encoding='utf-8')

#------------------------------------------------------------------------------------
# PLOT MET PERFECTE Y-LABELS (dit wil je)
#------------------------------------------------------------------------------------
for col in columns_to_plot:
    plt.figure(figsize=(12, 3.5), dpi=300)
    plt.plot(df.index, df[col], color='#1f77b4', linewidth=1.2)
    
    plt.title(units_dict[col], fontsize=14, pad=15)
    plt.xlabel('Time (UT) – 10–11 May 2024', fontsize=12)
    plt.ylabel(units_dict[col], fontsize=13)
    
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    plt.savefig(f"{output_folder}{col}.png", dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Perfect PNG saved: {col}.png → {units_dict[col]}")

print("\nOMNI processing complete")