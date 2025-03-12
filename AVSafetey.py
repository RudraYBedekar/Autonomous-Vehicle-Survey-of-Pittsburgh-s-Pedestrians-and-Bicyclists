import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_name = r"C:\Users\rudra\OneDrive\Desktop\gmu syllabus\sem 1\infs 580\Bedekar_Last_project\avsurvey2019data.csv"
data = pd.read_csv(file_name)

# Display the column names (already done in your output, just for reference)
print(data.columns)

# Assuming we are using 'SafeAv' as a safety score and grouping by 'FamiliarityTech'
grouped_data = data.groupby('FamiliarityTech')['SafeAv'].mean().reset_index()

# Creating a pie chart to visualize the average safety scores based on technological familiarity
plt.figure(figsize=(8, 8))
plt.pie(grouped_data['SafeAv'], labels=grouped_data['FamiliarityTech'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(range(len(grouped_data))))
plt.title('Average Safety Perception by Technological Familiarity')
plt.show()
