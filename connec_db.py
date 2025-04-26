import mysql.connector
import pandas as pd

def connect_to_mysql(): 
    try:
        conn = mysql.connector.connect(
            host="localhost",       # or "127.0.0.1"
            user="root",            # default user for XAMPP/WAMP
            password="",            # default is empty
            database="test"         # replace with your DB name
        )
        if conn.is_connected():
            print("✅ Connected to MySQL successfully!")
            return conn 
            
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
        return None

# create a function to load the data 
def load_csv_to_mysql(file_path, table_name, connection):
    try:
        # Read the CSV file into a DataFrame
        data = pd.read_csv(file_path)
        
        # Insert data into the MySQL table
        cursor = connection.cursor()
        for _, row in data.iterrows():
            # Static INSERT query (ensure the column names match your table structure)
                query = f"""
                    INSERT INTO {table_name} (cust_id, acc_name, billin_city, billin_address_line1, 
                                          billin_state, ship_state, ship_address_line1, 
                                          ship_city, interest) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                cursor.execute(query, (
                    row['cust_id'], 
                    row['acc_name'], 
                    row['billin_city'], 
                    row['billin_address_line1'], 
                    row['billin_state'], 
                    row['ship_state'], 
                    row['ship_address_line1'], 
                    row['ship_city'], 
                    row['interest']
            ))
        connection.commit()
        print(f"✅ Data from {table_name} loaded into table '{table_name}' successfully!")
    except Exception as e:
        print(f"❌ Error loading data: {e}")
    finally:
        cursor.close()


connection = connect_to_mysql()
if connection:
    connection.close()





