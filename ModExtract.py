import pandas as pd
import os 

# function which reads the csv file
def read_csv_file(file_path):
    df = pd.read_csv(file_path)
    return df

# check if the column names are present in the csv file
def check_column_names(df, column_names):
    for column_name in column_names:
        if column_name not in df.columns:
            print(f"The column {column_name} is not present in the csv file.")
            return False
    return True


# if the column is present in the csv file, take them and store them in a new csv file
def store_column_data(df, column_names, filename):
    column_data = df[column_names]
    column_data.to_csv(filename, index=False)

def delete_file(sourcefile):
    if os.path.exists(sourcefile):
        os.remove(sourcefile)
        print("file deleted")


# mainexecute function which takes the file path and column names as arguments,
def main_execute(sourcefile, desiredcolumns, targetfile):
        # delete_file(sourcefile)
        if os.path.exists(sourcefile):
            df = read_csv_file(sourcefile)
            columns_OK = check_column_names(df, desiredcolumns)
            if columns_OK:
                store_column_data(df, desiredcolumns, targetfile)
                print(f"Data stored successfully: {targetfile}")
            else:
                print("Error: The column names are not present in the csv file.")
        else:
            print("File does not exist")


