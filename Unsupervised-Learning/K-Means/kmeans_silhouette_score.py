# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score 

# --- 1. Data Loading ---
df = pd.read_csv("CC GENERAL.csv")
df = df.drop("CUST_ID", axis=1)
df.fillna(df.mean(), inplace=True)

# --- 2. Feature Scaling ---
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# --- 3. Model Training (using K=8 ) ---
final_kmeans = KMeans(n_clusters=8, n_init=10, random_state=42)
cluster_labels = final_kmeans.fit_predict(X_scaled)

# --- 4. Performance Evaluation ---
# Calculate the Silhouette Score
score = silhouette_score(X_scaled, cluster_labels)

print(f"The Silhouette Score for K=8 is: {score:.4f}")
print("(A score closer to +1 is better, indicating dense and well-separated clusters.)")