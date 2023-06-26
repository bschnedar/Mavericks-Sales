from google.oauth2 import service_account
import gspread
import matplotlib.pyplot as plt


def open(name):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive.file',
             'https://www.googleapis.com/auth/drive']

    # Reading Credentails
    credentials = service_account.Credentials.from_service_account_file('infographic-generator-a3267a9c8df0.json',
                                                                        scopes=scope)
    gc = gspread.authorize(credentials)
    # Open Sheet
    print("Opening Sheet " + name)

    sheet = gc.open("MV-"+name)

    try:
        sheet_info = sheet.get_worksheet(0)
        print("Sheet Exists: " + name)
        return sheet
    except:
        print('Error Occurred, Sheet missing: ' + name)
        return None


def plot_data(y,x_label,y_label,title2,label2):
    plt.plot(y,  label = label2)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.title(title2)
    return plt


#Retusn the total cans sold
def total_product(sheet):
    sheet_info = sheet.get_worksheet(0)
    product_amount = sheet_info.col_values(2)
    can_total = 0

    for x in product_amount:
        try:
            can_total = can_total + int(x)
        except:
            pass

    return can_total


#Returns total montly profit
def gross_profit(sheet):
    sheet_info = sheet.get_worksheet(0)
    daily_sales = sheet_info.col_values(3)
    profit_total = 0

    for x in daily_sales:
        x = x.strip('$')
        try:
            profit_total = profit_total + float(x)
        except:
            pass

    return profit_total


def main():

    sheet1 = open("January")
    sheet2 = open("Febuary")
    sheet3 = open("March")
    sheet4 = open("April")
    sheet5 = open("May")

    sheets = [sheet1,sheet2,sheet3,sheet4,sheet5]

    profit_plot = []
    can_total = []
    for x in sheets:
        profit_plot.append(gross_profit(x))
        can_total.append(total_product(x))

    product_sold = plot_data(
                            profit_plot,
                            "Months",
                            "Earnings",
                            "Mavericks Sales",
                            "Cans Sold"
                            )
    cans_sold = plot_data(
                            can_total,
                            "Months",
                            "Cans Sold",
                            "Mavericks Production",
                            "Earnings"
                            )
    plt.legend()
    #plt.show()
    plt.savefig(fname = "export")
    print("image has been generated sucessfully!")

    return


if __name__ == '__main__':
    main()