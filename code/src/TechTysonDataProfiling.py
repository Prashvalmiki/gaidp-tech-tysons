import pandas as pd 
file_path= input ("Enter the path:")
try:
    df=pd.read_csv(file_path)
    print("\n First 5 rows of the csv file:")
    print(df.head())

    print("\n column names in the CSV file:")
    print(df.columns)

    print(f"\n csv contains {df.shape[0]} rows and {df.shape[1]} column")

except Exception as e:
    print (f"Error: {e}")

