
#import pandas as pd
from google.oauth2 import service_account
import gspread

#gmail to add to google doc
#infographic-generator@infographic-generator.iam.gserviceaccount.com

#Retusn the total value of sales
def total(sheet):
    sheet_info = sheet.get_worksheet(0)
    product_amount = sheet_info.col_values(2)
    can_total = 0
    for x in product_amount:

        try:
            can_total = can_total + int(x)
        except:
            pass
    return can_total

def main():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive.file',
             'https://www.googleapis.com/auth/drive']

    # Reading Credentails
    credentials = service_account.Credentials.from_service_account_file('infographic-generator-a3267a9c8df0.json', scopes=scope)

    gc = gspread.authorize(credentials)

    #Open Sheet
    sheet1 = gc.open('MV-January')

    try:
        sheet_info = sheet1.get_worksheet(0)
    except:
        print('Error Occurred, Sheet could not open')
        return

    print(total(sheet1))
    

    return

if __name__ == '__main__':
    main()