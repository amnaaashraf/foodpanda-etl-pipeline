# Foodpanda ETL Pipeline & SQL Analytics

## Overview
End-to-end ETL pipeline built in Python on a food delivery dataset.
Covers data extraction, cleaning, transformation, loading into a
SQLite relational warehouse, and SQL-based business analytics.

## Tools & Technologies
- Python (Pandas, NumPy)
- SQLite / SQL
- JSON, Excel, TXT parsing

## Pipeline Steps
| Step | Script | What it does |
|------|--------|--------------|
| 1 | create_errors.py | Simulates real-world messy data |
| 2 | split_data.py | Splits dataset into multiple formats |
| 3 | clean_data.py | Fixes nulls, types, duplicates, formatting |
| 4 | create_db.py | Loads clean data into SQLite warehouse |
| 5 | generate_summary.py | Runs SQL queries for business insights |

## Key SQL Insights Generated
- Total orders and revenue
- Revenue by city
- Top performing restaurants
- Average customer rating
- Churn rate analysis

## How to Run
```python
python main.py
```

## Folder Structure
ETL-Project/
├── data_raw/
├── data_processed/
├── data_warehouse/
├── scripts/
└── main.py

## Course
Database Systems — MS Business Analytics, FAST-NUCES