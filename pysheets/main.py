#!/env/bin/python2
# main.py
# Handles the logic of the code.
"""
Equipment Checkout System

"""
from sheets import GoogleSheets
from objects import User, Equipment

if(__name__ == '__main__'):
    SPREADSHEET_ID = '1YKvM7jLvfbd4IGIYuyKHki_DES9LBhomOz_tdvuPbYo'
    sheets = GoogleSheets(SPREADSHEET_ID)
    
    RANGE_NAME = 'Users!A2:F'
    values = sheets.read(RANGE_NAME)
    users = {}
    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
           user = User(row)
           users[user.barcode] = user
           
    while(True):
       
        student = raw_input("Scan student barcode: ")
        if(student not in users):
            print("You are not a registered user.")
            continue
        
        
        laptop = raw_input("Scan laptop barcode (Optional):")
        mouse = raw_input("Scan mouse barcode (Optional):")
        ta = raw_input("Scan TA barcode: ")

        if(ta not in users):
            print("You are not a registered user.")
            continue

        ta_user = users[ta] 
        if(ta_user.ta != 'yes'):
            print("You are not a TA.")
            continue

        RANGE_NAME = 'Sheet1!A2:D2'
        values = [
            [student, laptop, mouse, ta],
        ]
        
        sheets.write(RANGE_NAME,values)

