from load_main import load_raw                  #Loading Dataset
from generate_errors import generate_error      #Generating Manual Errors
from split_data import split_my_data            #Spliting Single Datafile into different format 
from extract import extract_my_data             #Extracting Data from different sources (E)
from transform import transform_mydata          #Transfromation (T)
from merge import merge_mydata                  #Merging all 
from create_dbcopy import create_database
from generate_summary_copy import generate_summary
def main():
    file_path=r"D:\MSBA\Datbase Systems\ETL Project New\data_raw\Foodpanda Analysis Dataset.csv"
    df=load_raw(file_path)
    df=generate_error(df)
    df=split_my_data(df)
    extract_my_data()
    transform_mydata()
    merge_mydata()
    create_database()
    generate_summary()
    print(' ETL Done!!')

    

if __name__ == "__main__":
    main()