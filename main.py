import random 
import csv
import AccExtract as AE
import ModExtract as ME
import connec_db as DB
import DriveApiConnect as GDrive
import datetime
import handle_values as HV
import EmailConnect as EC
import pandas as pd
import os
import mysql.connector
import random
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive



# main function 
def main(): 
    # created a header for the csv file
    header = ['cust_id', 'acc_name','billin_city', 'billin_address_line1', 'billin_state', 'ship_state', 'ship_address_line1', 'ship_city', 'interest']
    account_path = r'E:\DATA ANALYSIS\PYTHON\Chapter 1\account.csv'
    AE.writearray(account_path, header)
    billing_path = r'E:\DATA ANALYSIS\PYTHON\Chapter 1\billing.csv'
    shipping_path = r'E:\DATA ANALYSIS\PYTHON\Chapter 1\shipping.csv'


    # calling the billing.py and shipping.py file
    column_names_billing = ["billin_address_line1", "billin_city", "billin_state"]
    column_names_shipping = ["ship_address_line1", "ship_city", "ship_state"]

    ME.main_execute(account_path, column_names_shipping , shipping_path)
    ME.main_execute(account_path, column_names_billing , billing_path)

    # calling the account.py file
    conn = DB.connect_to_mysql()
    if conn:
        # Check for missing values and get clean data
        clean_rows, header,filename = HV.check_and_log_missing_values(account_path)

        # Load clean data into the database
        if clean_rows:
            HV.load_clean_data_to_db(clean_rows, header, "account", conn)

        conn.close()
    GDrive.upload_to_gdrive(account_path)


    if filename:
        # Send the missing rows file via email
        EC.send_error_file_via_email(filename, "shubhamfifa12@gmail.com", "krkh ywpx xrli fxqg" , "shubham.thanki12@gmail.com")
    else:
        print("⚠️ No missing rows file to send via email.")

# main function call
if __name__ == "__main__":
    main()
    





