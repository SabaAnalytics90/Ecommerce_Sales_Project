# 📊 Interactive Supply Chain Sales Analytics Dashboard

A live, interactive data analytics dashboard built to monitor product performance, track sales distribution, and uncover high-value revenue drivers for business stakeholders.

🔗 **Live Dashboard Link:** [View Live Streamlit App](https://ecommercesalesproject-3ibosnua2smzadablakeiv.streamlit.app/)

---

## 🎯 Business Problem & Objective
In e-commerce and retail supply chains, stockouts of high-revenue items lead to direct financial losses, while overstocking low-performing goods ties up working capital. 

The objective of this project is to provide supply chain managers and stakeholders with real-time visibility into product sales performance, enabling them to:
* Identify top-performing products by revenue to prioritize inventory fulfillment.
* Filter and analyze sales metrics dynamically across different regions.
* Optimize stock allocation based on global demand patterns.

---

## 🛠️ Tech Stack & Skills Demonstrated
* **Data Processing & Analytics:** Python, Pandas
* **Data Visualization:** Plotly Express (Interactive Charts)
* **Web Deployment:** Streamlit, Streamlit Cloud
* **Version Control & DevOps:** Git, GitHub, CI/CD deployment workflows

---

## 💡 Key Business Insights Discovered
1. **The Core Revenue Driver:** *"Jam Making Set With Jars"* is identified as the highest revenue-generating product, accounting for maximum individual sales. From a supply chain perspective, this item requires strict safety stock monitoring to mitigate stockout risks.
2. **Regional Variations:** Sales density varies significantly across different countries, indicating that inventory placement should be localized closer to high-demand regions to optimize logistics costs and delivery speed.

---

## 📂 Project Structure
```text
ECOMMERCE_SALES_PROJECT/
├── Analysis/
│   └── sales_analysis.py       # Core data handling and exploration script
├── Dashboard/
│   └── Dashboard/
│       └── app.py              # Main Streamlit web application code
├── Data/                       # Raw and cleaned data storage
├── requirements.txt            # Production dependencies for cloud deployment
└── README.md                   # Professional project documentation