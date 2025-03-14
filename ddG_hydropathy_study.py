import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load data from CSV file
data = pd.read_csv("data.csv")

# Extract columns
diff = data["diff"].values
ddg = data["ddg"].values

# Scatter plot and linear regression
plt.scatter(diff, ddg, label="Data Points")
m, b = np.polyfit(diff, ddg, 1)
plt.plot(diff, m * diff + b, color="red", label="Best Fit Line")
plt.xlabel("Differences between WT and Mut")
plt.ylabel("Experimental ΔΔG Values")
plt.title("Hydropathy Index Differences of Wild Type and Mutant")
plt.legend()
plt.show()

# Compute correlation and R-squared value
correlation_matrix = np.corrcoef(diff, ddg)
correlation_diff_ddg = correlation_matrix[0, 1]
r_squared = correlation_diff_ddg ** 2
print(f"R-squared (all data): {r_squared:.6f}")

# Identify most depleted and enriched values
most_depleted = sorted([i for i in ddg if i < 0])
most_enriched = sorted([i for i in ddg if i > 0])

# Load corresponding diff values (manually specified)
diff_depleted = np.loadtxt("diff_depleted.txt")  # Create and store values in a TXT file
diff_enriched = np.loadtxt("diff_enriched.txt")  # Create and store values in a TXT file

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
p_hydro = stats.ttest_ind(diff, ddg)
p_depleted = stats.ttest_ind(diff_depleted, most_depleted)
p_enriched = stats.ttest_ind(diff_enriched, most_enriched)

print(f"T-test p-value (Hydropathy Differences): {p_hydro.pvalue:.6f}")
print(f"T-test p-value (Most Depleted): {p_depleted.pvalue:.6f}")
print(f"T-test p-value (Most Enriched): {p_enriched.pvalue:.6f}")

# Box plots for visualization
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

# Box plots for each category
create_boxplot(diff_enriched, "Most Enriched")
create_boxplot(diff_depleted, "Most Depleted")
create_boxplot(diff, "Hydropathy Differences of WT and Mut")
