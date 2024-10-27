import csv


#for adding new accounts
account_company = "Telus"
new_account = ["dylan.doe@gmail.com", 30, 22] #example
# Open the CSV file in append mode
if account_company == "Telus":
   with open('telus.csv', mode='a', newline='') as file:
       writer = csv.writer(file)
       writer.writerow(new_account)  # Add the new row
elif account_company == "Bell":
   with open('bell.csv', mode='a', newline='') as file:
       writer = csv.writer(file)
       writer.writerow(new_account)
elif account_company == "Rogers":
   with open('rogers.csv', mode='a', newline='') as file:
       writer = csv.writer(file)
       writer.writerow(new_account)




#for reading data from the csv file
data = []
if account_company == "Telus": 
   with open('telus.csv', mode='r') as file:
       csv_reader = csv.DictReader(file)
       for row in csv_reader:
           data.append(row)
           print(row)
elif account_company == "Rogers":
   with open('rogers.csv', mode='r') as file:
       csv_reader = csv.DictReader(file)
       for row in csv_reader:
           data.append(row)
elif account_company == "Bell":
   with open('bell.csv', mode='r') as file:
       csv_reader = csv.DictReader(file)
       for row in csv_reader:
           data.append(row)
else:
   with open('other.csv', mode='r') as file:
       csv_reader = csv.DictReader(file)
       for row in csv_reader:
           data.append(row)


print(data)


account_email = "dylan.doe@gmail.com"
max = 0
current = 0


for thisaccount in data:
   print(thisaccount)
   matching_keys = [key for key, value in thisaccount.items() if value == "AccountNumber"]
   if matching_keys == account_email:
       max = [key for key, value in thisaccount.items() if value == "MaxRate"]
       current = [key for key, value in thisaccount.items() if value == "CurrentUsage"]
       break


for row in data:
   if row.get("AccountName") == account_email:
       account = row


print(max)
print(current)