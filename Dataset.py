import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_name = r"C:\Users\rudra\OneDrive\Desktop\gmu syllabus\infs 580\avsurvey2019data.csv"  # Replace 'your_dataset.csv' with the path to your dataset file
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

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Prompt the user to input the file path
file_name = r"C:\Users\rudra\OneDrive\Desktop\gmu syllabus\infs 580\avsurvey2019data.csv"

# Read the CSV file
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


# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Prompt the user to input the CSV file path
file_name = r"C:\Users\rudra\OneDrive\Desktop\gmu syllabus\infs 580\avsurvey2019data.csv"

# Read the CSV file
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
