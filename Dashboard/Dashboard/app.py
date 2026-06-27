import pandas as pd
import streamlit as st
import plotly.express as px

# Set professional page configuration
st.set_page_config(page_title="E-commerce Executive Dashboard", layout="wide")

# Title of the Dashboard
st.title("📊 E-Commerce Sales Performance Dashboard")
st.markdown("---")

# Load the cleaned dataset
clean_file = "Data/cleaned_sales_data.csv"
df = pd.read_csv(clean_file)

# ---------------------------------------------------------
# SIDEBAR: DYNAMIC FILTERS
# ---------------------------------------------------------
st.sidebar.header("🔍 Filter Options")
# Get unique list of countries
countries = sorted(df['Country '].unique())
selected_country = st.sidebar.selectbox("Select Country", ["All Countries"] + countries)

# Filter dataset based on selection
if selected_country != "All Countries":
    filtered_df = df[df['Country '] == selected_country]
else:
    filtered_df = df

# ---------------------------------------------------------
# SECTION 1: TOP-LEVEL KEY PERFORMANCE INDICATORS (KPIs)
# ---------------------------------------------------------
st.header("📈 Key Performance Indicators")
col1, col2, col3 = st.columns(3)

total_revenue = filtered_df['Total_Revenue'].sum()
col1.metric(label="Total Revenue Generated", value=f"${total_revenue:,.2f}")

total_units = filtered_df['Quantity'].sum()
col2.metric(label="Total Units Sold", value=f"{total_units:,}")

avg_price = filtered_df['UnitPrice'].mean()
col3.metric(label="Average Unit Price", value=f"${avg_price:,.2f}")

st.markdown("---")

# ---------------------------------------------------------
# SECTION 2: CHARTS & VISUALIZATION
# ---------------------------------------------------------
st.header("📊 Sales Analytics Charts")

# Chart 1: Top 10 Products Bar Chart
st.subheader("📦 Top 10 Products by Revenue")
top_products = filtered_df.groupby('Description New ')['Total_Revenue'].sum().sort_values(ascending=False).head(10).reset_index()
top_products.columns = ['Product Description', 'Revenue ($)']

fig_products = px.bar(top_products, x='Revenue ($)', y='Product Description', 
                     orientation='h', color='Revenue ($)',
                     color_continuous_scale='Viridis')
fig_products.update_layout(yaxis={'categoryorder':'total ascending'}, height=400)
st.plotly_chart(fig_products, use_container_width=True)