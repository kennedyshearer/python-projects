import smtplib
import filetype
from email.message import EmailMessage


PASSWORD = "{APP_PASSWORD_HERE}"
SENDER = "everydaytechprojects@gmail.com"
RECEIVER = "everydaytechprojects@gmail.com"

def send_email(image_path):
    print("send_email function started.")
    email_message = EmailMessage()
    email_message["Subject"] = "Intruder alert!"
    email_message.set_content("Hey, there is a person in your room!")

    with open(image_path, "rb") as file:
        content = file.read()

        kind = filetype.guess(content)
        if kind is None:
            raise ValueError("Cannot guess file type!")

    maintype, subtype = kind.mime.split("/")
    email_message.add_attachment(content, maintype=maintype, subtype=subtype)

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("send_email function ended.")

if __name__ == "__main__":
    send_email(image_path="images/71.png")