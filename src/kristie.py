import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from constants import constants
import os

smtp_server = constants.SMTP_SERVER
smtp_port = constants.SMTP_PORT
email_address = constants.EMAIL_ADDRESS
app_password = constants.APP_PASSWORD

def send_email_notification(subject, body, to_address):
    msg = MIMEMultipart() # creates body of email
    msg['From'] = email_address
    msg['To'] = to_address
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port) # smtp server connection
        server.starttls()  # Enable security
        server.login(email_address, app_password)
        server.sendmail(email_address, to_address, msg.as_string()) 
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        server.quit()

if __name__ == "__main__":
    print("hi")