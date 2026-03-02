import pandas as pd
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("="*50)
print("P06: Customer Segmentation & Data Smoothing")
print("="*50)

# ---------------------------------------------------------
# Part 1: Customer Segmentation
# ---------------------------------------------------------
print("\n--- Part 1: Customer Monthly Income Segmentation ---")

# Raw Dataset
data_p1 = {
    'Customer_ID': [1, 2, 3, 4, 5],
    'Monthly_Income': [1800, 4500, 8000, 12000, 2500]
}
df_customers = pd.DataFrame(data_p1)

# Bins and Labels
bins = [0, 2500, 5000, 10000, float('inf')]
labels = ['$0 - $2,500', '$2,501 - $5,000', '$5,001 - $10,000', '$10,001 and above']

# Apply pd.cut() for segmentation
df_customers['Income_Category'] = pd.cut(
    df_customers['Monthly_Income'], 
    bins=bins, 
    labels=labels, 
    include_lowest=True, 
    right=True
)

print("\nCustomer Data Segmented by Income Bracket:")
print(df_customers.to_string(index=False))

# ---------------------------------------------------------
# Part 2: Data Binning & Smoothing
# ---------------------------------------------------------
print("\n--- Part 2: Data Binning and Smoothing ---")

salaries = [12, 15, 18, 19, 21, 23, 25, 26, 28, 30, 33, 35, 36, 38, 42]
print(f"Original Dataset (Salary in 1000s): \n{salaries}\n")
salaries.sort() # Ensure it is sorted naturally

# 1. Equal Width Binning (4 Bins)
min_val = min(salaries)
max_val = max(salaries)
n_bins_width = 4
width = (max_val - min_val) / n_bins_width

print(f"1) Equal Width Binning ({n_bins_width} bins, width={width}):")
# Determine bin boundaries spanning length of (width) starting from global min
ew_bins = [min_val + i*width for i in range(n_bins_width + 1)]
ew_bins[-1] = max_val + 0.1 # include maximum boundary

cut_ew = pd.cut(salaries, bins=ew_bins, right=False, include_lowest=True)
# .apply(list) converts internal pd arrays to traditional builtin python list formatting visually
grouped_ew = pd.Series(salaries).groupby(cut_ew, observed=False).apply(list)
for i, (interval, values) in enumerate(grouped_ew.items()):
    val_list = list(values) if isinstance(values, list) else values.tolist()
    print(f"   Bin {i+1} [{round(interval.left, 2)} - {round(interval.right, 2)}): {val_list}")

# 2. Equal Frequency Binning (3 Bins)
n_bins_freq = 3
elements_per_bin = len(salaries) // n_bins_freq

print(f"\n2) Equal Frequency Binning ({n_bins_freq} bins):")
ef_bins = [salaries[i : i + elements_per_bin] for i in range(0, len(salaries), elements_per_bin)]
for i, b in enumerate(ef_bins):
    print(f"   Bin {i+1}: {b}")
    
# 3. Smoothing by Mean
print("\n3a) Smoothing by Mean:")
smooth_mean = []
for b in ef_bins:
    mean_val = round(sum(b) / len(b), 2)
    smoothed = [mean_val] * len(b)
    smooth_mean.append(smoothed)
    
for i, b in enumerate(smooth_mean):
    print(f"   Bin {i+1}: {b}")

# 3. Smoothing by Median
print("\n3b) Smoothing by Median:")
smooth_median = []
for b in ef_bins:
    median_val = np.median(b)
    smoothed = [int(median_val) if median_val.is_integer() else median_val] * len(b)
    smooth_median.append(smoothed)
    
for i, b in enumerate(smooth_median):
    print(f"   Bin {i+1}: {b}")

# 3. Smoothing by Boundary
print("\n3c) Smoothing by Boundary:")
smooth_boundary = []
for b in ef_bins:
    min_b = min(b)
    max_b = max(b)
    smoothed = []
    for val in b:
        if abs(val - min_b) < abs(val - max_b):
            smoothed.append(min_b)
        else:
            smoothed.append(max_b)
    smooth_boundary.append(smoothed)

for i, b in enumerate(smooth_boundary):
    print(f"   Bin {i+1}: {b}")

print("\n[INFO] Execution Complete!")
