# -*- coding: utf-8 -*-
"""medicalApp.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J2_mzdWxAq3MwAIiIRxjQZ_SbgNWJNfU
"""

!pip install streamlit
!pip install pyngrok

# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from joblib import dump  # Import joblib to save models

# Load your dataset
data = pd.read_excel('/content/MEDICALaID.xlsx')  # Adjust the path as necessary

# Prepare your features and target variable
X = data.drop('PremiumPrice', axis=1)
y = data['PremiumPrice']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a scaler and scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the Random Forest model
model = RandomForestRegressor()
model.fit(X_train_scaled, y_train)

# Save the model and scaler
dump(model, 'random_forest_model.joblib')
dump(scaler, 'scaler.joblib')

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import pandas as pd
# import numpy as np
# import streamlit as st
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.preprocessing import StandardScaler
# from joblib import load
# 
# # Load the trained model and scaler
# model = load('random_forest_model.joblib')
# scaler = load('scaler.joblib')
# 
# # Function to calculate BMI
# def calculate_bmi(weight, height):
#     return weight / (height / 100) ** 2
# 
# # Streamlit app layout
# st.title("Medical Insurance Premium Predictor")
# 
# # User inputs
# age = st.number_input("Age", min_value=0, max_value=120, value=30)
# diabetes = st.selectbox("Diabetes (1 if Yes, 0 if No)", [0, 1])
# blood_pressure = st.selectbox("Blood Pressure Problems (1 if Yes, 0 if No)", [0, 1])
# transplants = st.selectbox("Any Transplants (1 if Yes, 0 if No)", [0, 1])
# chronic_diseases = st.selectbox("Any Chronic Diseases (1 if Yes, 0 if No)", [0, 1])
# height = st.number_input("Height (cm)", min_value=0, max_value=250, value=175)
# weight = st.number_input("Weight (kg)", min_value=0, max_value=300, value=70)
# allergies = st.selectbox("Known Allergies (1 if Yes, 0 if No)", [0, 1])
# cancer_history = st.selectbox("History of Cancer in Family (1 if Yes, 0 if No)", [0, 1])
# surgeries = st.number_input("Number of Major Surgeries", min_value=0, value=0)
# 
# # When the button is clicked
# if st.button("Predict Premium Price"):
#     # Calculate BMI
#     bmi = calculate_bmi(weight, height)
# 
#     # Create the input array for prediction
#     new_data = np.array([[age, diabetes, blood_pressure, transplants, chronic_diseases,
#                           height, weight, allergies, cancer_history, surgeries, bmi]])
# 
#     # Scale the new data
#     new_data_scaled = scaler.transform(new_data)
# 
#     # Predict the premium price
#     premium_prediction = model.predict(new_data_scaled)
#     st.success(f'Predicted Premium Price: ${premium_prediction[0]:.2f}')
#

