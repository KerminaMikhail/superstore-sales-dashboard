# Superstore Sales Analysis Dashboard

This project performs **end-to-end sales analysis** using **Python for ETL (Extract, Transform, Load)** and **Power BI for interactive visualization**.
The goal is to analyze product performance, regional sales distribution, customer profitability, and monthly sales trends.

---

## Project Overview

This project demonstrates a simple **data analytics pipeline**:

1. **Extract**

   * Load the Superstore dataset using Python.

2. **Transform**

   * Remove duplicates
   * Convert date columns
   * Create new analytical features:

     * Order Year
     * Order Month
     * Shipping Days
     * Profit Margin

3. **Load**

   * Export cleaned datasets for reporting in Power BI.

4. **Visualization**

   * Build an interactive dashboard for business insights.

---

## Dashboard Preview

images/dashboard_preview.png
---

## Key Insights

• Technology generates the highest sales.
• West region leads overall revenue.
• Phones and Chairs are the top-selling sub-categories.
• Some customers generate **high sales but negative profit**.

---

## Tech Stack

* Python
* Pandas
* NumPy
* Power BI

---

## Project Structure

superstore-sales-dashboard/

data/ → raw and processed datasets
etl/ → Python ETL pipeline
dashboard/ → Power BI dashboard (.pbix)
images/ → dashboard screenshots

requirements.txt → Python dependencies
README.md → project documentation

---

## Dataset

This project uses the **Superstore Sales dataset**.

Download it from Kaggle:

https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

After downloading, place the dataset inside the **data/** folder.

---

## How to Run the Project

Install dependencies:

pip install -r requirements.txt

Run the ETL pipeline:

python etl/superstore_etl.py

Open the Power BI dashboard:

dashboard/superstore_dashboard.pbix

---

## Author

**Kermina Mikhail**
Aspiring Data Analyst
=======
# superstore-sales-dashboard
Sales analytics dashboard using Python ETL and Power BI
>>>>>>> 215c22c25c7ceab81ee2b769accf602d2b024e25
