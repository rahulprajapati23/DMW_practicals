# Practical 10: Clustering - Mall Customer Segmentation

import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "Mall_Customers.csv")


def main():
    try:
        df = pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        print(f"{DATA_PATH} not found. Place the file next to this script to run the example.")
        return

    print(df.head())
    print(df.columns)

    # Expecting columns like 'Age', 'Annual_Income_(k$)', 'Spending_Score'
    # Update feature names below if your CSV uses different column names.
    features = df[['Age', 'Annual_Income_(k$)', 'Spending_Score']]

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # Elbow method to find optimal clusters
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
        kmeans.fit(scaled_features)
        wcss.append(kmeans.inertia_)

    plt.plot(range(1, 11), wcss)
    plt.xlabel("Number of Clusters")
    plt.ylabel("WCSS")
    plt.title("Elbow Method")
    plt.show()

    # Apply KMeans (k = 5)
    kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(scaled_features)

    # Visualize clusters by Annual Income vs Spending Score
    for i in range(5):
        plt.scatter(
            df[df['Cluster'] == i]['Annual_Income_(k$)'],
            df[df['Cluster'] == i]['Spending_Score'],
            label=f'Cluster {i}'
        )

    # Plot centroids (inverse-transform to original scale)
    centroids = scaler.inverse_transform(kmeans.cluster_centers_)
    plt.scatter(centroids[:, 1], centroids[:, 2], marker='X', s=200, label='Centroids')

    plt.xlabel("Annual Income (k$)")
    plt.ylabel("Spending Score")
    plt.title("Customer Segmentation")
    plt.legend()
    plt.show()

    # Save result
    out_path = "Mall_Customers_Clustered.csv"
    df.to_csv(out_path, index=False)
    print(f"Saved clustered results to {out_path}")


if __name__ == '__main__':
    main()
