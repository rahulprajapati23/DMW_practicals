# Practical 8: FP-Tree example (simplified)

import pandas as pd
import os
from collections import Counter
from anytree import Node, RenderTree

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
try:
    file_path = os.path.join(SCRIPT_DIR, 'Online Retail.xlsx')
    df = pd.read_excel(file_path)
    df = df.dropna(subset=['InvoiceNo', 'Description'])
    df = df.head(2000)
    transactions = df.groupby('InvoiceNo')['Description'].apply(lambda x: list(set(x))).tolist()

    min_support = 5
    item_count = Counter()
    for t in transactions:
        item_count.update(t)

    freq_items = {item: count for item, count in item_count.items() if count >= min_support}

    def sort_transaction(transaction):
        return sorted(
            [item for item in transaction if item in freq_items],
            key=lambda x: (-freq_items[x], x)
        )

    transactions = [sort_transaction(t) for t in transactions]

    root = Node("Null (1)")
    for transaction in transactions:
        current = root
        for item in transaction:
            found = None
            for child in current.children:
                if child.name.startswith(item):
                    found = child
                    break
            if found:
                count = int(found.name.split('(')[-1][:-1]) + 1
                found.name = f"{item} ({count})"
                current = found
            else:
                new_node = Node(f"{item} (1)", parent=current)
                current = new_node

    print("FP-Tree Structure:\n")
    for pre, _, node in RenderTree(root):
        print(f"{pre}{node.name}")
except FileNotFoundError:
    print(f"Online Retail.xlsx not found at {file_path} — place dataset next to this script to run the example.")
