import smtplib
from email.mime.text import MIMEText
import schedule
import time

def send_email():
    sender = 'your@gmail.com'    #this is sender's email
    receiver = 'receiver@gmail.com'   #this is receiver's email
    password = 'Your password'     
    msg = MIMEText('Daily reminder to stay hydrated! 💧')
    msg['Subject'] = 'Daily Reminder'
    msg['From'] = sender
    msg['To'] = receiver

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.send_message(msg)
        print("Reminder email sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Schedule the email to be sent daily at 9 AM
schedule.every(35).seconds.do(send_email)
while True:
    schedule.run_pending()
    time.sleep(1)  

if __name__ == "__main__":
    send_email()  
