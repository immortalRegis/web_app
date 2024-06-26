import smtplib
import ssl
import os


def send_new_email(content):
    username = "segun.adeokun@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "shegs637@gmail.com"

    host = "smtp.gmail.com"
    port = 465

    message = content
    con = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=con) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
