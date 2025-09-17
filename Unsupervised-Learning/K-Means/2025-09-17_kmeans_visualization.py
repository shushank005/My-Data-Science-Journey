# Import necessary libraries
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns # For better visualization

# --- 1. Data Loading ---
# Load the dataset from the CSV file
df = pd.read_csv("mall-customers.csv")

# Select the features for clustering
X = df[['Annual_Income', 'Spending_Score']]

# --- 2. Model Training ---
# We chose K=5 based on the Elbow Method from yesterday
optimal_k = 5
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)

# Fit the model and predict the clusters
# .fit_predict() trains the model and assigns a cluster to each data point
df['Cluster'] = kmeans.fit_predict(X)

# --- 3. Visualization of Clusters ---
plt.figure(figsize=(10, 8))
sns.scatterplot(data=df, x='Annual_Income', y='Spending_Score', hue='Cluster', palette='viridis', s=100, alpha=0.7, edgecolor='k')

# Plot the centroids
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, marker='X', label='Centroids')

plt.title('Customer Segments using K-Means Clustering (K=5)')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.grid(True)
plt.show()

# Display the first few rows with the new 'Cluster' column
print(df.head())