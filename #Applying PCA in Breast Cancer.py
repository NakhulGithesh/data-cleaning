# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer # type: ignore

# Load the breast cancer dataset from sklearn
breast = load_breast_cancer()

# Extract features and labels
breast_data = breast.data               # Shape: (569, 30)
breast_labels = breast.target          # Shape: (569,)

# Reshape labels to make it a column (569, 1)
labels = np.reshape(breast_labels, (569, 1))

# Combine data and labels into one array (569, 31)
final_breast_data = np.concatenate([breast_data, labels], axis=1)

# Create a pandas DataFrame
breast_dataset = pd.DataFrame(final_breast_data)

# Set column names: 30 feature names + 1 label column
features = breast.feature_names
features_labels = np.append(features, 'label')
breast_dataset.columns = features_labels

# Replace numerical labels with string labels for clarity
# 0 = Malignant, 1 = Benign (according to sklearn documentation)
breast_dataset['label'].replace(0, 'Malignant', inplace=True)
breast_dataset['label'].replace(1, 'Benign', inplace=True)

'''# View the first few rows of the dataset
print(breast_dataset.head())

print(breast_dataset.columns)
print(breast_dataset.isnull().sum())

# Saveing the cleaned dataset to an Excel file
breast_dataset.to_excel('cleaned_breast_cancer_data.xlsx', index=False)'''
































#showing the graphs
#Load the Excel file
df = pd.read_excel(r'C:\Users\Lenovo\OneDrive\Documents\intern\cleaned_breast_cancer_data.xlsx')


# Debugging: Print all column names in the DataFrame
print("Columns in the DataFrame:", df.columns.tolist())

# Update column names if necessary
texture_columns = ['mean texture', 'se texture', 'worst texture']  # Adjust based on actual column names
smoothness_columns = ['mean smoothness', 'se smoothness', 'worst smoothness']
area_columns = ['mean area', 'se area', 'worst area']

# Check if columns exist before calculating averages
for col in texture_columns + smoothness_columns + area_columns:
    if col not in df.columns:
        print(f"Column '{col}' is missing in the DataFrame.")

# First, let's see all the column names we have
print("All columns in the data:")
print(df.columns.tolist())

# Define the exact column names we want to use
# (Replace these with the actual column names from your printout)
texture_columns = ['mean texture', 'se texture', 'worst texture']
smoothness_columns = ['mean smoothness', 'se smoothness', 'worst smoothness']
area_columns = ['mean area', 'se area', 'worst area']

# Calculate averages
texture_vals = [df[col].mean() for col in texture_columns]
smoothness_vals = [df[col].mean() for col in smoothness_columns]
area_vals = [df[col].mean() for col in area_columns]

# Prepare for plotting
group_names = ['Mean', 'SE', 'Worst']  # Just the labels for the x-axis
bar_width = 0.25
x_positions = np.arange(len(group_names))  # Positions for the bars

# Create the plot
plt.figure(figsize=(10, 6))

plt.bar(x_positions - bar_width, texture_vals, width=bar_width, label='Texture', color='blue')
plt.bar(x_positions, smoothness_vals, width=bar_width, label='Smoothness', color='orange')
plt.bar(x_positions + bar_width, area_vals, width=bar_width, label='Area', color='green')

# Add labels and title
plt.xlabel('Measurement Type')
plt.ylabel('Average Value')
plt.title('Average Texture, Smoothness and Area Measurements')
plt.xticks(x_positions, group_names)
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()