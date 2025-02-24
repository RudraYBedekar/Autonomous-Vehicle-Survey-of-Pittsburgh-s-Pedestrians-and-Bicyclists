# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Prompt the user to input the file path
file_name = r"C:\Users\rudra\OneDrive\Desktop\gmu syllabus\sem 1\infs 580\Bedekar_Last_project\avsurvey2019data.csv"  # Replace 'your_dataset.csv' with the path to your dataset file
data = pd.read_csv(file_name)

# Display the columns and the first few rows of the dataset
print("Columns in the dataset:")
print(data.columns)
print("\nFirst few rows:")
print(data.head())

# Data Cleaning
data = data.dropna(subset=['SafeAv', 'Age', 'SharedCyclist'])  # Drop rows with missing values
data = data[data['SharedCyclist'].isin(['Yes', 'No'])]  # Keep only rows where SharedCyclist is Yes or No
grouped_data = data.groupby(['Age', 'SharedCyclist'])['SafeAv'].mean().reset_index()  # Group and calculate mean

# Reshape the data for easier plotting
pivot_data = grouped_data.pivot(index='Age', columns='SharedCyclist', values='SafeAv')

# Visualize the data
plt.figure(figsize=(10, 6))
pivot_data.plot(kind='bar', figsize=(10, 6), color=['blue', 'orange'])
plt.title('Impact of Age and Cycling Experience on Perceptions of AVs')
plt.xlabel('Age Group')
plt.ylabel('Average Perception of AV Safety (SafeAv)')
plt.xticks(rotation=45)
plt.legend(title='Shared Cyclist Experience', labels=['No', 'Yes'])
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()