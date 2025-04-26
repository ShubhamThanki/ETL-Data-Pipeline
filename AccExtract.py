import csv
import random
    
# for loop to generate 100 records and write it to csv file
def writearray(account_path, header):
        arr_acc_name = ['shubham','nishil','dhaval','vishal']
        arr_billing_adress_line1 = ['kaliyabid','shyamal','chaaya','bokhira']
        arr_billing_city = ['ahmedabad','surat','rajkot','jamnagar']
        arr_billing_state = ['gujarat','maharastra','rajasthan','punjab']
        arr_shipping_state = ['delhi','karnatak','rajasthan','punjab']
        arr_shipping_address_line1 = ['kaliyabid','shyamal','sagwadi','bokhira']
        arr_shipping_city = ['ahmedabad','surat','rajkot','jamnagar']
        arr_interest = ['sports','music','reading','']   
        with open(account_path , "w",newline='') as file:
                writer = csv.writer(file) # assign the file to the writer
                writer.writerow(header)
                for i in range(1,101):
                        cust_id = i
                        acc_name = random.choice(arr_acc_name) 
                        billin_address_line1 = random.choice(arr_billing_adress_line1)
                        billin_city = random.choice(arr_billing_city)
                        billin_state = random.choice(arr_billing_state)
                        ship_state = random.choice(arr_shipping_state)
                        ship_address_line1 = random.choice(arr_shipping_address_line1)
                        ship_city = random.choice(arr_shipping_city)
                        interest = random.choice(arr_interest)
                        records  = [
                                        cust_id, acc_name, billin_address_line1, billin_city, billin_state, ship_state, ship_address_line1, ship_city, interest
                       ]
                        writer.writerow(records)
        print("csv file created successfully")
                


