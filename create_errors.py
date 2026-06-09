
def generate_error(df):
    print("Generating Errors",'.'*10)
    df['age'] = df['age'].replace("Teenager", "twenty")
    df['city'] = df['city'].replace("Islamabad", "Isloo")
    df['restaurant_name']=df['restaurant_name'].replace('KFC',"Khan Fried Chicken")
    df.to_csv('data_processed\FoodPandaWithErrors.csv')
    return df



    
