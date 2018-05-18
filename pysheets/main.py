#!/env/bin/python2
# main.py
# Handles the logic of the code.
"""
Equipment Checkout System

"""
import datetime
from sheets import GoogleSheets
from objects import User, Users, Equipment

EQUIPMENT_SHEET = 'Equipment'
USERS_SHEET = 'Users'

def read_users(sheets):
    RANGE_NAME = '{}!A2:F'.format(USERS_SHEET)
    values = sheets.read(RANGE_NAME)
    users = Users()
    if not values:
        print('No data found.')
    else:
        for row in values:
           user = User(row)
           users.insert(user)
    return users

def checkout(sheets,users,first_empty_row):
    student_barcode = raw_input("Scan student barcode: ")
    if(not users.barcode_registered(student_barcode)):
        print("You are not a registered user.")
        return
    student_user = users.get_user(student_barcode)
    
    
    laptop = raw_input("Scan laptop barcode (Optional):")
    mouse = raw_input("Scan mouse barcode (Optional):")
    ta_barcode = raw_input("Scan TA barcode: ")

    if(not users.barcode_registered(ta_barcode)):
        print("You are not a registered user.")
        return

    ta_user = users.get_user(ta_barcode) 
    if(not users.is_TA(ta_user)):
        print("You are not a TA.")
        return
        
    date = str(datetime.date.today())
    first_name = student_user.first_name
    last_name = student_user.last_name
    pid = student_user.pid
    class_name = student_user.class_name
    laptop_num = laptop
    mouse_num = mouse
    ta_name = ta_user.first_name
    checked_out_time = str(datetime.datetime.now().time())
    checked_in_time = None

    
    start = 'A' 
    end = 'I' 
    RANGE_NAME = ('%s!%s%d:%s%d' % (EQUIPMENT_SHEET,start,first_empty_row,end,
                                       first_empty_row))
    values = [
        [date, first_name, last_name, pid, class_name, laptop_num, 
            mouse_num,ta_name,checked_out_time],
    ]
    
    sheets.write(RANGE_NAME,values)
    print("{} checked out laptop {}.".format(first_name,laptop_num))
    
def checkin(sheets,users):
    # Col length 10
    checkout_values = read_checkout(sheets)
    #print(checkout_values)
    print("Checking in items")
    laptop = raw_input("Scan laptop barcode (Optional):")
    mouse = raw_input("Scan mouse barcode (Optional):")
    
    i = 1
    for row in checkout_values:
        i += 1
        # Laptop,5 Mouse,6
        if(laptop != ''):
            if(row[5] == laptop):
                if(len(row) < 10):
                    cell = 'J' 
                    RANGE_NAME = ('%s!%s%d' % (EQUIPMENT_SHEET,cell,i))
                    values = [
                        [str(datetime.datetime.now().time())]
                    ]
                    sheets.write(RANGE_NAME,values)
                    print("{} checked in laptop {}.".format(row[1],laptop))
                    break
                    
                    
            
        
    
    
def read_checkout(sheets):
    range_name = EQUIPMENT_SHEET + '!A2:J'
    return sheets.read(range_name)
    

if(__name__ == '__main__'):
    SPREADSHEET_ID = '1YKvM7jLvfbd4IGIYuyKHki_DES9LBhomOz_tdvuPbYo'
    sheets = GoogleSheets(SPREADSHEET_ID)
    
    users = read_users(sheets)
           
    while(True):
        print("Choose what you wanna do:")
        print("1. Checkout")
        print("2. Checkin")
        cmd = raw_input("Command: ")
        one = cmd == '1'
        two = cmd == '2'
        if(not one and not two):
            print("Not a valid command. Please choose available.")
            continue
            
        if(one):
            print("Running Checkout:")
            checkout_values = read_checkout(sheets)
            length = 0
            if(checkout_values is not None):
                length = len(checkout_values)
            first_empty_row = length + 2    #Defined by us
            checkout(sheets,users,first_empty_row)
            continue
        if(two):
            print("Running Checkin:")
            checkin(sheets,users)
            continue
            
        print("You have gone to a weird place.")

