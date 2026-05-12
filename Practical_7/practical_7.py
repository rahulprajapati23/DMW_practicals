# Practical 7: Apriori Algorithm and Market Basket Analysis

from itertools import combinations
from collections import defaultdict, Counter
import pandas as pd
import os

# Part 1: Small transactions example and frequent itemset counting
transactions = [
    ['Milk', 'Bread', 'Butter'],
    ['Bread', 'Butter'],
    ['Milk', 'Bread'],
    ['Milk', 'Butter'],
    ['Bread', 'Butter'],
    ['Milk', 'Bread', 'Butter'],
    ['Milk', 'Bread'],
    ['Butter'],
    ['Milk', 'Butter'],
    ['Milk', 'Bread', 'Butter']
]

min_support = 0.3
min_count = int(min_support * len(transactions))

def get_support(itemset):
    count = 0
    for t in transactions:
        if set(itemset).issubset(set(t)):
            count += 1
    return count

L = []
L1 = {}
items = set(item for t in transactions for item in t)
for item in items:
    count = get_support([item])
    if count >= min_count:
        L1[frozenset([item])] = count
L.append(L1)

k = 2
while True:
    prev_L = list(L[-1].keys())
    candidates = set()
    for i in range(len(prev_L)):
        for j in range(i+1, len(prev_L)):
            union = prev_L[i] | prev_L[j]
            if len(union) == k:
                candidates.add(union)
    Lk = {}
    for candidate in candidates:
        count = get_support(candidate)
        if count >= min_count:
            Lk[candidate] = count
    if not Lk:
        break
    L.append(Lk)
    k += 1

print("Frequent Itemsets with Support:\n")
for level in L:
    for itemset, count in level.items():
        print(set(itemset), ":", count)

# Part 2: Using an online retail dataset (requires local file 'Online Retail.xlsx')
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
try:
    file_path = os.path.join(SCRIPT_DIR, 'Online Retail.xlsx')
    df = pd.read_excel(file_path)
    transactions = df.groupby('InvoiceNo')['Description'].apply(lambda x: list(set(x))).tolist()

    item_counter = Counter()
    for t in transactions:
        item_counter.update(t)

    pair_counter = Counter()
    for t in transactions:
        pair_counter.update(combinations(t, 2))

    print('\nTop 10 Most Popular Items:\n')
    for i, (item, count) in enumerate(item_counter.most_common(10), 1):
        print(f"{i}. {item} → {count}")

    print('\nTop 10 Most Frequent Item Combinations:\n')
    for i, (pair, count) in enumerate(pair_counter.most_common(10), 1):
        print(f"{i}. {pair[0]} + {pair[1]} → {count}")
except FileNotFoundError:
    print("Online Retail dataset not found. Place 'Online Retail.xlsx' next to this script to run the second part.")
