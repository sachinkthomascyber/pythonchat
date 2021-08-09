from user_factory.vigenereCipher import vigenereCipherEncode


def sender(plaintext, password):

    sending_text = vigenereCipherEncode(str(password), plaintext.decode())

    import os
    path_to_sending_text = os.path.join(os.getcwd(), "sending_text.txt")
    with open(path_to_sending_text, "wb") as sending_writer:
        sending_writer.write(sending_text)
    
    print("Message sent")


if __name__ == "__main__":
    sender("1940hrs", "password")