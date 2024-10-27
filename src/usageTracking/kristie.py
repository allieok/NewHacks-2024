import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
email_address = "yourerunningoutofdata@gmail.com"
app_password = "urct wsrl xiqo tgou"

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
    # if useddata == notif1*totaldata:
    #     subject = "You have used half of your data plan!"
    #     body = f"Hello {user},\n\nThis is a reminder that you have used {int(100 - notif1 * 100)}% of your data.\nYou have {useddata}GB remaining.\n\nRegards,\nYou're Running Out of Data"
    #     send_email_notification(subject, body)
    # elif useddata == notif2*totaldata:
    #     subject = "You have a quarter of data left!"
    #     body = f"Hello {user},\n\nThis is a reminder that you have used {int(100 - notif2 * 100)}% of your data.\nYou have {useddata}GB remaining.\n\nRegards,\nYou're Running Out of Data"
    #     send_email_notification(subject, body)
    # elif useddata == notif3*totaldata:
    #     subject = "You have a 10% of data left!"
    #     body = f"Hello {user},\n\nThis is a reminder that you have used {int(100- notif3 * 100)}% of your data.\nYou have {useddata}GB remaining.\n\nRegards,\nYou're Running Out of Data"
    #     send_email_notification(subject, body)
    # elif useddata == notif4*totaldata:
    #     subject = "You have a 5% of data left!"
    #     body = f"Hello {user},\n\nThis is a reminder that you have used {int(100- notif4 * 100)}% of your data.\nYou have {useddata}GB remaining.\n\nRegards,\nYou're Running Out of Data"
    #     send_email_notification(subject, body)