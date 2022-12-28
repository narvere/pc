import os
from email.message import EmailMessage
import ssl
import smtplib
import dotenv
import tkinter.messagebox as messagebox
# assert 'SYSTEMROOT' in os.environ


def show_info():
    messagebox.showinfo("Info", "Письмо успешно отправлено!")


def show_error(ex):
    messagebox.showerror("Error", ex)


def send_mail(email_receiver, clipboard_text):
    print("Start!")
    dotenv.load_dotenv('.env')
    email_sender = os.environ["EMAIL_SENDER"]
    email_password = os.environ["EMAIL_PASSWORD"]
    # email_receiver = os.environ["EMAIL_RECEIVER"]
    subject = "A new user password"
    body = clipboard_text
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    print("Start1!")
    # with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    #     smtp.login(email_sender, email_password)
    #     smtp.sendmail(email_sender, email_receiver, em.as_string())
    #     print("Start2!")
    print(os.environ["EMAIL_SENDER"])
    try:
        with smtplib.SMTP_SSL(os.environ["MAIL_SERVER"], 465, context=context) as smtp:
            print(email_sender, email_password)
            smtp.login(user=email_sender, password=email_password)
            smtp.sendmail(from_addr=email_sender, to_addrs=[email_receiver, 'deniss.hohlov@gmail.com'],
                          msg=em.as_string())
            show_info()
    except Exception as ex:
        show_error(ex)

# send_mail('deniss.hohlov@gmail.com')
