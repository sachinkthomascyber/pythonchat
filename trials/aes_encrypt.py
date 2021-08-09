from Crypto.Cipher import AES

key = b'Sixteen byte key'

def encrypt():
    cipher = AES.new(key, AES.MODE_EAX)

    nonce = cipher.nonce

    data = b"i love u"
    ciphertext, tag = cipher.encrypt_and_digest(data)

    print(ciphertext, tag)
    return nonce, ciphertext, tag


def decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        print("The message is authentic:", plaintext.decode())
    except ValueError:
        print("Key incorrect or message corrupted")


nonce, ciphertext, tag = encrypt()
print(type(nonce), type(ciphertext), type(tag))
decrypt(nonce=nonce, ciphertext=ciphertext, tag=tag)






