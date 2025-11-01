# May2024_GeomagneticStorm
This project investigates the May 2024 geomagnetic storm using high-resolution datasets from **OMNI** (solar wind and interplanetary magnetic field) and **AMPERE** (field-aligned currents).  
The analysis demonstrates how upstream solar wind conditions modulate the magnetosphere-ionosphere (M-I) system and affect geomagnetic activity.  

The repository contains Python scripts for processing the raw data, generating figures, and producing a LaTeX report summarizing the results. Raw data files are included, while processed CSVs and PNGs are generated automatically by the scripts.
# Repository Structure:
```bash
Project/
│
├── Code/ # Python scripts for processing raw data and generating figures
│ ├── OMNI_Data_Processing.py
│ └── Ampere_Data_Processing.py
│
├── Raw_Data_Files/ # Raw datasets
│ └── OMNI_HRO2_1MIN.csv
│ └── Ampere_Data/ # Here are all the raw Ampere Data files stored
│
├── Report/ # LaTeX report
│ ├── Report.tex
│ ├── Report.pdf
│ └── Graphs_Figures/ # LaTeX figure files
│   └── OMNI_Graph1.tex
│   └── OMNI_Graph2.tex
│   └── Ampere_Figure1.tex
│   └── Ampere_Figure2.tex
│
└── README.md
```
