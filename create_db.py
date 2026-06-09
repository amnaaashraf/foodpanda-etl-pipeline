import sqlite3
import pandas as pd
from pathlib import Path

def create_database():
    # Database file
    db_path = Path("data_warehouse/warehouse.db")

    # Connect to SQLite
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # ---- LOAD CLEANED CSV FILES ----
    customers = pd.read_csv('data_processed/cleaned_customers.csv')
    orders = pd.read_csv('data_processed/cleaned_orders.csv')
    delivery = pd.read_csv('data_processed/cleaned_delivery.csv')
    loyalty = pd.read_csv('data_processed/cleaned_loyalty.csv')
    ratings = pd.read_csv('data_processed/cleaned_ratings.csv')

    # ---- MERGE delivery info into orders ----
    orders = pd.merge(
        orders,delivery[['order_id','quantity','price','payment_method']],
        on='order_id',
        how='left'
    )

    # ---- CREATE TABLES ----
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id TEXT PRIMARY KEY,
            gender TEXT,
            age INTEGER,
            city TEXT,
            signup_date TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            customer_id TEXT,
            order_date TEXT,
            restaurant_name TEXT,
            dish_name TEXT,
            category TEXT,
            quantity INTEGER,
            price REAL,
            payment_method TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS loyalty (
            customer_id TEXT PRIMARY KEY,
            order_frequency INTEGER,
            last_order_date TEXT,
            loyalty_points INTEGER,
            churned TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ratings (
            order_id TEXT PRIMARY KEY,
            customer_id TEXT,
            rating REAL,
            rating_date TEXT
        )
    """)

    # ---- INSERT DATA INTO TABLES ----
    customers.to_sql('customers', conn, if_exists='replace', index=False)
    orders.to_sql('orders', conn, if_exists='replace', index=False)
    loyalty.to_sql('loyalty', conn, if_exists='replace', index=False)
    ratings.to_sql('ratings', conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()

    print("✅ SQLite Database created successfully with merged orders and delivery info!")

if __name__ == "__main__":
    create_database()
