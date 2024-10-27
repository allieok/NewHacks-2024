from flask import Flask, request, jsonify
import csv
import os
from account import Account
import kristie

app = Flask(__name__)

def load_account_from_csv(company_name, email):
    """
    Loads the account data for a specified company and account number.

    Parameters:
        company_name (str): The name of the company (used to locate the CSV file).
        account_number (str): The account number of the user.

    Returns:
        Account: An Account instance if the account is found, otherwise None.
    """
    if email == "a@mail.com" and company_name == "sample":
        return Account(email, company_name, 5000, 1000, 300, 50)
    
    file_path = f"src/{company_name}.csv"  

    if not os.path.isfile(file_path):
        print(f"Company not found. Please try agaain.")
        company_name = input("Enter your telecom company name: ").strip()
        load_account_from_csv(company_name, email)
        return None

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['email'].strip() == email:
                max_data = int(row['datamax'].strip())
                usage_data = int(row['datausage'].strip())
                max_call = int(row['callmax'].strip())
                call_usage = int(row['callusage'].strip())
                return Account(email, company_name, max_data, usage_data, max_call, call_usage)

    print(f"Account {email} not found in {company_name}. Please try again.")
    email = input("Enter your email: ").strip()
    load_account_from_csv(company_name, email)
    return None

def check_data_usage_limits(account, threshold = [0.1, 0.25, 0.5]):
    """
    Checks if an account's usage is nearing the max rate based on a threshold.

    Parameters:
        account (Account): The Account instance to check.
        threshold (float): The threshold of max data usage (default is 50%).

    Returns:
        bool: True if the account is below its threshold. False otherwise.
    """
    for num in threshold:
        if account.current_usage / account.max_data <= num:
            return True
    return False

def check_call_usage_limits(account, threshold = [0.1, 0.25, 0.5]):
    """
    Checks if an account's usage is nearing the max rate based on a threshold.

    Parameters:
        account (Account): The Account instance to check.
        threshold (float): The threshold of max data usage (default is 50%).

    Returns:
        bool: True if the account is below its threshold. False otherwise.
    """
    for num in threshold:
        if account.current_usage / account.max_data <= num:
            return True
    return False

@app.route('/run-check', methods=['POST'])
def run_check():
    data = request.json
    company = data.get('company')
    email = data.get('email')

    account, error = load_account_from_csv(company, email)
    if error:
        return jsonify({'message': error}), 400

    if account:
        data_used = account.current_usage
        data_remaining = account.max_data - data_used
        call_used = account.call_usage
        call_remaining = account.max_call - call_used

        response_message = "No email sent; limits not exceeded."
        email_sent = False

        if check_data_usage_limits(account):
            if check_call_usage_limits(account):
                kristie.send_email_notification(
                    "You're running out of data and minutes!",
                    f"Hello {account.email}, you have used {account.current_usage} MB of your {account.max_data} MB data plan and {account.call_usage} minutes of your {account.max_call} minutes.",
                    account.email
                )
                response_message = "Email for data and minutes sent."
                email_sent = True
            else:
                kristie.send_email_notification(
                    "You're running out of data!",
                    f"Hello {account.email}, you have used {account.current_usage} MB of your {account.max_data} MB data plan.",
                    account.email
                )
                response_message = "Email for data only sent."
                email_sent = True
        elif check_call_usage_limits(account):
            kristie.send_email_notification(
                "You're running out of minutes!",
                f"Hello {account.email}, you have used {account.call_usage} minutes of your {account.max_call} minutes.",
                account.email
            )
            response_message = "Email for minutes only sent."
            email_sent = True

        return jsonify({
            'message': response_message,
            'email_sent': email_sent,
            'data_used': data_used,
            'data_remaining': data_remaining,
            'call_used': call_used,
            'call_remaining': call_remaining
        })
    else:
        return jsonify({'message': "Account not found."}), 404


if __name__ == "__main__":
    app.run(debug=True)
