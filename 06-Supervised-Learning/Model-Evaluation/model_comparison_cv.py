# Import necessary libraries
import pandas as pd
from sklearn.model_selection import cross_val_score  # Imports the function for cross-validation
from sklearn.preprocessing import StandardScaler        # Imports the tool for feature scaling
from sklearn.linear_model import LogisticRegression   # Imports the Logistic Regression model
from sklearn.neighbors import KNeighborsClassifier    # Imports the KNN model
from sklearn.ensemble import RandomForestClassifier   # Imports the Random Forest model

# --- 1. Data Loading ---
# Load the dataset from the CSV file into a pandas DataFrame
df = pd.read_csv('Social_Network_Ads.csv')

# --- 2. Feature Selection ---
# Select the columns 'Age' and 'EstimatedSalary' as our features (input variables)
X = df[['Age', 'EstimatedSalary']]
# Select the 'Purchased' column as our target (what we want to predict)
y = df['Purchased']

# --- 3. Feature Scaling ---
# Create an instance of the StandardScaler
scale = StandardScaler()
# Fit the scaler to the data and transform it, so all features have a similar scale.
X_scaled = scale.fit_transform(X)

# --- 4. Model Definition ---
# Define all the machine learning models we want to compare
model1 = LogisticRegression()
model2 = KNeighborsClassifier(n_neighbors=7)
model3 = RandomForestClassifier(n_estimators=100) # n_estimators=100 means it will build 100 decision trees

# Create lists to hold the models and their names for easy looping
models = [model1, model2, model3]
model_names = ["Logistic Regression", "KNN (K=7)", "Random Forest"]

print("--- Comparing Model Performance with 10-Fold Cross-Validation ---")
# --- 5. Cross-Validation Loop ---
# Loop through each model to perform cross-validation and print its score
for i, model in enumerate(models):
    # Perform 10-fold cross-validation (cv=10).
    # This splits the data into 10 parts, trains on 9, and tests on 1, repeating 10 times.
    scores = cross_val_score(model, X_scaled, y, cv=10)
    
    # --- 6. Print Results ---
    # Print the name of the current model
    print(f"\nModel: {model_names[i]}")
    # Print the average accuracy across all 10 folds
    print(f"Average Accuracy: {scores.mean():.4f}")
    # Print the standard deviation, which shows how consistent the model's performance is
    print(f"Stability (Std Dev): {scores.std():.4f}")