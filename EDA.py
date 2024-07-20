# Summary statistics
print(sales_data.describe())

# Total sales
total_sales = sales_data['sales_amount'].sum()
print(f"Total Sales: {total_sales}")

# Sales by region
sales_by_region = sales_data.groupby('region')['sales_amount'].sum().reset_index()
print(sales_by_region)

# Sales by product category
sales_by_category = sales_data.groupby('product_category')['sales_amount'].sum().reset_index()
print(sales_by_category)
