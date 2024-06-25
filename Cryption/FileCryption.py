import os
from cryptography.fernet import Fernet
import Cryption.Key
import Utilities.ChooseFile


class FileCryption():
    def __init__(self, key, filePath):
        self.__key = key
        self.__filePath = filePath

    def GetKey(self):
        return self.__key

    def GetFilePath(self):
        return self.__filePath

    def SetKey(self, key):
        self.__key = key

    def SetFilePath(self, filePath):
        self.__filePath = filePath

    def EncryptionFile(key, filePath):
        # Create a Fernet object with the key
        fernet = Fernet(key)

        # Dosya uzantısı için
        fileName, fileExtension = os.path.splitext(os.path.basename(filePath))

        # şifrelenecek dosyayı seçme
        with open("../SendFile/" + fileName + fileExtension, 'rb') as file:
            file = file.read()

        # şifreleme
        lockedFile = fernet.encrypt(file)

        # şifrelenmiş yeni dosyayı yazma
        with open("../SendFile/" + 'locked_' + fileName + fileExtension, 'wb') as lockedWritableFile:
            lockedWritableFile.write(lockedFile)

    # EncryptionFile(Cryption.Key.ReadKeyFromText(), Utilities.ChooseFile.FileDirectoryWithGui())

    def DecryptionFile(key, filePath):
        # Fernet yardimi ile anahtar(key) oluşturuluyor
        fernet = Fernet(key)

        # Dosya uzantısı için
        fileName, fileExtension = os.path.splitext(os.path.basename(filePath))

        # şifrelenmiş dosya okunuyor
        with open("../SendFile/" + fileName + fileExtension, 'rb') as file:
            locked_file = file.read()

        # dosya şifresi çözülüyor
        unlockedFile = fernet.decrypt(locked_file)

        # şifresi çözülen dosyaya yazılıyor
        with open("../SendFile/" + 'un' + fileName + fileExtension, 'wb') as unlockedWritableFile:
            unlockedWritableFile.write(unlockedFile)

    # DecryptionFile(Cryption.Key.ReadKeyFromText(), Utilities.ChooseFile.FileDirectoryWithGui())
