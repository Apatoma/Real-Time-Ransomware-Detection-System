import smtplib
from email.mime.text import MIMEText

class AlertSystem:
    def __init__(self, email_recipients):
        self.email_recipients = email_recipients

    def send_alert(self, message):
        msg = MIMEText(message)
        msg['Subject'] = 'Ransomware Alert'
        msg['From'] = 'alert@securitysystem.com'
        msg['To'] = ', '.join(self.email_recipients)

        with smtplib.SMTP('localhost') as server:
            server.sendmail('alert@securitysystem.com', self.email_recipients, msg.as_string())

        print("Alert sent!")
