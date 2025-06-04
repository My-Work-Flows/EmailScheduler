import smtplib
import os
import sys
from email.mime.text import MIMEText

def send_email(subject, html_path):
    try:
        sender = os.environ["EMAIL_SENDER"]
        password = os.environ["EMAIL_PASSWORD"]
        recipients = os.environ["EMAIL_RECIPIENTS"].split(",")
        smtp_server = os.environ["SMTP_SERVER"]
        smtp_port = int(os.environ["SMTP_PORT"])

        print("🔐 Sender:", sender)
        print("📧 Recipients:", recipients)
        print("🌐 SMTP Server:", smtp_server)
        print("📁 HTML File:", html_path)

        if not os.path.exists(html_path):
            raise FileNotFoundError(f"HTML file not found: {html_path}")

        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        msg = MIMEText(html_content, "html")
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = ", ".join(recipients)

        print("🔌 Connecting to SMTP server...")
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.set_debuglevel(1)  # <--- Enables SMTP debug output
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, recipients, msg.as_string())

        print("✅ Email sent successfully.")

    except Exception as e:
        print(f"❌ Error sending email: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python email_sender.py '<subject>' '<html_path>'")
        sys.exit(1)

    subject = sys.argv[1]
    html_path = sys.argv[2]
    send_email(subject, html_path)
