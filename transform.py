import pandas as pd

def clean_customers(df):
    print("\nCleaning Customers Table................")

    df = df.drop_duplicates()
    age_map = {
        'teenager': 18,
        'adult': 30,
        'senior': 60}

    df['age'] = df['age'].astype(str).str.lower()

    df['age'] = df['age'].map(age_map)

    default_age=25
    df['age'] = df['age'].fillna(default_age)

    df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')

    return df


def clean_orders(df):
    print('\nCleaning Orders table.....................')
    df = df.drop_duplicates()
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    return df

def transform_mydata():
        
        customers = pd.read_csv(r'D:\MSBA\Datbase Systems\ETL Project New\data_processed\Cusomerinfo.csv')
        orders = pd.read_json(r'D:\MSBA\Datbase Systems\ETL Project New\data_processed\orders.json')
        delivery = pd.read_excel(r'D:\MSBA\Datbase Systems\ETL Project New\data_processed\delivery.xlsx')
        loyalty = pd.read_csv(r'D:\MSBA\Datbase Systems\ETL Project New\data_processed\loyalty_semicolon.csv', sep=';')
        ratings = pd.read_csv(r'D:\MSBA\Datbase Systems\ETL Project New\data_processed\Ratings.txt', sep='\t')
        
        customers=clean_customers(customers)
        orders=clean_orders(orders)

        print('\nCleaning Delivery Table...............')
        delivery['price']=pd.to_numeric(delivery['price'],errors='coerce')
        delivery['quantity']=pd.to_numeric(delivery['quantity'],errors='coerce')
        
        
        customers['city'] = customers['city'].replace("Isloo","Islamabad")
        orders['restaurant_name']=orders['restaurant_name'].replace("Khan Fried Chicken",'KFC')

        customers.to_csv(r'data_processed\cleaned_customers.csv', index=False)
        orders.to_csv(r'data_processed\cleaned_orders.csv', index=False)
        delivery.to_csv(r'data_processed\cleaned_delivery.csv', index=False)
        loyalty.to_csv(r'data_processed\cleaned_loyalty.csv', index=False)
        ratings.to_csv(r'data_processed\cleaned_ratings.csv', index=False)
        print('\nTransformation done.')


