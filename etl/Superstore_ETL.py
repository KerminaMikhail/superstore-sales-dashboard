import pandas as pd 
#1 Extract - Load the dataset
data = pd.read_csv('Superstore_Dataset/Sample - Superstore.csv', encoding='latin1')
""" 
Explore Dataset:
# Display the first few rows of the dataset
print(data.head())
print("===============================================================================================")
# Check for missing values
print(data.isnull().sum())
print("===============================================================================================")
# Basic statistics of the dataset           
print(data.describe())
print("===============================================================================================")
# Group by 'Category' and calculate total sales
category_sales = data.groupby('Category')['Sales'].sum()
print(category_sales)
print("===============================================================================================")
# Group by 'Region' and calculate total sales
region_sales = data.groupby('Region')['Sales'].sum()
print(region_sales)
print("===============================================================================================")
# Group by 'Segment' and calculate total sales
segment_sales = data.groupby('Segment')['Sales'].sum()
print(segment_sales)
print("===============================================================================================")
# Group by 'Sub-Category' and calculate total sales
subcategory_sales = data.groupby('Sub-Category')['Sales'].sum()
print(subcategory_sales)
print("===============================================================================================")
# Group by 'State' and calculate total sales
state_sales = data.groupby('State')['Sales'].sum()
print(state_sales)
print("===============================================================================================")
# Group by 'City' and calculate total sales
city_sales = data.groupby('City')['Sales'].sum()
print(city_sales) """
#2 Transform Dataset:

data = data.drop_duplicates()
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Ship Date'] = pd.to_datetime(data['Ship Date'])
data['Order Year'] = data['Order Date'].dt.year
data['Order Month'] = data['Order Date'].dt.month
data['Shipping Days'] = (data['Ship Date'] - data['Order Date']).dt.days
data['Profit Margin'] = data['Profit'] / data['Sales']
#print(data.isnull().sum()) --> No missing values  
#print(data.duplicated().sum()) --> No duplicate values
#print(data.info()) --> Check data types and memory usage 
sales_region = data.groupby("Region")["Sales"].sum().reset_index()

sales_category = data.groupby("Category")["Sales"].sum().reset_index()

monthly_sales = data.groupby(
    ["Order Year", "Order Month"]
)["Sales"].sum().reset_index()

top_customers = data.groupby("Customer Name")["Sales"].sum().reset_index()
top_customers = top_customers.sort_values(by="Sales", ascending=False).head(10)

#3 LOAD

data.to_csv("clean_superstore.csv", index=False)
sales_region.to_csv("sales_by_region.csv", index=False)
sales_category.to_csv("sales_by_category.csv", index=False)
monthly_sales.to_csv("monthly_sales.csv", index=False)
top_customers.to_csv("top_customers.csv", index=False)

print("ETL completed successfully.")
print("Clean dataset shape:", data.shape)
data.to_csv("clean_superstore.csv", index=False)
