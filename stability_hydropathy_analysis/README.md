# Stability Hydropathy Analysis

## Overview
This project analyzes **stability hydropathy differences** between wild-type (WT) and mutant proteins to assess their impact on protein stability. The analysis is based on **experimental ΔΔG values (ddG)**, which indicate whether mutations stabilize or destabilize the protein structure.

The project includes:
- **Data preprocessing** – Reading stability difference values from external CSV files.
- **Correlation Analysis** – Assessing relationships between stability shifts and experimental ddG values.
- **Statistical Tests** – Evaluating significance using T-tests.
- **Visualizations** – Scatter plots, regression lines, and box plots for stability differences.

## Files & Data
- **`data/stability_data.csv`** – Contains stability differences (`stab_diff`) and experimental ΔΔG (`ddg_exp`) values.
- **`src/stability_analysis.py`** – Main script for data analysis.

## How to Use
1. **Ensure Data Availability:** Place the CSV file inside the `data/` directory.
2. **Run the Analysis Script:** Execute the Python script:
   ```bash
   python src/stability_analysis.py
   ```
3. **Interpret Results:**
   - Scatter plots will display the correlation between stability differences and ΔΔG values.
   - R² values and p-values will be printed to indicate statistical significance.
   - Box plots will visualize data distribution.

## Dependencies
Ensure you have the following Python libraries installed:
```bash
pip install numpy pandas matplotlib scipy
```

## Results Interpretation
- **A high R² value** – Indicates a strong correlation between stability differences and protein stability.
- **A low p-value (< 0.05)** – Suggests significant differences between the groups.
- **Scatter plots & regression lines** – Show overall trends in the data.


