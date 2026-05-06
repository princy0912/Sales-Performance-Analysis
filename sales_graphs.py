import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_sales_data.csv")

# 1) Category-wise Sales
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(7,5))
plt.bar(category_sales.index, category_sales.values)
plt.title("Category-wise Total Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.savefig("category_sales.png")
plt.show()

# 2) Region-wise Profit
region_profit = df.groupby("Region")["Profit"].sum()

plt.figure(figsize=(7,5))
plt.bar(region_profit.index, region_profit.values)
plt.title("Region-wise Total Profit")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.savefig("region_profit.png")
plt.show()

# 3) Discount vs Average Profit
discount_profit = df.groupby("Discount")["Profit"].mean()

plt.figure(figsize=(7,5))
plt.plot(discount_profit.index, discount_profit.values, marker="o")
plt.title("Discount vs Average Profit")
plt.xlabel("Discount")
plt.ylabel("Average Profit")
plt.grid(True)
plt.savefig("discount_vs_profit.png")
plt.show()