from user_factory.vigenereCipher import vigenereCipherDecode


def read_received_text():
    import os
    path_to_received_text = os.path.join(os.getcwd(), "sending_text.txt")
    with open(path_to_received_text, "rb") as received_reader:
        return received_reader.read()


def decrypt(password):
    ciphertextBase64 = read_received_text()
    message = vigenereCipherDecode(str(password), ciphertextBase64)
    print("Received message", end="\n\n")
    print("> ", message, end="\n")


if __name__ == "__main__":
    decrypt("password")