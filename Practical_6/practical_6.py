# Practical 6: Binning and Smoothing

Q1data = {
    "Customer_ID": [1, 2, 3, 4, 5],
    "Monthly_Income": [1800, 4500, 8000, 12000, 2500]
}
Q2data = [12, 15, 18, 19, 21, 23, 25, 26, 28, 30, 33, 35, 36, 38, 42]

# Question 1: Income categories
IncCat = {}
for id in Q1data["Customer_ID"]:
    income = Q1data["Monthly_Income"][id-1]
    if income <= 2500:
        IncCat[id] = "$0 - $2,500"
    elif income <= 5000:
        IncCat[id] = "$2,501 - $5,000"
    elif income <= 10000:
        IncCat[id] = "$5,001 - $10,000"
    elif income >= 10001:
        IncCat[id] = "$10,001 and above"

print("Income Distribution:")
for i in IncCat:
    print(f"    {i}       :  {IncCat[i]}")

# Question 2: Binning on Q2data
print(f"Original Data: {Q2data}")
Q2data.sort()
print(f"Sorted Data: {Q2data}")

# 1) Equal Width Binning
bin_no = 4
bin_width = (max(Q2data) - min(Q2data)) / bin_no
width_bins = [[], [], [], []]
for i in Q2data:
    if i <= min(Q2data) + bin_width:
        width_bins[0].append(i)
    elif i <= min(Q2data) + 2 * bin_width:
        width_bins[1].append(i)
    elif i <= min(Q2data) + 3 * bin_width:
        width_bins[2].append(i)
    else:
        width_bins[3].append(i)

print(f"\nEqual Width Binning (4 bins):")
for i in range(bin_no):
    print(f"Bin {i+1}: {width_bins[i]}")

# 2) Equal Frequency Binning
bin_no = 3
bin_size = len(Q2data) // bin_no
freq_bins = [[], [], []]
for i in Q2data:
    if i <= Q2data[bin_size - 1]:
        freq_bins[0].append(i)
    elif i <= Q2data[2 * bin_size - 1]:
        freq_bins[1].append(i)
    else:
        freq_bins[2].append(i)

print(f"\nEqual Frequency Binning (3 bins):")
for i in range(bin_no):
    print(f"Bin {i+1}: {freq_bins[i]}")

# 3) Smoothing by mean, median and boundary values
mean_smoothed = [[], [], []]
for i in range(bin_no):
    if freq_bins[i]:
        mean_val = sum(freq_bins[i]) / len(freq_bins[i])
        mean_smoothed[i] = [mean_val] * len(freq_bins[i])
print("\nMean Smoothed Bins:")
for i in range(bin_no):
    print(f"Bin {i+1}: {mean_smoothed[i]}")

median_smoothed = [[], [], []]
for i in range(bin_no):
    if freq_bins[i]:
        if len(freq_bins[i]) % 2 == 0:
            median_val = (freq_bins[i][len(freq_bins[i]) // 2 - 1] + freq_bins[i][len(freq_bins[i]) // 2]) / 2
        else:
            median_val = freq_bins[i][len(freq_bins[i]) // 2]
        median_smoothed[i] = [median_val] * len(freq_bins[i])
print("\nMedian Smoothed Bins:")
for i in range(bin_no):
    print(f"Bin {i+1}: {median_smoothed[i]}")

boundary_smoothed = [[], [], []]
for i in range(bin_no):
    if freq_bins[i]:
        boundary_smoothed[i] = [freq_bins[i][0]] * len(freq_bins[i])
        boundary_smoothed[i][-1] = freq_bins[i][-1]
print("\nBoundary Smoothed Bins:")
for i in range(bin_no):
    print(f"Bin {i+1}: {boundary_smoothed[i]}")
