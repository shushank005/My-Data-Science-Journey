# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

# ---  Data Preparation ---
df = pd.read_csv('Social_Network_Ads.csv')
X = df[['Age', 'EstimatedSalary']]
y = df['Purchased']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ---  Define Models and Their Parameter Grids ---

# Model 1: Logistic Regression
lr = LogisticRegression(max_iter=1000)
lr_params = {'C': [0.1, 1, 10, 100]}

# Model 2: K-Nearest Neighbors (KNN)
knn = KNeighborsClassifier()
knn_params = {'n_neighbors': range(3, 15)}

# Model 3: Random Forest
rf = RandomForestClassifier(random_state=42)
rf_params = {'n_estimators': [50, 100, 200], 'max_depth': [None, 10, 20]}


# --- Run GridSearchCV for Each Model ---

# For Logistic Regression
print("--- Tuning Logistic Regression ---")
grid_lr = GridSearchCV(estimator=lr, param_grid=lr_params, cv=5)
grid_lr.fit(X_train_scaled, y_train)
print(f"Best Parameters: {grid_lr.best_params_}")
print(f"Best CV Score: {grid_lr.best_score_:.4f}\n")

# For K-Nearest Neighbors
print("--- Tuning K-Nearest Neighbors ---")
grid_knn = GridSearchCV(estimator=knn, param_grid=knn_params, cv=5)
grid_knn.fit(X_train_scaled, y_train)
print(f"Best Parameters: {grid_knn.best_params_}")
print(f"Best CV Score: {grid_knn.best_score_:.4f}\n")

# For Random Forest
print("--- Tuning Random Forest ---")
grid_rf = GridSearchCV(estimator=rf, param_grid=rf_params, cv=5)
grid_rf.fit(X_train_scaled, y_train)
print(f"Best Parameters: {grid_rf.best_params_}")
print(f"Best CV Score: {grid_rf.best_score_:.4f}\n")