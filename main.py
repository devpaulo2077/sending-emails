import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(recipient, subject, message):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender = "sender@gmail.com"
    password = "password_app"
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject

    msg.attach(MIMEText(message_html, 'html'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender, password)
        
        server.sendmail(sender, recipient, msg.as_string())
        print("EMAIL SENT")
    except Exception as e:
        print(f"ERROR SENDING EMAIL: {e}")
    finally:
        server.quit()

message_html = """
<html>
<head></head>
<body>
    <h1 style="color:#2563eb;">Hello World!!!</h1>
    <p>This is an email sent with an HTML body with <i>Python</i> !</p>
    <p style="color:#040916;">Save this repository</p>
</body>
</html>
"""

send_email("receiver@gmail.com", "title", message_html)
