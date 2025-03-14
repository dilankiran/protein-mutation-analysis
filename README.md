# Mutation Hydropathy Analysis

## Overview
This project analyzes the **hydropathy index differences** between wild-type (WT) and mutant proteins and their impact on protein stability. The analysis is based on **experimental ΔΔG values (ddG)**, which indicate whether mutations stabilize or destabilize the protein structure.

The project includes:
- **Data preprocessing** – Reading hydropathy difference values from external files (CSV/TXT).
- **Correlation Analysis** – Assessing relationships between hydropathy shifts and experimental ddG values.
- **Statistical Tests** – Evaluating significance using T-tests.
- **Visualizations** – Scatter plots, regression lines, and box plots for enriched and depleted mutations.

## Contribution
These are contributions to my **internship at Karaca Lab** in the **Izmir Biomedicine and Genome Center**.  
Here, I conducted a **statistical analysis of training data** for selected features and created **box plots and scatter plots**.  
These codes include **plot creation and R-value calculations** to better understand the correlation between mutation hydropathy and protein stability.

## Files & Data
- **`data.csv`** – Contains hydropathy differences (`diff`) and experimental ΔΔG (`ddg`) values.
- **`diff_depleted.txt`** – List of mutations with the most negative ΔΔG values (most depleted).
- **`diff_enriched.txt`** – List of mutations with the highest ΔΔG values (most enriched).
- **`mutation_hydropathy_analysis.py`** – The main script for performing the analysis.

## How to Use
1. **Prepare Data:** Ensure `data.csv`, `diff_depleted.txt`, and `diff_enriched.txt` are in the same directory as the script.
2. **Run the Script:** Execute `mutation_hydropathy_analysis.py` using Python:
   ```bash
   python mutation_hydropathy_analysis.py
   ```
3. **Interpret Results:**  
   - Scatter plots will show the correlation between mutation hydropathy changes and ΔΔG values.
   - R² values and p-values will be printed to indicate statistical significance.
   - Box plots will visualize data distribution.

## Dependencies
Ensure you have the following Python libraries installed:
```bash
pip install numpy pandas matplotlib scipy
```

## Results Interpretation
- **A high R² value** – Indicates a strong correlation between hydropathy differences and protein stability.
- **A low p-value (< 0.05)** – Suggests significant differences between the groups.
- **Scatter plots & regression lines** – Show overall trends in the data.


