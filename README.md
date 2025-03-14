# Protein Mutation Analysis Repository

## Overview
This repository consolidates three distinct projects focused on analyzing **protein mutations and their impact on hydropathy, stability, and ΔΔG values**. Each project contributes to understanding the relationships between **wild-type (WT) and mutant proteins** through statistical analysis, visualizations, and correlation studies.

These projects were developed as part of my **internship at Karaca Lab, Izmir Biomedicine and Genome Center**, where I performed **data preprocessing, statistical analysis, and visualization of hydropathy and stability changes in mutated proteins**.

## Repository Structure
```
protein-mutation-analysis/
│-- mutation-hydropathy-analysis/
│   │-- README.md
│   │-- data.csv
│   │-- ddG_hydropathy_study.py
│   │-- diff_depleted.txt
│   │-- diff_enriched.txt
│
│-- stability_hydropathy_analysis/
│   │-- README.md
│   │-- stability_data.csv
│   │-- stability_vs_ddG.py
│
│-- wt_mutant_ddG_analysis/
│   │-- README.md
│   │-- depleted_data.csv
│   │-- enriched_data.csv
│   │-- mutation_proximal_ddG.py
│   │-- proximal_data.csv
│
│-- README.md (This File)
```

## Projects Included
### 1. **Mutation Hydropathy Analysis**
- Examines how **hydropathy index differences** impact experimental ΔΔG values.
- Utilizes **scatter plots, regression analysis, and statistical tests** to determine relationships.
- **Files:** `data.csv`, `ddG_hydropathy_study.py`, `diff_depleted.txt`, `diff_enriched.txt`

### 2. **Stability Hydropathy Analysis**
- Investigates how **stability differences between WT and mutant proteins** correlate with ΔΔG.
- Includes **correlation analysis, box plots, and p-value calculations**.
- **Files:** `stability_data.csv`, `stability_vs_ddG.py`

### 3. **WT vs. Mutant ΔΔG Analysis**
- Focuses on **proximal stability differences** in mutant proteins.
- **Statistical evaluations and visualizations** for enriched and depleted mutations.
- **Files:** `proximal_data.csv`, `depleted_data.csv`, `enriched_data.csv`, `mutation_proximal_ddG.py`

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/dilankiran/protein-mutation-analysis.git
   cd protein-mutation-analysis
   ```
2. Install dependencies:
   ```bash
   pip install numpy pandas matplotlib scipy
   ```
3. Navigate to a project folder and run the analysis script:
   ```bash
   python script_name.py
   ```

## Results Interpretation
- **High R² values** indicate strong correlations between hydropathy/stability and ΔΔG.
- **Low p-values (< 0.05)** suggest statistically significant findings.
- **Box plots and scatter plots** provide insights into mutation effects.

## Suggested Repository Name
1. **`protein-mutation-analysis`** (Recommended) – General and professional.
2. **`mutation-stability-hydropathy`** – Highlights the key focus areas.
3. **`wt-mutant-ddG-study`** – Emphasizes the ΔΔG analysis.
4. **`karaca-lab-mutation-study`** – Recognizes the contribution to Karaca Lab.

## License
MIT License – Free to use and modify.

---
This repository provides an integrated approach to studying **protein mutations and stability changes** through computational analysis. Feel free to contribute or use the insights for further research!

