import csv
import random
from datetime import datetime
import pandas as pd
import mysql.connector

def check_and_log_missing_values(csv_file_path):
    rows_with_missing_data = []
    rows_without_missing_data = []

    try:
        # Read the CSV file
        with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)

            for row in reader:
                if any(cell.strip() == "" for cell in row):  # Check for empty/blank values
                    rows_with_missing_data.append(row)
                else:
                    rows_without_missing_data.append(row)

        # If any rows with missing values exist
        if rows_with_missing_data:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"missing_rows_{timestamp}.txt"

            with open(filename, mode='w', encoding='utf-8') as f:
                f.write(",".join(header) + "\n")  # write header
                for row in rows_with_missing_data:
                    f.write(",".join(row) + "\n")

            print(f"⚠️ Found {len(rows_with_missing_data)} rows with missing values.")
            print(f"📝 Missing rows saved to: {filename}")
        else:
            print("✅ No missing values found in the CSV file.")

        # Return rows without missing values
        return rows_without_missing_data, header, filename

    except FileNotFoundError:
        print("❌ File not found. Please check the file path.")
        return [], []
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return [], []

def load_clean_data_to_db(rows_without_missing_data, header, table_name, connection):
    try:
        cursor = connection.cursor()
        # Generate the INSERT query dynamically based on the header
        columns = ", ".join(header)
        placeholders = ", ".join(["%s"] * len(header))
        query = f"""
                INSERT INTO {table_name} (cust_id, acc_name, billin_city, billin_address_line1, 
                                          billin_state, ship_state, ship_address_line1, 
                                          ship_city, interest) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
        
        # Insert rows into the database
        for row in rows_without_missing_data:
                cursor.execute(query, row)

        connection.commit()
        print(f"✅ Clean data loaded into table '{table_name}' successfully!")
    except Exception as e:
        print(f"❌ Error loading clean data: {e}")
    finally:
        cursor.close()