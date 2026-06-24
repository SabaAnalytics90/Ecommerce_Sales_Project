# 📊 E-commerce Sales Performance & Insights Analysis

## 🎯 Project Overview
This project takes on the role of a Data Analyst to investigate an e-commerce sales dataset. The goal is to uncover hidden trends, identify high-value customer segments, and provide data-driven recommendations to boost overall profitability.

## 💼 The Business Problem & Objectives
This project will interrogate the dataset to answer three critical business questions:
1. **Product Performance:** Which product categories drive 80% of the revenue, and which items are lagging?
2. **Customer Behavior:** What is the average order value (AOV) and regional sales trends?
3. **Sales Metrics:** Which months or seasons show the highest sales peaks?

## 🛠️ Planned Tech Stack
* **Data Cleaning:** Google Sheets
* **Data Interrogation:** SQL Queries
* **Data Storytelling:** Dashboard Visualization

## 🧹 Data Cleaning & Standardisation

A structured data cleaning process was executed in Google Sheets to transform the raw, messy transaction records into a reliable dataset for business intelligence. Below is the documentation of the steps taken:

1. **Column Width & UI Adjustment:** Fixed text truncating errors, specifically in the `InvoiceDate` column, ensuring all tracking points are completely visible.
2. **Deduplication:** Identified and permanently removed duplicate transactional entries (e.g., duplicated rows for `HAND WARMER UNION JACK` and `JUMBO BAG TOY DESIGN`) to protect data integrity.
3. **Text Standardisation:** Standardised the text formatting of the `Country` column using text alignment and proper casing. Inconsistencies like `UNITED KINGDOM` and `united kingdom` were unified into a single corporate format: `United Kingdom`.
4. **Missing Values Imputation (Contextual Logic):**
   * **InvoiceNo:** Successfully recovered missing invoice numbers (Rows 4 and 13) by reverse-engineering nearby patterns (matching identical `CustomerID` and `InvoiceDate` metrics).
   * **CustomerID:** For transactions missing specific buyer IDs but retaining complete pricing and inventory metrics, the value was updated to `Guest` checkout to preserve revenue tracking data.
5. **Data Dropping (Risk Mitigation):** Safely removed incomplete data records where critical analysis metrics like `Quantity` or `UnitPrice` were missing entirely. This maintains structural precision and prevents downstream analytical errors.