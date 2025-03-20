import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression


# Function to train the model
def train_model(data, model_type='random_forest'):
    # Ensure the input data is in the correct format
    data = data.astype(np.float64)


    X = data.drop("target", axis=1)  # Features
    y = data["target"]  # Target variable
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    if model_type == 'random_forest':
        model = RandomForestClassifier()
    elif model_type == 'svm':
        model = SVC()
    elif model_type == 'logistic_regression':
        model = LogisticRegression()

    model.fit(X_train, y_train)
    
    return model

def predict(model, input_data):
    """
    Predicts the kilocalories burned based on user input and provides exercise recommendations.
    """
    prediction = model.predict(input_data)
    
    # Provide exercise recommendations based on the prediction
    if prediction[0] < 2000:
        recommendation = "Consider light exercises like walking or yoga."
    elif 2000 <= prediction[0] < 3000:
        recommendation = "Moderate exercises like jogging or cycling are recommended."
    else:
        recommendation = "Engage in vigorous exercises like running or high-intensity workouts."
    
    return prediction, recommendation

    """
    Predicts the kilocalories burned based on user input.
    """
    return model.predict(input_data)
