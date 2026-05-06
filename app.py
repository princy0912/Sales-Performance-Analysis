import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Performance Dashboard")
st.write("Superstore Sales Analysis using Python, Pandas & Matplotlib")

# Load Data
df = pd.read_csv("sales_data.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
avg_discount = df["Discount"].mean()

st.subheader("📌 Key Performance Indicators (KPIs)")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"{total_sales:.2f}")
col2.metric("Total Profit", f"{total_profit:.2f}")
col3.metric("Total Quantity", int(total_quantity))
col4.metric("Avg Discount", f"{avg_discount:.2f}")

# Category Analysis
st.subheader("📌 Category-wise Sales & Profit")
category_analysis = df.groupby("Category")[["Sales", "Profit"]].sum().sort_values(by="Sales", ascending=False)
st.dataframe(category_analysis)

# Region Analysis
st.subheader("📌 Region-wise Sales & Profit")
region_analysis = df.groupby("Region")[["Sales", "Profit"]].sum().sort_values(by="Sales", ascending=False)
st.dataframe(region_analysis)

# Profit Subcategories
st.subheader("✅ Top 5 Profit Making Sub-Categories")
profit_subcategory = df.groupby("Sub_Category")["Profit"].sum().sort_values(ascending=False).head(5)
st.dataframe(profit_subcategory)

# Loss Subcategories
st.subheader("❌ Top 5 Loss Making Sub-Categories")
loss_subcategory = df.groupby("Sub_Category")["Profit"].sum().sort_values().head(5)
st.dataframe(loss_subcategory)

# Chart 1: Category Sales
st.subheader("📊 Category-wise Sales Chart")
category_sales = df.groupby("Category")["Sales"].sum()

fig1, ax1 = plt.subplots()
ax1.bar(category_sales.index, category_sales.values)
ax1.set_title("Category-wise Total Sales")
ax1.set_xlabel("Category")
ax1.set_ylabel("Total Sales")
st.pyplot(fig1)

# Chart 2: Region Profit
st.subheader("📊 Region-wise Profit Chart")
region_profit = df.groupby("Region")["Profit"].sum()

fig2, ax2 = plt.subplots()
ax2.bar(region_profit.index, region_profit.values)
ax2.set_title("Region-wise Total Profit")
ax2.set_xlabel("Region")
ax2.set_ylabel("Total Profit")
st.pyplot(fig2)

# Chart 3: Discount vs Profit
st.subheader("📊 Discount vs Average Profit")
discount_profit = df.groupby("Discount")["Profit"].mean()

fig3, ax3 = plt.subplots()
ax3.plot(discount_profit.index, discount_profit.values, marker="o")
ax3.set_title("Discount vs Average Profit")
ax3.set_xlabel("Discount")
ax3.set_ylabel("Average Profit")
ax3.grid(True)
st.pyplot(fig3)

st.success("✅ Dashboard Generated Successfully!")