from os import system
import time
import ui.main as ui
import csv

def call_add_customer():
    ui.print_header()
    print('Add Customer')
    print()
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    address = input("Address: ")
    email = input("Email: ")

    fields = ['first_name', 'last_name', 'address', 'email']
    rows = [[first_name, last_name, address, email]]

    with open("data/customers.csv", 'a') as csvfile:
       # creating a csv writer object  
       csvwriter = csv.writer(csvfile) 

       if csvfile.tell() == 0:
           # writing the fields  
           csvwriter.writerow(fields)

       # writing the data rows  
       csvwriter.writerows(rows)
    
    system("clear")
    print("New customer added")
    time.sleep(3)


def call_edit_customer():
    pass

def call_find_customer():
    pass

def call_delete_customer():
    pass