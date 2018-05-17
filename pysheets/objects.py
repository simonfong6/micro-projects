"""
Users
Equipment
"""

class User:
    def __init__(self,row):
        self.barcode = row[0]
        self.pid = row[1]
        self.first_name = row[2]
        self.last_name = row[3]
        self.class_name = row[4]
        self.ta = row[5]
        print('%s, %s, %s, %s, %s, %s' % (row[0],row[1],row[2],row[3], row[4], row[5]))
        
class Equipment:
     def __init__(self,row):
        self.date = row[0]
        self.first_name = row[1]
        self.last_name = row[2]
        self.pid = row[3]
        self.class_name = row[4]
        self.laptop_num = row[5]
        self.mouse_num = row[6]
        self.ta_sign = row[7]
        self.checked_in = row[8]
        self.checked_in = row[9]
