# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC  # Support Vector Classifier
from sklearn.metrics import accuracy_score

# --- 1. Data Preparation ---
df = pd.read_csv('Social_Network_Ads.csv')
X = df[['Age', 'EstimatedSalary']]
y = df['Purchased']

# --- 2. Train-Test Split ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# --- 3. Feature Scaling (Crucial for SVM) ---
# SVMs are sensitive to the scale of features, so scaling is a very important step.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# --- 4. SVM Model Training and Prediction ---
model = SVC(kernel='rbf', random_state=42)

# Train the model on the scaled training data
model.fit(X_train_scaled, y_train)

# Make predictions on the unseen scaled test data
y_pred = model.predict(X_test_scaled)

# --- 5. Evaluate the Model ---
# Check the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"SVM Model Accuracy: {accuracy:.4f}")