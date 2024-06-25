from cryptography.fernet import Fernet


class MessageCryption():
    def __init__(self, message, key):
        self.__message = message
        self.__key = key

    def GetMessage(self):
        return self.__message

    def GetKey(self):
        return self.__key

    def SetMessage(self, message):
        self.__message = message

    def SetKey(self, key):
        self.__key = key


    def DecryptMessage(message, key):  # şifreli mesajlajı alıp çözmeye yarar
        fernet = Fernet(key)
        decryptedMessage = fernet.decrypt(message)
        return decryptedMessage


    def EncryptMessage(message, key):  # mesajı alıp şifrelemeye yarar
        message = message.encode()
        fernet = Fernet(key)
        encryptedMessage = fernet.encrypt(message)
        return encryptedMessage
