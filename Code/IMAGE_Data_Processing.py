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
for col in numeric_cols:
    plt.figure(figsize=(12,3))
    plt.plot(df.index, df[col], color='tab:blue')
    plt.title(f"IMAGE Electrojet: {col}")
    plt.xlabel('Time (UT)')
    plt.ylabel(col)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_folder}{col}.png", dpi=300)
    plt.close()
    print(f"Saved PNG: {output_folder}{col}.png")

print("Processing complete!")
