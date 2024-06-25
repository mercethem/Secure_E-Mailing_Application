import os
import zipfile
from zipfile import ZipFile
from Utilities import CurrentMilliTime


class Zip():
    def __init__(self, filePath):
        self.__filePath = filePath

    def GetFilePath(self):
        return self.__filePath

    def SetFilePath(self, filePath):
        self.__filePath = filePath

    def FileCompression(filePath):
        # dosyayı seçmeye yarar ve uzantıyı seçer
        fullFileName = filePath
        fullFileNameArray = fullFileName.split(".")
        fileExtension = fullFileNameArray.pop()
        fileName = fullFileNameArray.pop()

        # zipleme işlemini ad olarak milisaniyelerle yapıyor
        with ZipFile(str(CurrentMilliTime.CurrentMilliTime()) + '.zip', 'w') as zipFile:
            zipFile.write(fileName + "." + fileExtension)

    def FileExtract(filePath):
        # zipten çıkartma

        fileName, fileExtension = os.path.splitext(os.path.basename(filePath))

        with zipfile.ZipFile("../" + fileName + fileExtension, 'r') as myzip:
            myzip.extractall("../" + fileName)

    def FolderCompression(folderPath, packageName):
        if not packageName.endswith(".zip"):
            packageName += ".zip"

        with zipfile.ZipFile(packageName, 'w', zipfile.ZIP_DEFLATED) as packageFolder:
            for packageRoot, folderNames, fileNames in os.walk(folderPath):
                for fileName in fileNames:  # Düzeltme: folderNames yerine fileName kullanılmalı
                    filePath = os.path.join(packageRoot, fileName)
                    packageFolder.write(filePath, os.path.relpath(filePath, folderPath))
        # FileChangeName(packageName)

    def FolderExtract(folderPath, packageName=None):
        with zipfile.ZipFile(folderPath, 'r') as packageFolder:
            if packageName is None:
                # Eğer packageName belirtilmemişse, klasör adını kullan
                packageName = os.path.splitext(os.path.basename(folderPath))[0]
            packageFolder.extractall(packageName)

    def FileChangeName(oldNamePath):
        newNamePath = oldNamePath.replace(".zip", ".package")
        os.rename(oldNamePath, newNamePath)
