import smtplib, ssl
import random
import getpass


def verify_user_email():
    """
    Verifies a user by sending a PIN to his/her email
    return True if verified else False
    """
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "sachinkthomas098@gmail.com"  # Enter your address
    password = "9446717333"
    pin = random.randint(100000,999999)
    
    receiver_email = input("Enter your email ID: ")
    
    message = f"""\
    Subject: Hi there

    Your 6 digit code is {pin}."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    code = input("Enter 6 digit code sent in email: ")

    if code == str(pin):
        print("Verification successful")
        return True
    else:
        print("Verification failed")
        return False


if __name__ == "__main__":
    print(verify_user_email())

