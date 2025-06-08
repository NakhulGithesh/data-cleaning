import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel(r'C:\Users\Lenovo\OneDrive\Documents\intern\final_datasheet.xlsx')

# Ensure column names are stripped of extra spaces
df.columns = df.columns.str.strip()

# Filling unknown values in 'Account Number Xcellence' and 'Supplier Reference-Xcellence'
df['Account Number Xcellence'] = df['Account Number Xcellence'].fillna('Unknown')
df['Supplier Reference-Xcellence'] = df['Supplier Reference-Xcellence'].fillna('Unknown')

# Grouping data by 'Supplier Reference-Xcellence' and saving to Excel
grouped = df.groupby('Supplier Reference-Xcellence', as_index=False)['Amount (AED)'].sum()
grouped.to_excel('grouped_data.xlsx', index=False)

# Print column names and check for missing values
print(df.columns)
print(df.isnull().sum())


# Filling unknown values in 'DR/CR', 'Account Number Xcellence', and 'Supplier Reference-Xcellence'
df['DR / CR'] = df['DR / CR'].fillna('Unknown')
df['Account Number Xcellence'] = df['Account Number Xcellence'].fillna('Unknown')
df['Supplier Reference-Xcellence'] = df['Supplier Reference-Xcellence'].fillna('Unknown')
df['Currency'] = df['Currency'].fillna('AED')
df['Account Name'] = df['Account Name'].fillna('Unknown')

grouped = df.groupby('Supplier Reference-Xcellence', as_index=False)['Amount (AED)'].sum()
grouped.to_excel('grouped_data.xlsx', index=False)
df.columns = df.columns.str.strip()
print(df.columns)
plt.show()

# saving the cleaned data to a new Excel file
df.to_excel('cleaned_final_datasheet.xlsx', index=False)

#indexing the data
print(df['Supplier Reference-Xcellence'].value_counts())
print(df.iloc[0:5 , 2:3])
print(df.isnull().sum())

# Identifies outliers in the 'Account Number Xcellence' column using the Interquartile Range (IQR) method.
column_name = 'Account Number Xcellence'
df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
Q1 = df[column_name].quantile(0.25)
Q3 = df[column_name].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df[column_name] < lower_bound) | (df[column_name] > upper_bound)]
print('outliers in AC_No:-', outliers)

# Ensure column names are stripped of extra spaces and formatted
df.columns = df.columns.str.strip().str.replace(' ', '_')
df['Amount_(AED)'] = pd.to_numeric(df['Amount_(AED)'].str.replace(',', ''), errors='coerce')
df['Account_Name'] = df['Account_Name'].fillna('Unknown')
grouped_account = df.groupby('Account_Name', as_index=False).agg(Avg_Amount=('Amount_(AED)', 'mean'))
grouped_account = grouped_account.dropna(subset=['Avg_Amount'])

# Plotting the bar chart
plt.figure(figsize=(12, 6))
plt.bar(grouped_account['Account_Name'], grouped_account['Avg_Amount'], color='skyblue')
plt.xlabel("Account Name", fontsize=12)
plt.ylabel("Average Amount Spent (AED)", fontsize=12)
plt.title("Average Amount Spent per Account Name", fontsize=14)
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

# Pie chart
import pandas as pd
import matplotlib.pyplot as plt

# Ensure 'Amount (AED)' is numeric
grouped['Amount (AED)'] = pd.to_numeric(grouped['Amount (AED)'].str.replace(',', ''), errors='coerce')

# Prepare data for the pie chart
grouped = grouped.sort_values(by='Amount (AED)', ascending=False)
top_suppliers = grouped.head(5)  # Top 5 suppliers
others = pd.DataFrame([{
    'Supplier Reference-Xcellence': 'Others',
    'Amount (AED)': grouped['Amount (AED)'][5:].sum()
}])
grouped = pd.concat([top_suppliers, others], ignore_index=True)

# Plot the pie chart
plt.figure(figsize=(8, 8))
plt.pie(
    grouped['Amount (AED)'], 
    labels=grouped['Supplier Reference-Xcellence'], 
    autopct='%1.1f%%', 
    textprops={'fontsize': 8}
)
plt.title("Top 5 Suppliers + Others", fontsize=14)
plt.axis('equal')
plt.tight_layout()
plt.show()





# Extract the top 5 suppliers based on their total 'Amount (AED)'
top_suppliers = df.groupby('Supplier Reference-Xcellence')['Amount (AED)'].sum().nlargest(5).index

# Filter the data for the top 5 suppliers
filtered_data = df[df['Supplier Reference-Xcellence'].isin(top_suppliers)]

# Add a 'Month' column for grouping
filtered_data['Month'] = filtered_data['Voucher_Date'].dt.to_period('M')

# Group by 'Month' and 'Supplier_Reference-Xcellence', then pivot for stacking
filtered_grouped = filtered_data.groupby(['Month', 'Supplier Reference-Xcellence'])['Amount (AED)'].sum().unstack().fillna(0)

# Plot the stacked area chart
filtered_grouped.plot(kind='area', figsize=(12, 6), alpha=0.7)
plt.title("Monthly Total Amount for Top 5 Suppliers", fontsize=14)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Total Amount (AED)", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend(title="Supplier", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


print('hello world')