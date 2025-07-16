import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL = os.environ.get("EMAIL_USER")
PASSWORD = os.environ.get("EMAIL_PASS")
TO = os.environ.get("EMAIL_TO")

if EMAIL is None or PASSWORD is None or TO is None:
    raise ValueError("EMAIL_USER, EMAIL_PASS, and EMAIL_TO environment variables must be set.")

subject = "Automated Email"
body = "This is a test email sent automatically from GitHub Actions!"

msg = MIMEMultipart()
msg['From'] = EMAIL
msg['To'] = TO
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.send_message(msg)
    print("✅ Email sent successfully.")
except Exception as e:
    print(f"❌ Failed to send email: {e}")
finally:
    server.quit()
