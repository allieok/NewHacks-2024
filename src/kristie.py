import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

smtp_server = os.getenv("SMTP_SERVER")
smtp_port = int(os.getenv("SMTP_PORT"))
email_address = os.getenv("EMAIL_ADDRESS")
app_password = os.getenv("APP_PASSWORD")
to_address = os.getenv("TO_ADDRESS")

def send_email_notification(subject, body):
    msg = MIMEMultipart() # creates body of email
    msg['From'] = email_address
    msg['To'] = to_address
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port) # smtp server connection
        server.starttls()  # Enable security
        server.login(email_address, app_password)
        server.sendmail(email_address, to_address, msg.as_string()) # sends the mail
        print("Email sent successfully.") # can delete after
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        server.quit()

user = "Kristie" # need to change lol

# will be taken in by processed data
totaldata = 50
useddata = 25

# user can toggle the following based on preferences
notif1 = 0.5
notif2 = 0.25
notif3 = 0.1
notif4 = 0.05

# Example usage
if __name__ == "__main__":
    if useddata == notif1*totaldata:
        subject = "You have used half of your data plan!"
        body = f"Hello {user},\n\nThis is a reminder that you have used {int(100 - notif1 * 100)}% of your data.\nYou have {useddata}GB remaining.\n\nRegards,\nYou're Running Out of Data"
        send_email_notification(subject, body)
    elif useddata == notif2*totaldata:
        subject = "You have a quarter of data left!"
        body = f"Hello {user},\n\nThis is a reminder that you have used {int(100 - notif2 * 100)}% of your data.\nYou have {useddata}GB remaining.\n\nRegards,\nYou're Running Out of Data"
        send_email_notification(subject, body)
    elif useddata == notif3*totaldata:
        subject = "You have a 10% of data left!"
        body = f"Hello {user},\n\nThis is a reminder that you have used {int(100- notif3 * 100)}% of your data.\nYou have {useddata}GB remaining.\n\nRegards,\nYou're Running Out of Data"
        send_email_notification(subject, body)
    elif useddata == notif4*totaldata:
        subject = "You have a 5% of data left!"
        body = f"Hello {user},\n\nThis is a reminder that you have used {int(100- notif4 * 100)}% of your data.\nYou have {useddata}GB remaining.\n\nRegards,\nYou're Running Out of Data"
        send_email_notification(subject, body)