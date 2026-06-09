def split_my_data(df):
    customer_info=df[['customer_id','gender','age','city','signup_date']]
    print('\nGenerating the Customer Info csv File\n')
    customer_info.to_csv(r'data_processed\Cusomerinfo.csv')

    orders = df[['order_id','order_date','customer_id','restaurant_name','dish_name','category']]
    print('\nGenerating the Orders Json File\n')
    orders.to_json(r'data_processed\orders.json', orient='records', lines=False)

    delivery = df[['order_id','delivery_status','quantity','price','payment_method']]
    print('\nGenerating the delivery Excel File\n')
    delivery.to_excel(r'data_processed\delivery.xlsx', index=False)

    loyalty = df[['customer_id','order_frequency','last_order_date','loyalty_points','churned']]
    loyalty.to_csv(r'data_processed\loyalty_semicolon.csv', sep=';', index=False)
    print('\nGenerating the Loyalty csv File\n')

    ratings = df[['customer_id','rating','rating_date']]
    ratings.to_csv(r'data_processed\Ratings.txt', sep='\t', index=False)
    print('\nGenerating the Rating txt File\n')

    print('Split files created in data_processed')
    return df
