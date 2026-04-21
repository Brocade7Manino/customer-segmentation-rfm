# customer-segmentation-rfm
# Customer Segmentation & RFM Analysis (E-Commerce)

## Project Overview
This project analyzes e-commerce transaction data using two complementary approaches:

1. SQL – Basic business queries (top customers, monthly revenue, top products)  
2. Python (pandas) – Full RFM scoring & customer segmentation (VIP / Loyal / At Risk / Regular)

Goal: Understand customer value and purchasing patterns to support data-driven decisions.

---

## Tech Stack
Python– pandas, matplotlib (RFM scoring & segmentation)
SQL – aggregation, sorting, date formatting
Tableau– dashboard (top products, monthly revenue, RFM distribution)

---

## Files in This Repo

| File | Description |
|------|-------------|
| `Data Cleaning.py` | Data cleaning script: handling missing values, removing outliers, formatting dates. |
| `rfm_segmentation_SQL.sql` | Basic business queries: top 10 customers by spend, monthly revenue trend, top 10 products by quantity sold. |
| `rfm_segmentation_python.py` | Full RFM analysis: Recency / Frequency / Monetary scoring (quintiles), customer segmentation (VIP, Loyal, At Risk, Regular), and bar chart visualization. |
| `Customer Analysis Dashboard.pdf` | Static export of Tableau dashboard (or link to interactive version). |

---

## SQL Queries (Quick Business Insights)
Top Customers – Identify high-spending customers  
Monthly Revenue – Track revenue trends over time  
Top Products – Find best-selling products by volume  

These queries can be run directly on the cleaned dataset to get fast answers.

---

## Python RFM Segmentation (Deeper Customer Analysis)

### RFM Definition
Recency (R) – Days since last purchase (lower = better)  
Frequency (F) – Number of unique orders (higher = better)  
Monetary (M) – Total money spent (higher = better)  

### Scoring & Segmentation Logic
- Each metric is ranked and divided into 5 quintiles (1 = lowest, 5 = highest)  
- R_score: higher is better (recent) → labels `[5,4,3,2,1]`  
- F_score & M_score: higher is better → labels `[1,2,3,4,5]`  

**Segmentation rules:**
| Segment | Condition |
|---------|-----------|
| VIP | R_score ≥4 AND F_score ≥4 AND M_score ≥4 |
| Loyal | R_score ≥3 AND F_score ≥3 |
| At Risk | R_score ≤2 |
| Regular | Others |

### Output
- Each customer gets R/F/M scores + a segment label  
- Bar chart showing segment distribution

---

##  Tableau Dashboard
The dashboard includes:
- Top products by revenue  
- Customer monthly revenue trend  
- RFM customer distribution  

---

##  How to Use
1. Data cleaning – Run `Data Cleaning.py` first to prepare the dataset.  
2. SQL queries – Execute `rfm_segmentation_SQL.sql` on the cleaned table.  
3. Python RFM – Run `rfm_segmentation_python.py` for segmentation.  
4. Dashboard – Open the PDF or Tableau link.

---

## About Me
Statistics student with a focus on data analysis.  
Skilled in Python, SQL, and Tableau.  
Seeking Data Analyst Internship opportunities (2026).
Contact: yunyy6137@gmail.com

---

## Note
This project is for portfolio purposes. Data is anonymized/simulated.
