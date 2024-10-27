import csv

def addtofiles(account_company,new_account):
    #example: account_company = "Telus"
    #example: new_account = ["dylan.doe@gmail.com", 30, 22]
    
    # Open the CSV file in append mode
    if account_company == "Telus":
        with open('src/telus.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_account)  # Add the new row
    elif account_company == "Bell":
        with open('src/bell.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_account)
    elif account_company == "Rogers":
        with open('src/rogers.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_account)



def getaccountdetails(user_company,user_email):
    #for reading data from the csv file
    data = []
    if user_company == "Telus": 
        with open('src/telus.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
    elif user_company == "Rogers":
        with open('src/rogers.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
    elif user_company == "Bell":
        with open('src/bell.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
    else:
        with open('src/other.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)


    #find the dictionary related to each account and returns the account's maxrate and current datausage
    for thisaccount in data:
        print(thisaccount)
        thisemail = thisaccount.get("email")
        if thisemail == user_email:
            maxrate = thisaccount.get("datamax")
            datausage = thisaccount.get("datausage")

    return maxrate,datausage 