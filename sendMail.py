import smtplib, ssl

def send_mail(subject, message, _recever_mail, _sender_mail, _sender_pass):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    recever_mail = _recever_mail # Kendi mailinizi koyunca o maile gonderiyor
    sender_mail = _sender_mail
    sender_password = _sender_pass

    server.login(sender_mail, sender_password)

    msg = f"Subject: {subject}\n\n{message}"

    server.sendmail(
        sender_mail,
        recever_mail,
        msg.encode("utf8")
    )

    print(msg)

    print("Mail has been sent")

    server.quit()
