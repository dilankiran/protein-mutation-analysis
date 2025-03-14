import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load data from CSV file
data = pd.read_csv("stability_data.csv")

# Extract columns
stab_diff = data["stab_diff"].values
ddg_exp = data["ddg_exp"].values

# Scatter plot and linear regression
plt.scatter(stab_diff, ddg_exp, label="Data Points")
m, b = np.polyfit(stab_diff, ddg_exp, 1)
plt.plot(stab_diff, m * stab_diff + b, color="red", label="Best Fit Line")
plt.xlabel("Stability Differences between WT and Mut")
plt.ylabel("Experimental ΔΔG Values")
plt.title("Stability Hydropathy Differences Analysis")
plt.legend()
plt.show()

# Compute correlation and R-squared value
correlation_matrix = np.corrcoef(stab_diff, ddg_exp)
correlation_stabdiff_dgg = correlation_matrix[0, 1]
r_squared = correlation_stabdiff_dgg ** 2
print(f"R-squared (stability differences): {r_squared:.6f}")

# Box plot for stability differences
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)
bp = ax.boxplot(stab_diff, patch_artist=True, notch=True, vert=0)

for patch in bp['boxes']:
    patch.set_facecolor('#00FF00')  # Green color for boxes
for whisker in bp['whiskers']:
    whisker.set(color='#8B008B', linewidth=1.5, linestyle=":")

plt.title("Stability Differences between WT and Mut")
plt.show()

# Perform statistical test
p_stab = stats.ttest_ind(stab_diff, ddg_exp)
print(f"T-test p-value (Stability Differences): {p_stab.pvalue:.6f}")
