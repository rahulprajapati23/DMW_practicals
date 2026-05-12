# Practical 6: Binning - Simple Version

# Question 1: Income categorization
Q1data = {
    "Customer_ID": [1, 2, 3, 4, 5],
    "Monthly_Income": [1800, 4500, 8000, 12000, 2500]
}

print("Income Categories:")
for cid, income in zip(Q1data["Customer_ID"], Q1data["Monthly_Income"]):
    if income <= 2500:
        cat = "$0 - $2,500"
    elif income <= 5000:
        cat = "$2,501 - $5,000"
    elif income <= 10000:
        cat = "$5,001 - $10,000"
    else:
        cat = "$10,001 and above"
    print(f"Customer {cid}: {cat}")

# Question 2: Binning on salary data
data = [12, 15, 18, 19, 21, 23, 25, 26, 28, 30, 33, 35, 36, 38, 42]
data.sort()

print(f"\nOriginal Data: {data}")

# Equal Width Binning (4 bins)
bin_width = (max(data) - min(data)) / 4
width_bins = [[], [], [], []]
for val in data:
    bin_idx = min(3, int((val - min(data)) / bin_width))
    width_bins[bin_idx].append(val)

print("\nEqual Width Binning (4 bins):")
for i, bin_vals in enumerate(width_bins):
    print(f"Bin {i+1}: {bin_vals}")

# Equal Frequency Binning (3 bins)
bin_size = len(data) // 3
freq_bins = [data[i*bin_size:(i+1)*bin_size] for i in range(3)]

print("\nEqual Frequency Binning (3 bins):")
for i, bin_vals in enumerate(freq_bins):
    print(f"Bin {i+1}: {bin_vals}")

# Smoothing by Mean
print("\nMean Smoothing:")
for i, bin_vals in enumerate(freq_bins):
    mean = sum(bin_vals) / len(bin_vals)
    print(f"Bin {i+1}: {[mean] * len(bin_vals)}")

# Smoothing by Median
print("\nMedian Smoothing:")
for i, bin_vals in enumerate(freq_bins):
    sorted_vals = sorted(bin_vals)
    median = sorted_vals[len(sorted_vals)//2]
    print(f"Bin {i+1}: {[median] * len(bin_vals)}")

# Smoothing by Boundary
print("\nBoundary Smoothing:")
for i, bin_vals in enumerate(freq_bins):
    boundary = [bin_vals[0]] * len(bin_vals)
    boundary[-1] = bin_vals[-1]
    print(f"Bin {i+1}: {boundary}")
