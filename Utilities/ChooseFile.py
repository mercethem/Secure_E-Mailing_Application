import os
import shutil
from tkinter import Tk, filedialog  # Python 3.x
from tkinter.filedialog import askopenfilename


def FileDirectoryWithGui():  # dosyayı seçmeyi sağlar
    try:
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        fileDirectory = askopenfilename()
        return fileDirectory
    except NameError:
        return None


def PackageDirectoryWithGui():
    Tk().withdraw()  # Tam bir GUI istemiyoruz, bu yüzden kök pencerenin görünmesini önle
    filePath = askopenfilename(filetypes=[("PCK files", "*.pck")])
    return filePath


def FileName(fileDirectory):  # Sadece dosyanın ismini ve uzantısını bir olarak döndürür
    fileName = fileDirectory  # show an "Open" dialog box and return the path to the selected file
    fileNameArray = fileName.split('\\')
    fileName = fileNameArray.pop()

    # Yukarıda belirtilen işlemler dosyanın adının seçilmesini bir gui yardımı ile yapar
    # Bir liste oluşturur ve steak mantığı güderek dosya adını seçer ve iki tane değer döndürür adı ve uzantısı
    return fileName


def FilePath(fileDirectory):  # Sadece dosyanın bulunduğu klasörün yolunu verir
    filePath = fileDirectory  # show an "Open" dialog box and return the path to the selected file
    fileNameArray = filePath.split('\\')
    filePath = fileNameArray.pop()
    fileNameArray = '\\'.join(fileNameArray)

    # Yukarıda belirtilen işlemler dosyanın adının seçilmesini bir gui yardımı ile yapar
    # Bir liste oluşturur ve steak mantığı güderek dosya adını seçer ve iki tane değer döndürür adı ve uzantısı
    return fileNameArray


def FolderPathWithGui():
    folderPah = filedialog.askdirectory()
    return folderPah


def FileListInFolder(filePath):
    fileList = os.listdir(filePath)
    return fileList


def FileDirectoryListInFolder(filePath):
    fileList = os.listdir(filePath)
    for i in range(len(fileList)):
        fileList[i] = (filePath + "\\" + fileList[i])
    return fileList


def CutPasteFiles(fileList, destinyFolder):
    for dosya in fileList:
        dosya_adi = os.path.basename(dosya)
        hedef_yol = os.path.join(destinyFolder, dosya_adi)
        shutil.move(dosya, hedef_yol)


#
# kaynak_klasor = FolderPathWithGui()
# dosya_listesi = FileDirectoryListInFolder(kaynak_klasor)
# # Taşınacak dosyaların hedef klasörü
# hedef_klasor = FolderPathWithGui()
# # Fonksiyonu çağırarak dosyaları kes
# CutPasteFiles(dosya_listesi, hedef_klasor)

def CopyPasteFile(filePath):
    shutil.copy2(filePath, "../SendFile")


def CopyPastePackage(filePath):
    shutil.copy2(filePath, "../")
