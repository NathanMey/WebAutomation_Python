import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import inputBox

def send_email(to, subject, file_path, emailContent):
    sender = inputBox.input_with_button('Please type in your username for the email')
    password = inputBox.input_with_button('Please type in your password for the email')

    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = to
    message["Subject"] = subject
    message.attach(MIMEText(emailContent))

    with open(file_path, "rb") as f:
        payload = MIMEBase("application", "octet-stream")
        payload.set_payload((f.read()))

    encoders.encode_base64(payload)
    payload.add_header("Content-Disposition", "attachment", filename=os.path.basename(file_path))
    message.attach(payload)

    with smtplib.SMTP("smtp.office365.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(sender, password)
        smtp.sendmail(sender, to, message.as_string())
        print("Email sent successfully")

    if __name__ == "__main__":
        to = "thembani.ncalane@driverisk.com"
        subject = "Test Email with Attachment"
        file_path = "path/to/your/file.ext"
        send_email(to, subject, file_path)
