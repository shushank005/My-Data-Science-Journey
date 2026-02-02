# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline  
from sklearn.metrics import accuracy_score

# --- 1. Data Preparation ---
df = pd.read_csv('Social_Network_Ads.csv')
X = df[['Age', 'EstimatedSalary']]
y = df['Purchased']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# --- 2. Define the Pipeline Steps ---
steps = [
    ('scaler', StandardScaler()),              
    ('classifier', LogisticRegression())       
]

# --- 3. Create the Pipeline ---
pipeline = Pipeline(steps)

# --- 4. Train the Entire Pipeline ---
pipeline.fit(X_train, y_train)

# --- 5. Make Predictions ---
y_pred = pipeline.predict(X_test)

# --- 6. Evaluate the Pipeline ---
accuracy = accuracy_score(y_test, y_pred)
print(f"Pipeline Accuracy: {accuracy:.4f}")