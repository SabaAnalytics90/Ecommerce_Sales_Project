import pandas as pd

# Define the dataset paths
clean_file = "Data/cleaned_sales_data.csv"

# Load the cleaned dataset
df = pd.read_csv(clean_file)

print("=============================================")
print("        E-COMMERCE BUSINESS PERFORMANCE      ")
print("=============================================\n")

# KPI 1: Total Revenue
total_revenue = df['Total_Revenue'].sum()
print(f"💰 Total Revenue Generated: ${total_revenue:,.2f}")

# KPI 2: Top Products by Revenue
top_products = df.groupby('Description New ')['Total_Revenue'].sum().sort_values(ascending=False).head(5)
print("\n📦 Top 5 Products by Revenue Generation:")
for product, revenue in top_products.items():
    print(f" - {product.strip()}: ${revenue:,.2f}")

# KPI 3: Geographic Revenue Distribution
country_revenue = df.groupby('Country ')['Total_Revenue'].sum().sort_values(ascending=False)
print("\n🌍 Revenue Contribution by Country:")
for country, revenue in country_revenue.items():
    print(f" - {country.strip()}: ${revenue:,.2f}")
print("=============================================")