"""
Shows basic usage of the Sheets API. Prints values from a Google Spreadsheet.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

class GoogleSheets:
    def __init__(self,spreadsheet_id,
                      credentials='credentials.json',
                      secret = 'client_secret.json'):
        # Setup the Sheets API              
        self.scopes = 'https://www.googleapis.com/auth/spreadsheets'
        self.spreadsheet_id = spreadsheet_id
        store = file.Storage(credentials)
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(secret, self.scopes)
            creds = tools.run_flow(flow, store)
        service = build('sheets', 'v4', http=creds.authorize(Http()))
        self.spreadsheet = service.spreadsheets().values()
    
    def read(self,range_name):
        request = self.spreadsheet.get(spreadsheetId=self.spreadsheet_id,
                                       range=range_name)
        result = request.execute()
        values = result.get('values', [])
        
        if not values:
            print('No data found.')
            return None
        else:
            for row in values:
                # Print all columns
                for elem in row:
                    #print(elem)
                    pass
        return values
     
    def write(self,range_name,
                   values,
                   value_input_option = 'USER_ENTERED'):
        body = {
            'values': values
        }
        request = self.spreadsheet.update(spreadsheetId=self.spreadsheet_id, 
                                          range=range_name,
                                          valueInputOption=value_input_option,
                                          body=body)
        result = request.execute()
        num_updated = result.get('updatedCells')
        #print('{0} cells updated.'.format(num_updated));
        return num_updated
        



       


            
    
    
def main():
    import objects
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
           user = objects.User(row)
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

if(__name__ == '__main__'):
    main()
