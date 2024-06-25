import os
import pyzipper
from Utilities import CurrentMilliTime


class Package():
    def __init__(self, filePath, password):
        self.__filePath = filePath
        self.__password = password

    def GetFilePath(self):
        return self.__filePath

    def GetPassword(self):
        return self.__password

    def SetFilePath(self, filePath):
        self.__filePath = filePath

    def SetPassword(self, password):
        self.__password = password

    def Packaging(filePath, password):
        # Dosya adını ve uzantısını alma
        fileName, fileExtension = os.path.splitext(os.path.basename(filePath))
        timeStamp = str(CurrentMilliTime.CurrentMilliTime())

        with pyzipper.AESZipFile("../" + timeStamp + '.pck', 'w',
                                 encryption=pyzipper.WZ_AES) as zf:
            password = bytes(password, 'utf-8')
            zf.setpassword(password)
            zf.write(filePath, fileName + fileExtension)

    def Depackaging(filePath, password):
        # Dosyanın bulunduğu klasöre çıkartılacak yol oluştur
        extractPath = os.path.dirname(filePath)

        with pyzipper.AESZipFile(filePath) as zf:
            password = bytes(password, 'utf-8')
            zf.setpassword(password)
            zf.extractall(path=extractPath)
