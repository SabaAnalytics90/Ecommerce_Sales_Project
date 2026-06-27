import pandas as pd
import streamlit as st

# Set professional page configuration
st.set_page_config(page_title="E-commerce Executive Dashboard", layout="wide")

# Title of the Dashboard
st.title("📊 E-Commerce Sales Performance Dashboard")
st.markdown("---")

# Load the cleaned dataset
clean_file = "Data/cleaned_sales_data.csv"
df = pd.read_csv(clean_file)

# ---------------------------------------------------------
# SECTION 1: TOP-LEVEL KEY PERFORMANCE INDICATORS (KPIs)
# ---------------------------------------------------------
st.header("📈 Key Performance Indicators")
col1, col2, col3 = st.columns(3)

# KPI 1: Total Revenue
total_revenue = df['Total_Revenue'].sum()
col1.metric(label="Total Revenue Generated", value=f"${total_revenue:,.2f}")

# KPI 2: Total Units Sold
total_units = df['Quantity'].sum()
col2.metric(label="Total Units Sold", value=f"{total_units:,}")

# KPI 3: Average Unit Price
avg_price = df['UnitPrice'].mean()
col3.metric(label="Average Unit Price", value=f"${avg_price:,.2f}")

st.markdown("---")

# ---------------------------------------------------------
# SECTION 2: CORE BUSINESS INSIGHTS (TABLES)
# ---------------------------------------------------------
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📦 Top Products by Revenue")
    top_products = df.groupby('Description New ')['Total_Revenue'].sum().sort_values(ascending=False).head(5)
    # Convert to standard DataFrame for clean visualization
    top_products_df = top_products.reset_index().rename(columns={'Description New ': 'Product Description', 'Total_Revenue': 'Revenue ($)'})
    st.dataframe(top_products_df, width='stretch')

with col_right:
    st.subheader("🌍 Geographic Revenue Distribution")
    country_revenue = df.groupby('Country ')['Total_Revenue'].sum().sort_values(ascending=False)
    country_df = country_revenue.reset_index().rename(columns={'Country ': 'Country', 'Total_Revenue': 'Revenue ($)'})
    st.dataframe(country_df, width='stretch')