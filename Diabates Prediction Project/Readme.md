DIABETES PREDICTION

# One-Line Overview :

A smart system that employs Machine Learning (SVM) in analyzing medical data to predict whether a patient has diabetes.

# Objective : 

The objective of this project is to develop a system that can assist a doctor in identifying whether a patient has diabetes by looking for patterns in the patient’s health statistics.

# Technical Flow :

- Data: Load patient data (Glucose, BMI, Age, etc.).

- Clean: Scale the numbers so they are all in a similar range (Standardization).

- Split: Split the data 80% to train the model and 20% to test how smart it is.

- Train: Train the SVM Algorithm to draw a mathematical "line" (hyperplane) that separates healthy patients from diabetic patients.

- Predict: Use the model to predict an instant "Yes" or "No" answer for new patient data.
