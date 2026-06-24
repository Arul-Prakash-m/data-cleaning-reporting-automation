import matplotlib.pyplot as plt
import pandas as pd

# Load Dataset
file_path = r"C:\Users\roman\OneDrive\Desktop\Data-Cleaning-Reporting-Automation\data\online_retail_II.csv"

df = pd.read_csv(file_path)

# Data Cleaning
df = df.drop_duplicates()
df = df.dropna(subset=["Description"])
df = df.dropna(subset=["Customer ID"])
df = df[df["Quantity"] > 0]
df = df[df["Price"] > 0]

# Date Conversion
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Revenue Column
df["Revenue"] = df["Quantity"] * df["Price"]

# Export Cleaned Dataset
df.to_csv(
    r"C:\Users\roman\OneDrive\Desktop\Data-Cleaning-Reporting-Automation\reports\cleaned_online_retail.csv",
    index=False
)

# KPI Calculations
total_revenue = round(df["Revenue"].sum(), 2)

total_orders = df["Invoice"].nunique()

total_customers = df["Customer ID"].nunique()

top_country = (
    df.groupby("Country")["Revenue"]
      .sum()
      .idxmax()
)

top_product = (
    df.groupby("Description")["Revenue"]
      .sum()
      .idxmax()
)

# KPI Report
kpi_report = pd.DataFrame({
    "Metric": [
        "Total Revenue",
        "Total Orders",
        "Total Customers",
        "Top Country",
        "Top Product"
    ],
    "Value": [
        total_revenue,
        total_orders,
        total_customers,
        top_country,
        top_product
    ]
})

# Save KPI Report
kpi_report.to_csv(
    r"C:\Users\roman\OneDrive\Desktop\Data-Cleaning-Reporting-Automation\reports\kpi_report.csv",
    index=False
)

print("KPI Report Generated Successfully!")
print(kpi_report)
# Revenue by Country Chart

country_revenue = (
    df.groupby("Country")["Revenue"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10, 5))

country_revenue.plot(kind="bar")

plt.title("Top 10 Countries by Revenue")

plt.xlabel("Country")

plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig(
    r"C:\Users\roman\OneDrive\Desktop\Data-Cleaning-Reporting-Automation\visuals\revenue_by_country.png"
)

plt.close()

print("\nRevenue by Country chart saved successfully!")

# Monthly Revenue Trend

df["YearMonth"] = df["InvoiceDate"].dt.to_period("M")

monthly_revenue = (
    df.groupby("YearMonth")["Revenue"]
      .sum()
)

plt.figure(figsize=(12,5))

monthly_revenue.plot(kind="line")

plt.title("Monthly Revenue Trend")

plt.xlabel("Month")

plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig(
    r"C:\Users\roman\OneDrive\Desktop\Data-Cleaning-Reporting-Automation\visuals\monthly_revenue.png"
)

plt.close()

print("Monthly Revenue chart saved successfully!")

# Top Products by Revenue

top_products = (
    df.groupby("Description")["Revenue"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(12,6))

top_products.plot(kind="bar")

plt.title("Top 10 Products by Revenue")

plt.xlabel("Product")

plt.ylabel("Revenue")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig(
    r"C:\Users\roman\OneDrive\Desktop\Data-Cleaning-Reporting-Automation\visuals\top_products.png"
)

plt.close()

print("Top Products chart saved successfully!")
