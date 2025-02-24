import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_name = r"C:\Users\rudra\OneDrive\Desktop\gmu syllabus\sem 1\infs 580\Bedekar_Last_project\avsurvey2019data.csv"  # Replace 'your_dataset.csv' with the path to your dataset file
data = pd.read_csv(file_name)

# Preview the dataset
print("Columns in the dataset:")
print(data.columns)
print("\nFirst few rows:")
print(data.head())

# Data Cleaning
data = data.dropna(subset=['SafeAv', 'SharedCyclist', 'SharedPedestrian'])

# Grouping and Aggregation
grouped_data = data.groupby(['SharedCyclist', 'SharedPedestrian']).agg({
    'SafeAv': 'mean'
}).reset_index()

# Creating an Infrastructure column for visualization
grouped_data['Infrastructure'] = grouped_data['SharedCyclist'] + " + " + grouped_data['SharedPedestrian']

# Visualization
plt.figure(figsize=(10, 6))
sns.barplot(x='Infrastructure', y='SafeAv', data=grouped_data, palette='viridis')
plt.title('Comfort Levels of Cyclists and Pedestrians')
plt.xlabel('Type of Infrastructure (Pedestrian and Cyclist)')
plt.ylabel('Typical Level of Comfort')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


