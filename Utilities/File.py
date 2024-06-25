from Package.Packaging import Package


class File(Package):
    def __init__(self, fileName, fileExtension, fileDirectory):
        self.__fileName = fileName
        self.__fileExtension = fileExtension
        self.__fileDirectory = fileDirectory

    def GetFileName(self):
        return self.__fileName

    def GetFileExtension(self):
        return self.__fileExtension

    def GetDirectory(self):
        return self.__fileDirectory

    def SetFileName(self, fileName):
        self.__fileName = fileName

    def SetFileExtension(self, fileExtension):
        self.__fileExtension = fileExtension

    def SetDirectory(self, fileDirectory):
        self.__fileDirectory = fileDirectory
