# import important library
import pandas as pd
from sklearn.model_selection import cross_val_score,GridSearchCV,train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC


# --- Data Preparation ---

df = pd.read_csv('Social_Network_Ads.csv')

X = df[['Age', 'EstimatedSalary']]

y = df['Purchased']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# --- Define and Create the Pipeline ---
pipeline_svm=Pipeline([
    ('scaler',StandardScaler()),
    ('classifier4',SVC(random_state=42))
])

# --- Parameter Grid for Pipeline ---
param_grid_svm={
    'classifier4__C':[0.1, 1, 10, 100],

    'classifier4__gamma':[1, 0.1, 0.01, 0.001]
}

# --- GridSearchCV with Pipeline ---
grid_search_svm=GridSearchCV(estimator=pipeline_svm,param_grid=param_grid_svm,cv=5, verbose=2)

# --- Train the Entire Pipeline ---
grid_search_svm.fit(X_train,y_train)

# --- find best estimator ---
best_model=grid_search_svm.best_estimator_

# --- Make Predictions ---
y_pred=best_model.predict(X_test)

# --- apply accuracy to check statbility of model ---
accuracy=accuracy_score(y_test,y_pred)

print(accuracy)