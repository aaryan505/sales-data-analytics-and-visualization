# Sales by region
plt.figure(figsize=(10, 6))
sns.barplot(data=sales_by_region, x='region', y='sales_amount')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)
plt.show()

# Sales by product category
plt.figure(figsize=(10, 6))
sns.barplot(data=sales_by_category, x='product_category', y='sales_amount')
plt.title('Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)
plt.show()
