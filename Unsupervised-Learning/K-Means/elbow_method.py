# Practicing K-Means Clustering today, September 16, 2025.


# Import necessary libraries
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# --- 1. Data Loading ---
# Load the dataset from the CSV file
df = pd.read_csv("mall-customers.csv")

# Select the features for clustering
X = df[['Annual_Income', 'Spending_Score']]

# --- 2. Finding Optimal K using Elbow Method ---
inertia_scores = []
k_values = range(1, 10)

# Loop through K values to find the inertia for each cluster number
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    inertia_scores.append(kmeans.inertia_)

# --- 3. Plotting the Elbow Curve ---
plt.figure(figsize=(10, 6))
plt.plot(k_values, inertia_scores, marker='o', linestyle='--')

plt.title('The Elbow Method for Optimal K')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia (Within-cluster sum of squares)')
plt.grid(True) # Add a grid for better readability
plt.show()