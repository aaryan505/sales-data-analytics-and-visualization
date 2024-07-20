# Sales over time
sales_data['month'] = sales_data['date'].dt.to_period('M')
sales_trend = sales_data.groupby('month')['sales_amount'].sum().reset_index()

# Plotting sales trends
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 6))
sns.lineplot(data=sales_trend, x='month', y='sales_amount')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)
plt.show()
