import smtplib
import os
from email.mime.text import MIMEText

def send_email(subject, html_path):
    sender = os.environ["EMAIL_SENDER"]
    password = os.environ["EMAIL_PASSWORD"]
    recipients = os.environ["EMAIL_RECIPIENTS"].split(",")
    smtp_server = os.environ["SMTP_SERVER"]
    smtp_port = int(os.environ["SMTP_PORT"])

    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    msg = MIMEText(html_content, "html")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipients, msg.as_string())
        print(f"Email sent to: {recipients}")
