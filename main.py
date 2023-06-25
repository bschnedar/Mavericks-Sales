import gspread
#import pandas
from google.oauth2 import service_account

import gspread


#infographic-generator@infographic-generator.iam.gserviceaccount.com

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
        # Get and print all records
        print(sheet_info.get_all_records())
    except:
        print('Error Occurred')
    return



if __name__ == '__main__':
    main()