import os
from cryptography.fernet import Fernet


class Key():
    def __init__(self):
        return


def GenerateKey():  # Anahtar üretir ve kaydeder ayrıca geri döndürür
    key = Fernet.generate_key()
    return key


def GenerateKeyAndWriteToText():
    key = Fernet.generate_key()

    if not os.path.exists("../SendFile"):
        os.makedirs("../SendFile")

    with open('../SendFile/key.key', 'wb') as keyFile:
        keyFile.write(key)


def ReadKeyFromText():
    # Load the key from the file
    with open('../SendFile/key.key', 'rb') as file:
        key = file.read()

    return key
