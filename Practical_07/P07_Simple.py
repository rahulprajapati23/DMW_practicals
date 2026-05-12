# Practical 7: Apriori Algorithm - Simple Version

from itertools import combinations
from collections import Counter
import pandas as pd
import os

# Part 1: Frequent itemsets from transactions
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

def get_support(itemset, trans):
    return sum(1 for t in trans if set(itemset).issubset(set(t)))

# Generate frequent itemsets
L = []
for size in range(1, 4):
    itemset_counts = {}
    if size == 1:
        for item in set(item for t in transactions for item in t):
            count = get_support([item], transactions)
            if count >= min_count:
                itemset_counts[frozenset([item])] = count
    else:
        prev = list(L[-1].keys())
        for i1, i2 in combinations(prev, 2):
            itemset = i1 | i2
            if len(itemset) == size:
                count = get_support(itemset, transactions)
                if count >= min_count:
                    itemset_counts[itemset] = count
    
    if not itemset_counts:
        break
    L.append(itemset_counts)

print("Frequent Itemsets with Support:")
for level in L:
    for itemset, count in level.items():
        print(f"{set(itemset)}: {count}")

# Part 2: Real retail data (if available)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
try:
    df = pd.read_excel(os.path.join(SCRIPT_DIR, 'Online Retail.xlsx'))
    transactions_real = df.groupby('InvoiceNo')['Description'].apply(lambda x: list(set(x))).tolist()
    
    item_counter = Counter()
    for t in transactions_real:
        item_counter.update(t)
    
    pair_counter = Counter()
    for t in transactions_real:
        pair_counter.update(combinations(t, 2))
    
    print("\nTop 10 Most Popular Items:")
    for i, (item, count) in enumerate(item_counter.most_common(10), 1):
        print(f"{i}. {item} → {count}")
    
    print("\nTop 10 Most Frequent Item Pairs:")
    for i, (pair, count) in enumerate(pair_counter.most_common(10), 1):
        print(f"{i}. {pair[0]} + {pair[1]} → {count}")
except FileNotFoundError:
    print("\nOnline Retail.xlsx not found for Part 2")
