# Data Cleaning & Reporting Automation

## Overview

This project demonstrates an end-to-end **Data Cleaning, KPI Reporting, Visualization, and Dashboard Development** workflow using Python and Power BI. The objective is to automate the process of transforming raw retail transaction data into actionable business insights through data cleaning, reporting, and interactive dashboarding.

The project utilizes the **Online Retail II Dataset**, a real-world e-commerce dataset containing transactional records from a UK-based online retailer between December 2009 and December 2011.

---

## Project Objectives

* Automate data cleaning and preprocessing tasks
* Handle missing values and duplicate records
* Generate business KPIs automatically
* Create analytical visualizations using Python
* Export cleaned datasets and reports
* Develop an interactive Power BI dashboard
* Demonstrate a complete business intelligence workflow

---

## Dataset Information

**Dataset:** Online Retail II Dataset

### Features

| Column      | Description         |
| ----------- | ------------------- |
| Invoice     | Invoice Number      |
| StockCode   | Product Code        |
| Description | Product Description |
| Quantity    | Quantity Purchased  |
| InvoiceDate | Transaction Date    |
| Price       | Unit Price          |
| Customer ID | Customer Identifier |
| Country     | Customer Country    |

---

## Project Structure

```text
data-cleaning-reporting-automation/
│
├── automation/
│   └── data_cleaning.py
│
├── data/
│   └── online_retail_II.zip
│
├── reports/
│   ├── cleaned_online_retail.zip
│   └── kpi_report.csv
│
├── visuals/
│   ├── monthly_revenue.png
│   ├── revenue_by_country.png
│   └── top_products.png
│
├── dashboard/
│   └── Data_Cleaning_Reporting_Dashboard.pbix
│
└── README.md
```

---

## Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* OpenPyXL
* XlsxWriter

### Business Intelligence

* Power BI

### Development Environment

* Visual Studio Code
* Windows

---

## Data Cleaning Workflow

The automation script performs the following operations:

### Data Loading

* Loads the Online Retail II dataset into a Pandas DataFrame.

### Data Inspection

* Dataset shape analysis
* Data type validation
* Missing value identification
* Duplicate row detection

### Missing Value Handling

Removed records containing:

* Missing Product Description
* Missing Customer ID

### Duplicate Removal

Removed duplicate transactions to improve dataset quality and reliability.

### Feature Engineering

Created a new **Revenue** column:

```python
Revenue = Quantity * Price
```

### Data Export

Exports the cleaned dataset for reporting and dashboard development.

---

## KPI Reporting

The project automatically generates key business metrics.

### Generated KPIs

| KPI                 | Value                    |
| ------------------- | ------------------------ |
| Total Revenue       | £17.37M                  |
| Average Order Value | £469.98                  |
| Total Orders        | 36,969                   |
| Total Customers     | 5,878                    |
| Top Country         | United Kingdom           |
| Top Product         | REGENCY CAKESTAND 3 TIER |

Generated report:

```text
reports/kpi_report.csv
```

---

## Visualizations

### Monthly Revenue Trend

Analyzes revenue growth over time.

### Revenue by Country

Identifies the highest revenue-generating countries.

### Top Products by Revenue

Highlights products contributing the most revenue.

Generated visualization files:

```text
visuals/monthly_revenue.png
visuals/revenue_by_country.png
visuals/top_products.png
```

---

## Power BI Dashboard

An interactive Power BI dashboard was developed using the cleaned dataset.

### Dashboard Features

#### KPI Cards

* Total Revenue
* Average Order Value
* Total Orders
* Total Customers

#### Revenue Trend Analysis

* Monthly revenue trend visualization

#### Country Performance Analysis

* Revenue by country

#### Product Performance Analysis

* Top products by revenue

#### Interactive Filters

* Country Slicer
* Invoice Date Range Filter

---

## Dashboard Preview

<img width="100%" alt="Dashboard Preview" src="dashboard/dashboard_preview.png">

---

## Key Insights

### Revenue Performance

* Generated over **£17.37 Million** in total revenue.
* Strong revenue growth observed during peak sales periods.

### Geographic Analysis

* United Kingdom contributed the largest share of revenue.
* European countries represented the majority of international sales.

### Product Analysis

* REGENCY CAKESTAND 3 TIER emerged as the highest revenue-generating product.
* Decorative and gift-oriented products dominated overall sales.

### Customer Analysis

* More than **5,800 customers** contributed to transactions.
* Nearly **37,000 orders** were processed.

---

## Data Cleaning Results

### Before Cleaning

| Metric               | Value     |
| -------------------- | --------- |
| Rows                 | 1,067,371 |
| Columns              | 8         |
| Missing Customer IDs | 243,007   |
| Missing Descriptions | 4,382     |
| Duplicate Rows       | 34,335    |

### After Cleaning

| Metric         | Value   |
| -------------- | ------- |
| Rows           | 779,425 |
| Columns        | 9       |
| Missing Values | 0       |
| Revenue Column | Added   |

---

## How to Run

### Clone the Repository

```bash
git clone https://github.com/Arul-Prakash-m/data-cleaning-reporting-automation.git
```

### Navigate to Project Directory

```bash
cd data-cleaning-reporting-automation
```

### Install Dependencies

```bash
pip install pandas numpy matplotlib openpyxl xlsxwriter
```

### Run the Automation Script

```bash
python automation/data_cleaning.py
```

---

## Learning Outcomes

This project helped strengthen practical skills in:

* Data Cleaning and Preprocessing
* Exploratory Data Analysis (EDA)
* Business KPI Development
* Python Automation
* Data Visualization
* Power BI Dashboard Design
* Retail Analytics
* Business Intelligence Reporting
* Data-Driven Decision Making

---

## Author

**Arul Prakash M**

* LinkedIn: https://www.linkedin.com/in/arul-prakash-m
* GitHub: https://github.com/Arul-Prakash-m

---

## License

This project is intended for educational, learning, and portfolio purposes.
