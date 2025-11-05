# May2024_GeomagneticStorm
This project investigates the May 2024 geomagnetic storm using high-resolution datasets from **OMNI** (solar wind and interplanetary magnetic field) and **AMPERE** (field-aligned currents).  
The analysis demonstrates how upstream solar wind conditions modulate the magnetosphere-ionosphere (M-I) system and affect geomagnetic activity.  

The repository contains Python scripts for processing the raw data, generating figures, and producing a LaTeX report summarizing the results. Raw data files are included, while processed CSVs and PNGs are generated automatically by the scripts.
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
