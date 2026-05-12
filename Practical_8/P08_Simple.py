# Practical 8: FP-Tree - Simple Version

import pandas as pd
import os
from collections import Counter
from anytree import Node, RenderTree

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
try:
    df = pd.read_excel(os.path.join(SCRIPT_DIR, 'Online Retail.xlsx'))
    df = df.dropna(subset=['InvoiceNo', 'Description'])
    df = df.head(2000)
    
    transactions = df.groupby('InvoiceNo')['Description'].apply(lambda x: list(set(x))).tolist()
    
    # Count item frequency
    item_count = Counter()
    for t in transactions:
        item_count.update(t)
    
    # Filter frequent items (support >= 5)
    freq_items = {item: count for item, count in item_count.items() if count >= 5}
    
    # Sort transactions by frequency
    transactions = [
        sorted(
            [item for item in t if item in freq_items],
            key=lambda x: (-freq_items[x], x)
        )
        for t in transactions
    ]
    
    # Build FP-Tree
    root = Node("Null (1)")
    
    for transaction in transactions:
        current = root
        for item in transaction:
            # Find or create child
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
                current = Node(f"{item} (1)", parent=current)
    
    # Display tree
    print("FP-Tree Structure:")
    for pre, _, node in RenderTree(root):
        print(f"{pre}{node.name}")
        
except FileNotFoundError:
    print(f"Online Retail.xlsx not found")
