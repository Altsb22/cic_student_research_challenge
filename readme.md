# Mental Health, Economic Strain, and Vaccine Uptake During COVID-19: 
## A Longitudinal, Data-Driven Story (2020–2023) 

![Python](https://img.shields.io/badge/python-3.13%2B-blue.svg)
![Conda](https://img.shields.io/badge/conda-compatible-green.svg)
![Jupyter](https://img.shields.io/badge/jupyterlab-4.0%2B-orange.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.xxxxxxx.svg)](https://doi.org/10.5281/zenodo.xxxxxxx)

# Purpose
This repository serves as the data and methods appendix for the research paper  
*"Mental Health, Economic Strain, and Vaccine Uptake During COVID-19: 
A Longitudinal, Data-Driven Story (2020–2023)"*  
It integrates public datasets (KFF, CDC, Google Dataset Publishing Language) and applies OLS and LASSO regression  
to examine the relationship between economic strain, mental health distress, and COVID-19 vaccination coverage. 

Repository structure is delineated in File_Guide.pdf.

# Mental Health, Economic Strain, and Vaccine Uptake During COVID-19:
## A Longitudinal, Data-Driven Story (2020–2023)

![Python](https://img.shields.io/badge/python-3.13%2B-blue.svg)
![Conda](https://img.shields.io/badge/conda-compatible-green.svg)
![Jupyter](https://img.shields.io/badge/jupyterlab-4.0%2B-orange.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)
![Last Commit](https://img.shields.io/github/last-commit/Altsb22/cic_student_research_challenge)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.xxxxxxx.svg)](https://doi.org/10.5281/zenodo.xxxxxxx)

This repository serves as the **data & methods appendix** for the research paper:  
*“Mental Health, Economic Strain, and Vaccine Uptake During COVID-19: A Longitudinal, Data-Driven Story (2020–2023).”*  

It integrates public datasets (CDC, KFF, CBPP, BLS, BEA, Census) and applies regression modeling (OLS, LASSO, Post-LASSO OLS) to examine the relationships between economic strain, mental health distress, and COVID-19 vaccine uptake across U.S. states from 2020 to 2023.

---

## 📂 Repository Structure

- `data/` → state-level datasets (2020–2023).  For quick specific info on file contents refer the the File_Guide.pdf
- `scripts/` → analysis code & notebooks  
  - `cic_challenge_regression.ipynb` → main analysis notebook  
  - `smoke_test.py` → environment verification script  
- `output/` → generated figures, maps, and regression tables  
- `requirements.txt` → pip dependencies  
- `environment.yml` → Conda environment file  
- `LICENSE` → open source license (MIT)  
- `CITATION.cff` → citation metadata  

---

## 🚀\ Getting Started

> Requires **Python ≥ 3.13**

### 1. Clone this repository
```bash
git clone https://github.com/Altsb22/cic_student_research_challenge
cd cic_student_research_challenge

### Run the Smoke Test

There are two ways to verify the environment:  

**Option A — in JupyterLab**  
1. Start JupyterLab  
   ```bash
   conda activate mental-health-economic-strain-covid-vaccine
   jupyter lab
2. Open scripts/smoke_test.ipynb
3.Run all cells

Option B — in terminal
Run the script version:
python scripts/smoke_test.py

Both versions will:
 -Print package versions
 -Run a sample OLS and LASSO regression
 -Save output/smoke_pairplot.png
 -Save output/smoke_map.html
