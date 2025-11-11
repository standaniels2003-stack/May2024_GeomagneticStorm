# May2024_GeomagneticStorm
# FYS3600 Project: The Extreme Geomagnetic Storm of 10–11 May 2024
**Stan Daniels** – University of Oslo – Autumn 2025

This repository contains the complete analysis of one of the strongest geomagnetic storms of Solar Cycle 25 using four independent high-latitude datasets:

- Time-shifted OMNI solar wind and IMF parameters  
- SuperDARN global convection maps  
- AMPERE field-aligned currents  
- IMAGE auroral electrojet indices (AU/AL/IE)

The project clearly demonstrates intense dayside and nightside magnetic reconnection, massive polar cap expansion, cross-polar-cap potentials > 200 kV, Region 1/2 currents exceeding 3 µA/m², and multiple substorms with AL < −3000 nT.
## Repository structure
# Notes on raw data
The raw datasets used in this project are included in the repository under Raw_Data_Files/, but they can also be obtained from the original sources:  
OMNI_HRO2_1MIN: https://cdaweb.gsfc.nasa.gov/index.html  
SuperDARN: https://superdarn.ca/convection-maps  
Ampere: https://ampere.jhuapl.edu/  
IMAGE: https://space.fmi.fi/image/www/index.php?page=home
# How to generate processed data
To generate the processed data run the folowing comands:  
python3 OMNI_Data_Processing.py  
python3 Ampere_Data_Processing.py  
python3 SuperDARN_Data_Processing.py  
python3 IMAGE_Data_Processing.py
# How to generate the pdf yourself
To generate the pdf of the report run the folowwing commands in order:  
pdflatex Report.tex  
bibtex Report  
pdflatex Report.tex  
pdflatex Report.tex
# Repository Structure:
```bash
Project/
│
├── Code/ # Python scripts for processing raw data and generating figures
│ ├── OMNI_Data_Processing.py
│ └── Ampere_Data_Processing.py
│ └── SuperDARN_Data_Processing.py
│ └── IMAGE_Data_Processing.py
│
├── Raw_Data_Files/ # Raw datasets
│ └── OMNI_HRO2_1MIN.csv # This is the csv file used from the OMNI data
│ └── Ampere_Data/ # Here are the raw Ampere data files stored
│ └── SuperDARN_Data/ # Here are the raw data files from SuperDARN stored
│ └── IMAGE_Data/ # Here are the IMAGE Data files stored
│
├── Report/ # LaTeX report
│ ├── References.bib
│ ├── Report.tex
│ ├── Report.pdf
│ └── Graphs_Figures/ # LaTeX figure files
│   └── OMNI_Graph1.tex
│   └── OMNI_Graph2.tex
│   └── SuperDARN_Figure1.tex
│   └── SuperDARN_Figure2.tex
│   └── Ampere_Figure1.tex
│   └── Ampere_Figure2.tex
│   └── IMAGE_Graph.tex
│
└── README.md
```
