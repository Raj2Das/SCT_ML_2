# ==========================================
# K-MEANS CUSTOMER SEGMENTATION
# Mall Customers Dataset
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ------------------------------------------
# 1. LOAD DATASET
# ------------------------------------------

df = pd.read_csv("Mall_Customers.csv")

print("\nDataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())

# ------------------------------------------
# 2. SELECT FEATURES
# ------------------------------------------

X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# ------------------------------------------
# 3. SCALE FEATURES
# ------------------------------------------

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ------------------------------------------
# 4. ELBOW METHOD
# ------------------------------------------

wcss = []

for i in range(1, 11):
    model = KMeans(
        n_clusters=i,
        random_state=42,
        n_init=10
    )

    model.fit(X_scaled)
    wcss.append(model.inertia_)

# ------------------------------------------
# 5. ELBOW PLOT
# ------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    range(1, 11),
    wcss,
    marker='o',
    linewidth=3,
    markersize=10
)

plt.title(
    "Elbow Method for Optimal K",
    fontsize=16,
    fontweight='bold'
)

plt.xlabel("Number of Clusters (K)", fontsize=12)
plt.ylabel("WCSS", fontsize=12)

plt.grid(True, linestyle='--', alpha=0.7)

plt.show()

# ------------------------------------------
# 6. TRAIN K-MEANS
# ------------------------------------------

k = 5

kmeans = KMeans(
    n_clusters=k,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(X_scaled)

df["Cluster"] = clusters

# ------------------------------------------
# 7. GET CENTROIDS
# ------------------------------------------

centroids = scaler.inverse_transform(
    kmeans.cluster_centers_
)

# ------------------------------------------
# 8. CLUSTER VISUALIZATION
# ------------------------------------------

colors = [
    '#1f77b4',
    '#ff7f0e',
    '#2ca02c',
    '#d62728',
    '#9467bd'
]

plt.figure(figsize=(12, 8))

for i in range(k):

    plt.scatter(
        df[df["Cluster"] == i]["Annual Income (k$)"],
        df[df["Cluster"] == i]["Spending Score (1-100)"],
        s=120,
        color=colors[i],
        label=f'Cluster {i+1}',
        alpha=0.8
    )

# Plot centroids

plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    s=400,
    c='black',
    marker='X',
    label='Centroids'
)

plt.title(
    "Customer Segmentation using K-Means",
    fontsize=18,
    fontweight='bold'
)

plt.xlabel("Annual Income (k$)", fontsize=12)
plt.ylabel("Spending Score (1-100)", fontsize=12)

plt.legend(fontsize=10)

plt.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()

plt.show()

# ------------------------------------------
# 9. CLUSTER SUMMARY
# ------------------------------------------

summary = df.groupby("Cluster").agg({
    "Annual Income (k$)": "mean",
    "Spending Score (1-100)": "mean",
    "CustomerID": "count"
}).rename(columns={
    "CustomerID": "Number of Customers"
})

print("\nCluster Summary:")
print(summary.round(2))

# ------------------------------------------
# 10. CUSTOMER SEGMENT LABELS
# ------------------------------------------

segment_names = {
    0: "Average Customers",
    1: "High Income - High Spending",
    2: "Low Income - High Spending",
    3: "High Income - Low Spending",
    4: "Low Income - Low Spending"
}

df["Segment"] = df["Cluster"].map(segment_names)

print("\nCustomer Segments:")
print(df[[
    "CustomerID",
    "Annual Income (k$)",
    "Spending Score (1-100)",
    "Segment"
]].head(10))

# ------------------------------------------
# 11. SAVE RESULTS
# ------------------------------------------

df.to_csv(
    "Customer_Segmentation_Result.csv",
    index=False
)

print(
    "\nResults saved as "
    "'Customer_Segmentation_Result.csv'"
)