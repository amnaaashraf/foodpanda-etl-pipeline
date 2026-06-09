import sqlite3
from pathlib import Path

def generate_summary():

    db_path = Path("data_warehouse/warehouse.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    summary = "\n====== SQL SUMMARY REPORT ======\n\n"

    queries = {

        "Total Orders from Islamabad": """
            SELECT COUNT(*) 
            FROM orders o
            JOIN customers c ON o.customer_id = c.customer_id
            WHERE c.city = 'Islamabad';
        """,

        "Average Rating": """
            SELECT ROUND(AVG(rating),2) FROM ratings;
        """,

        "Total Revenue": """
            SELECT ROUND(SUM(quantity * price),2) FROM orders;
        """,

        "Top 5 Most Ordered Dishes": """
            SELECT dish_name, COUNT(*) 
            FROM orders
            GROUP BY dish_name 
            ORDER BY 2 DESC
            LIMIT 5;
        """,

        "Sales By City": """
            SELECT c.city, ROUND(SUM(o.quantity * o.price),2)
            FROM orders o
            JOIN customers c ON o.customer_id = c.customer_id
            GROUP BY c.city
            ORDER BY 2 DESC;
        """,

        "Orders By City": """
            SELECT c.city, COUNT(o.order_id)
            FROM orders o
            JOIN customers c ON o.customer_id = c.customer_id
            GROUP BY c.city
            ORDER BY 2 DESC;
        """,

        "Top 5 Customers By Spend": """
            SELECT c.customer_id, ROUND(SUM(o.quantity*o.price),2)
            FROM orders o
            JOIN customers c ON o.customer_id = c.customer_id
            GROUP BY c.customer_id
            ORDER BY 2 DESC
            LIMIT 5;
        """,

        "Churn Analysis": """
            SELECT churned, COUNT(*) 
            FROM loyalty
            GROUP BY churned;
        """,

        "Monthly Order Trend": """
            SELECT substr(order_date, 1, 7) AS month, COUNT(order_id)
            FROM orders
            GROUP BY month
            ORDER BY month;
        """,

        "Category Performance": """
            SELECT category, COUNT(order_id)
            FROM orders
            GROUP BY category
            ORDER BY 2 DESC;
        """, 
        "sir task ":"""SELECT *
        FROM delivery
        """

    }

    # Run each SQL query
    for title, sql in queries.items():
        cursor.execute(sql)
        rows = cursor.fetchall()

        summary += f"\n--- {title} ---\n"
        
        for row in rows:
            summary += str(row) + "\n"

    conn.close()

    # Save report
    Path("outputs").mkdir(exist_ok=True)
    report_file = Path("outputs/sql_summary_report.txt")

    with open(report_file, "w") as f:
        f.write(summary)

    print("✅ SQL Summary Report Created:")
    print(report_file)
    


if __name__ == "__main__":
    generate_summary()
