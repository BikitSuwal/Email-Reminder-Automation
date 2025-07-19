import smtplib
import os
from dotenv import load_dotenv
import logging
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

log_folder = "logs"
os.makedirs(log_folder, exist_ok=True)

log_file= os.path.join(log_folder,"email_log.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)



def send_email():
    try:
        Email = os.getenv("EMAIL_USER")
        Password = os.getenv("EMAIL_PASSWORD")
        Recipient = os.getenv("EMAIL_TO")
        subject = "Where is your DISCIPLINE??"
        body = "You forgot you have to become the strongest and richest person in the entire bloodline of your family.!!! Stop being a pussy and get back to work!!"

        if not Email or not Password or not Recipient:
            raise ValueError("EMAIL_USER, EMAIL_PASSWORD, and EMAIL_TO environment variables must be set.")

        msg = MIMEText(body)
        msg['From'] = Email
        msg['To'] = Recipient
        msg['Subject'] = subject


        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(Email, Password)
            server.send_message(msg)

        logging.info(f"Email sent successfully to {Recipient} at {datetime.now()}")
    
    except Exception as e:
        logging.error(f"Failed to send email to {Recipient} at {datetime.now()}: {e}")
        raise

if __name__ == "__main__":
    logging.info("===script-started===")
    send_email()
    logging.info("===script-finished===")