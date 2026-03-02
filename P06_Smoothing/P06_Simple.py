import pandas as pd
import numpy as np

# Part 1: Segmentation
print("--- Customer Monthly Income Segmentation ---")
cust = pd.DataFrame({'Income': [1800, 4500, 8000, 12000, 2500]})
bins = [0, 2500, 5000, 10000, float('inf')]
lbls = ['$0-2.5K', '$2.5-5K', '$5-10K', '>$10K']
cust['Category'] = pd.cut(cust['Income'], bins=bins, labels=lbls, include_lowest=True)
print(cust.to_string(index=False))

# Part 2: Binning and Smoothing
salaries = sorted([12, 15, 18, 19, 21, 23, 25, 26, 28, 30, 33, 35, 36, 38, 42])
print(f"\nOriginal Salaries: {salaries}")

# 1. Equal Width (4 Bins)
w_bins = np.linspace(min(salaries), max(salaries) + 0.1, 5)
ew = pd.Series(salaries).groupby(pd.cut(salaries, w_bins, right=False), observed=False).apply(list)
print(f"\n1) Equal Width Binning (4 Bins):")
for i, (interval, vals) in enumerate(ew.items()): 
    print(f"   Bin {i+1} [{interval.left:.2f}-{interval.right:.2f}): {list(map(int, vals))}")

# 2. Equal Frequency (3 Bins)
ef_bins = np.array_split(salaries, 3)
print(f"\n2) Equal Frequency Binning (3 Bins):")
for i, b in enumerate(ef_bins): print(f"   Bin {i+1}: {b.tolist()}")

# 3. Smoothing
print(f"\n3) Smoothing (by frequency bins):")
for i, b in enumerate(ef_bins):
    print(f"   Bin {i+1} - Mean: {[round(float(b.mean()),2)] * len(b)}")
    print(f"   Bin {i+1} - Median: {[int(np.median(b))] * len(b)}")
    bounds = [int(min(b)) if abs(x - min(b)) < abs(x - max(b)) else int(max(b)) for x in b]
    print(f"   Bin {i+1} - Boundary: {bounds}\n")

print("[INFO] Execution Complete!")
