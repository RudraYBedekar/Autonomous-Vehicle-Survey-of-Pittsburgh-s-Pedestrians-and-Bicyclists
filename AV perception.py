# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Prompt the user to input the CSV file path
file_name = r"C:\Users\rudra\OneDrive\Desktop\gmu syllabus\sem 1\infs 580\Bedekar_Last_project\avsurvey2019data.csv"  # Replace 'your_dataset.csv' with the path to your dataset file
data = pd.read_csv(file_name)

# Required columns
columns = ['SafeAv', 'Age', 'Speed25Mph', 'SchoolZoneManual']

# Check for missing columns
if not all(col in data.columns for col in columns):
    missing_cols = [col for col in columns if col not in data.columns]
    raise ValueError(f"Missing columns in the dataset: {missing_cols}")

# Data Cleaning: Drop rows with missing values
filtered_data = data.dropna(subset=columns)

# Encode categorical columns
filtered_data['Age_Encoded'] = filtered_data['Age'].astype('category').cat.codes
filtered_data['Speed25Mph_Encoded'] = filtered_data['Speed25Mph'].astype('category').cat.codes
filtered_data['SchoolZoneManual_Encoded'] = filtered_data['SchoolZoneManual'].astype('category').cat.codes

# Define features (AA) and target variable (BB)
AA = filtered_data[['Age_Encoded', 'Speed25Mph_Encoded', 'SchoolZoneManual_Encoded']]
BB = filtered_data['SafeAv']

# Split data into training and testing sets
AA_train, AA_test, BB_train, BB_test = train_test_split(AA, BB, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(AA_train, BB_train)

# Make predictions on the test set
BB_pred = model.predict(AA_test)

# Visualize observed vs. predicted data
plt.figure(figsize=(10, 6))
plt.scatter(range(len(BB_test)), BB_test, color='blue', alpha=0.6, label='Observed Data')
plt.scatter(range(len(BB_pred)), BB_pred, color='red', alpha=0.6, label='Predicted Data')
plt.title('Perceptions of Safety as Observed and Predicted')
plt.xlabel('Data Points')
plt.ylabel('Perception of AV Safety (1–5)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Calculate and display the R-squared score
r2 = r2_score(BB_test, BB_pred)
print(f"R-squared score: {r2}")