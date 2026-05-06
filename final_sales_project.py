import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("sales_data.csv")

print("===== SALES DATA ANALYSIS PROJECT =====")

# -------------------------------
# 1. Basic Data Understanding
# -------------------------------
print("\nDataset Shape (Rows, Columns):", df.shape)
print("\nColumns:\n", df.columns)

# -------------------------------
# 2. Data Cleaning
# -------------------------------
print("\nDuplicate Rows Before:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
print("Duplicate Rows After:", df.duplicated().sum())

# -------------------------------
# 3. KPI Summary
# -------------------------------
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
avg_discount = df["Discount"].mean()

print("\n===== KPI SUMMARY =====")
print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Quantity Sold:", int(total_quantity))
print("Average Discount:", round(avg_discount, 2))

# -------------------------------
# 4. Category-wise Sales and Profit
# -------------------------------
category_analysis = df.groupby("Category")[["Sales", "Profit"]].sum().sort_values(by="Sales", ascending=False)

print("\n===== CATEGORY WISE SALES & PROFIT =====")
print(category_analysis)

# -------------------------------
# 5. Sub-Category Wise Sales (Top 10)
# -------------------------------
subcat_sales = df.groupby("Sub_Category")["Sales"].sum().sort_values(ascending=False).head(10)

print("\n===== TOP 10 SUB-CATEGORIES BY SALES =====")
print(subcat_sales)

# -------------------------------
# 6. Region Wise Sales and Profit
# -------------------------------
region_analysis = df.groupby("Region")[["Sales", "Profit"]].sum().sort_values(by="Sales", ascending=False)

print("\n===== REGION WISE SALES & PROFIT =====")
print(region_analysis)

# -------------------------------
# 7. State Wise Profit (Top 10)
# -------------------------------
state_profit = df.groupby("State")["Profit"].sum().sort_values(ascending=False).head(10)

print("\n===== TOP 10 STATES BY PROFIT =====")
print(state_profit)

# -------------------------------
# 8. City Wise Sales (Top 10)
# -------------------------------
city_sales = df.groupby("City")["Sales"].sum().sort_values(ascending=False).head(10)

print("\n===== TOP 10 CITIES BY SALES =====")
print(city_sales)

# -------------------------------
# 9. Segment Wise Sales
# -------------------------------
segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)

print("\n===== SEGMENT WISE SALES =====")
print(segment_sales)

# -------------------------------
# 10. Discount Impact on Profit
# -------------------------------
discount_profit = df.groupby("Discount")["Profit"].mean().sort_index()

print("\n===== DISCOUNT VS AVERAGE PROFIT =====")
print(discount_profit)

# -------------------------------
# 11. Best Ship Mode (Sales Based)
# -------------------------------
shipmode_sales = df.groupby("Ship Mode")["Sales"].sum().sort_values(ascending=False)

print("\n===== SHIP MODE WISE SALES =====")
print(shipmode_sales)

# -------------------------------
# 12. Profit Margin Column
# -------------------------------
df["Profit Margin"] = (df["Profit"] / df["Sales"]) * 100

print("\nProfit Margin Column Added Successfully!")

# -------------------------------
# 13. Highest Profit Product Category
# -------------------------------
highest_profit_category = category_analysis["Profit"].idxmax()
highest_profit_value = category_analysis["Profit"].max()

print("\n===== HIGHEST PROFIT CATEGORY =====")
print("Category:", highest_profit_category)
print("Profit:", round(highest_profit_value, 2))

# -------------------------------
# Loss Making Sub-Categories
# -------------------------------
loss_subcategory = df.groupby("Sub_Category")["Profit"].sum().sort_values().head(5)

print("\n===== TOP 5 LOSS MAKING SUB-CATEGORIES =====")
print(loss_subcategory)

# Save loss report
loss_subcategory.to_csv("loss_subcategory_report.csv")
print("\nLoss report saved as loss_subcategory_report.csv")

# -------------------------------
# Top Profit Making Sub-Categories
# -------------------------------
profit_subcategory = df.groupby("Sub_Category")["Profit"].sum().sort_values(ascending=False).head(5)

print("\n===== TOP 5 PROFIT MAKING SUB-CATEGORIES =====")
print(profit_subcategory)

# Save profit report
profit_subcategory.to_csv("profit_subcategory_report.csv")
print("\nProfit report saved as profit_subcategory_report.csv")

print("\n===== BUSINESS RECOMMENDATIONS =====")

print("1. Focus more on high-profit sub-categories to increase overall revenue.")
print("2. Reduce discounts on loss-making sub-categories because high discount impacts profit negatively.")
print("3. Improve pricing strategy for products with negative profit margin.")
print("4. Focus marketing on top-performing regions and cities for better sales growth.")
print("5. Analyze loss-making states/sub-categories for supply chain and cost optimization.")

# -------------------------------
# 14. Export Reports
# -------------------------------
category_analysis.to_csv("category_analysis_report.csv")
region_analysis.to_csv("region_analysis_report.csv")
df.to_csv("cleaned_sales_data.csv", index=False)

print("\n===== FILES EXPORTED SUCCESSFULLY =====")
print("1. cleaned_sales_data.csv")
print("2. category_analysis_report.csv")
print("3. region_analysis_report.csv")

print("\n===== PROJECT COMPLETED SUCCESSFULLY =====")