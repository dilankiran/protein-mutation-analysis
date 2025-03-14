import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load data from CSV files
data = pd.read_csv("proximal_data.csv")
depleted_data = pd.read_csv("depleted_data.csv")
enriched_data = pd.read_csv("enriched_data.csv")

# Extract columns
proximal_diff = data["proximal_diff"].values
ddg_exp = data["ddg_exp"].values

diff_depleted = depleted_data["diff_depleted"].values
most_depleted = depleted_data["most_depleted"].values

diff_enriched = enriched_data["diff_enriched"].values
most_enriched = enriched_data["most_enriched"].values

# Scatter plot and linear regression
plt.scatter(proximal_diff, ddg_exp, label="Data Points")
m, b = np.polyfit(proximal_diff, ddg_exp, 1)
plt.plot(proximal_diff, m * proximal_diff + b, color="red", label="Best Fit Line")
plt.xlabel("Proximal Differences between WT and Mut")
plt.ylabel("Experimental ΔΔG Values")
plt.title("Proximal Hydropathy Differences Analysis")
plt.legend()
plt.show()

# Compute correlation and R-squared value
correlation_matrix = np.corrcoef(proximal_diff, ddg_exp)
correlation_proximal = correlation_matrix[0, 1]
r_squared = correlation_proximal ** 2
print(f"R-squared (all data): {r_squared:.6f}")

# Scatter plot for most depleted values
plt.scatter(diff_depleted, most_depleted, label="Data Points")
m, b = np.polyfit(diff_depleted, most_depleted, 1)
plt.plot(diff_depleted, m * diff_depleted + b, color="blue", label="Best Fit Line")
plt.xlabel("Differences between WT and Mut")
plt.ylabel("Experimental ΔΔG Values")
plt.title("Most Depleted")
plt.legend()
plt.show()

# Compute R-squared for depleted data
correlation_matrix = np.corrcoef(diff_depleted, most_depleted)
correlation_depleted = correlation_matrix[0, 1]
r_squared_depleted = correlation_depleted ** 2
print(f"R-squared (most depleted): {r_squared_depleted:.6f}")

# Scatter plot for most enriched values
plt.scatter(diff_enriched, most_enriched, label="Data Points")
m, b = np.polyfit(diff_enriched, most_enriched, 1)
plt.plot(diff_enriched, m * diff_enriched + b, color="green", label="Best Fit Line")
plt.xlabel("Differences between WT and Mut")
plt.ylabel("Experimental ΔΔG Values")
plt.title("Most Enriched")
plt.legend()
plt.show()

# Compute R-squared for enriched data
correlation_matrix = np.corrcoef(diff_enriched, most_enriched)
correlation_enriched = correlation_matrix[0, 1]
r_squared_enriched = correlation_enriched ** 2
print(f"R-squared (most enriched): {r_squared_enriched:.6f}")

# Perform statistical tests
p_prox = stats.ttest_ind(proximal_diff, ddg_exp)
p_depleted = stats.ttest_ind(diff_depleted, most_depleted)
p_enriched = stats.ttest_ind(diff_enriched, most_enriched)

print(f"T-test p-value (Proximal Differences): {p_prox.pvalue:.6f}")
print(f"T-test p-value (Most Depleted): {p_depleted.pvalue:.6f}")
print(f"T-test p-value (Most Enriched): {p_enriched.pvalue:.6f}")

# Box plot function
def create_boxplot(data, title):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(data, patch_artist=True, notch=True, vert=0)
    for patch in bp['boxes']:
        patch.set_facecolor('#00FF00')  # Green color for boxes
    for whisker in bp['whiskers']:
        whisker.set(color='#8B008B', linewidth=1.5, linestyle=":")
    plt.title(title)
    plt.show()

# Box plots
create_boxplot(diff_enriched, "Most Enriched")
create_boxplot(diff_depleted, "Most Depleted")
create_boxplot(proximal_diff, "Proximal Differences of WT and Mut")
