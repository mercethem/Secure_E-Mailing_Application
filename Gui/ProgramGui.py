import glob
import shutil
import tkinter as tk
from tkinter import messagebox
import Cryption.Key
import Cryption.FileCryption
import EMail.EMail
import Package.Zip
import Package.Packaging
import Utilities.ChooseFile
import Utilities.MacAdress

passwordGenerated = False  # Flag to check if the password has been generated or not


class ProgramGui():
    def __init__(self):
        return


def Packaging():
    paketlenecekdosya = "../SendFile.zip"  # paketleme başlangıç
    packaging = Package.Packaging.Package
    packaging.Packaging(paketlenecekdosya, Utilities.MacAdress.GetMacMyAddress())
    # Package.Packaging.Packaging(paketlenecekdosya, Utilities.MacAdress.GetMacMyAddress())  # paketleme bitiş
    os.remove("../SendFile.zip")
    UpdateFileList()
    UpdateReceiverFileList()


def Depacking():
    packageFiles = glob.glob(os.path.join("../", '*.pck'))
    for file in packageFiles:
        try:
            messagebox.showwarning("Success",
                                   "Depackaging Done!")
            depackage = Package.Packaging.Package
            depackage.Depackaging(file, Utilities.MacAdress.GetMacMyAddress())
            # Package.Packaging.Depackaging(file, "50-EB-F6-E6-68-FD")  # depaketleme bitiş
            # shutil.rmtree(file)
            os.remove(file)
        except:
            messagebox.showwarning("Failed",
                                   "Package not found!")
    UpdateReceiverFileList()


def CheckKeyFile():
    if os.path.exists("../SendFile/key.key"):
        messagebox.showwarning("Warning",
                               "A key file already exists. Creating a new key will invalidate the previous one.")
        return True
    return False


def SendEmail():
    try:
        x = EMail.EMail.Email
        x.SendEmail(senderEmailEntry.get().strip(), senderPasswordEntry.get().strip(),
                    receiverEmailEntry.get().strip())
        # EMail.EMail.SendEmail(senderEmailEntry.get().strip(), senderPasswordEntry.get().strip(), receiverEmailEntry.get().strip())
        messagebox.showinfo("Information", "Email sent successfully!")
    except Exception as exception:
        messagebox.showinfo("Error!!!")


def Zipping():
    # ziplenecekdosya = Utilities.ChooseFile.FolderPathWithGui()  # zip başlangıç
    folderCompression = Package.Zip.Zip
    folderCompression.FolderCompression("../SendFile", Utilities.ChooseFile.FileName("../SendFile"))
    # Package.Zip.FolderCompression("../SendFile", Utilities.ChooseFile.FileName("../SendFile"))  # zip bitiş
    shutil.rmtree("../SendFile")
    UpdateFileList()


def Dezipping():
    # deziplenecekdosya = Utilities.ChooseFile.FileDirectoryWithGui()  # dezip başlangıç
    fileExtract = Package.Zip.Zip
    fileExtract.FileExtract("../SendFile.zip")
    # Package.Zip.FileExtract("../SendFile.zip")  # dezip bitiş
    os.remove("../SendFile.zip")
    UpdateFileList()


def AttachFile():
    # Add necessary code to attach files here
    Utilities.ChooseFile.CopyPasteFile(Utilities.ChooseFile.FileDirectoryWithGui())
    UpdateFileList()


def AttachFilePackage():
    # Add necessary code to attach files here
    Utilities.ChooseFile.CopyPastePackage(Utilities.ChooseFile.PackageDirectoryWithGui())
    UpdateReceiverFileList()


def GeneratePassword():
    global passwordGenerated
    if os.path.exists("../SendFile/key.key"):
        answer = messagebox.askquestion("Warning",
                                        "A key file already exists. Creating a new key will invalidate the previous one. Do you still want to generate a new password?")
        if answer == 'no':
            return
    if not passwordGenerated:  # If password has not been generated previously
        answer = messagebox.askquestion("Password Generation", "Do you want to generate a new password?")
        if answer == 'yes':
            Cryption.Key.GenerateKeyAndWriteToText()
            passwordGenerated = True
            messagebox.showinfo("Information", "Password generated successfully.")
    else:
        answer = messagebox.askquestion("Warning",
                                        "A password has already been generated. Creating a new password will invalidate the previous one. Do you want to continue?")
        if answer == 'yes':
            Cryption.Key.GenerateKeyAndWriteToText()
            messagebox.showinfo("Information", "New password generated successfully.")
    UpdateFileList()


def EncryptFile():
    if not os.path.exists("../SendFile/key.key"):
        messagebox.showinfo("ATTENTION", "There is not exist KEY.")
        return

    key = Cryption.Key.ReadKeyFromText()

    # Dosya listesinin bulunduğu dizini al
    directory = "../SendFile"

    # ethem_folder = os.path.join(directory, "ethem")
    # os.makedirs(ethem_folder, exist_ok=True)

    # Klasördeki tüm dosyaları sırayla şifrele
    for fileName in os.listdir(directory):
        filePath = os.path.join(directory, fileName)
        if os.path.isfile(filePath) and fileName != "key.key":
            encryptionFile = Cryption.FileCryption.FileCryption
            encryptionFile.EncryptionFile(key, filePath)
            os.remove(filePath)

    UpdateFileList()


def DecryptFile():
    if not os.path.exists("../SendFile/key.key"):
        messagebox.showinfo("ATTENTION", "There is not exist KEY.")
        return

    key = Cryption.Key.ReadKeyFromText()

    # Dosya listesinin bulunduğu dizini al
    directory = "../SendFile"

    # ethem_folder = os.path.join(directory, "ethem")
    # os.makedirs(ethem_folder, exist_ok=True)

    # Klasördeki tüm dosyaları sırayla şifrele
    for fileName in os.listdir(directory):
        filePath = os.path.join(directory, fileName)
        if os.path.isfile(filePath) and fileName != "key.key":
            decryption = Cryption.FileCryption.FileCryption
            decryption.DecryptionFile(key, filePath)
            # Cryption.FileCryption.DecryptionFile(key, filePath)
            os.remove(filePath)
    os.remove("../SendFile/key.key")
    UpdateFileList()
    UpdateReceiverFileList()


def UpdateFileList():
    fileList.delete(0, tk.END)
    directory = "../SendFile"
    if os.path.exists(directory):
        files = os.listdir(directory)
        for file in files:
            fileList.insert(tk.END, file)


def UpdateReceiverFileList():
    receiverFileList.delete(0, tk.END)
    mainPath = "../"  # ethem dizini
    if os.path.exists(mainPath):
        packageFiles = [dosya for dosya in os.listdir(mainPath) if dosya.endswith(".pck")]
        for file in packageFiles:
            receiverFileList.insert(tk.END, file)


def DeleteSelectedFiles():
    selectedIndices = fileList.curselection()
    if selectedIndices:
        for index in selectedIndices[::-1]:
            fileName = fileList.get(index)
            directory = "../SendFile"
            filePath = os.path.join(directory, fileName)
            if os.path.exists(filePath):
                os.remove(filePath)
                if fileName == "key.key":  # If the deleted file is key.key, update the flag
                    global passwordGenerated
                    passwordGenerated = False
        UpdateFileList()


import os


def DeleteSelectedFilesPackage():
    selectedIndices = receiverFileList.curselection()
    if selectedIndices:
        for index in selectedIndices[::-1]:
            fileName = receiverFileList.get(index)
            if fileName.endswith(".pck"):  # Dosya uzantısını kontrol et
                directory = "../"
                filePath = os.path.join(directory, fileName)
                if os.path.exists(filePath):
                    os.remove(filePath)
    UpdateReceiverFileList()


# Create main window
root = tk.Tk()
root.title("Ethem MERÇ")

# Sender email and password entry
senderEmailLabel = tk.Label(root, text="Sender email:")
senderEmailLabel.grid(row=0, column=0, sticky='w', padx=5, pady=5)
senderEmailEntry = tk.Entry(root, width=5)
senderEmailEntry.grid(row=1, column=0, sticky='we', padx=5, pady=5)

senderPasswordLabel = tk.Label(root, text="Password:")
senderPasswordLabel.grid(row=0, column=1, sticky='w', padx=1, pady=1)
senderPasswordEntry = tk.Entry(root, show="*")
senderPasswordEntry.grid(row=1, column=1, sticky='we', padx=5)

# Generate password button
generatePasswordButton = tk.Button(root, text="Generate Password", command=GeneratePassword)
generatePasswordButton.grid(row=0, column=2, sticky='w', padx=5, pady=10)

# Zip button
zippingButton = tk.Button(root, text="Zip Folder                ",
                          command=Zipping)  # Burada EthemFunction, bu butona basıldığında gerçekleşecek işlemi tanımlamak için bir fonksiyon adı olmalı
zippingButton.grid(row=2, column=2, sticky='w', padx=5, pady=10)

# Unzip button
dezippingButton = tk.Button(root, text="Dezip Folder                ",
                            command=Dezipping)  # Burada EthemFunction, bu butona basıldığında gerçekleşecek işlemi tanımlamak için bir fonksiyon adı olmalı
dezippingButton.grid(row=2, column=4, sticky='w', padx=5, pady=10)

# Encrypt file button
encryptButton = tk.Button(root, text="Encrypt File             ", command=EncryptFile)
encryptButton.grid(row=1, column=2, sticky='w', padx=5, pady=10)

# Dencrypt file button
decryptButton = tk.Button(root, text="Decrypt File                  ", command=DecryptFile)
decryptButton.grid(row=3, column=4, sticky='w', padx=5, pady=10)

# Packaging button
packagingButton = tk.Button(root, text="Packaging Folder   ",
                            command=Packaging)  # Burada EthemFunction, bu butona basıldığında gerçekleşecek işlemi tanımlamak için bir fonksiyon adı olmalı
packagingButton.grid(row=3, column=2, sticky='w', padx=5, pady=10)

# Depackaging button
depackagingButton = tk.Button(root, text="Depackaging Folder   ",
                              command=Depacking)  # Burada EthemFunction, bu butona basıldığında gerçekleşecek işlemi tanımlamak için bir fonksiyon adı olmalı
depackagingButton.grid(row=1, column=4, sticky='w', padx=5, pady=10)

# Receiver email entry
receiverEmailLabel = tk.Label(root, text="Receiver email:")
receiverEmailLabel.grid(row=2, column=0, sticky='w', padx=1, pady=1)
receiverEmailEntry = tk.Entry(root)
receiverEmailEntry.grid(row=3, column=0, columnspan=2, sticky='we', padx=5)

macAddress = tk.Label(root, text="Physical My Mac Address: {MyMac}".format(MyMac=Utilities.MacAdress.GetMacMyAddress()))
macAddress.grid(row=10, column=0, sticky='w')

# Attach file button
attachButton = tk.Button(root, text="Attach File                ", command=AttachFile)
attachButton.grid(row=9, column=1, sticky='w', padx=10, pady=10)

# Listbox for file list
fileListLabel = tk.Label(root, text="Sender File List :")
fileListLabel.grid(row=7, column=0, sticky='w')
fileList = tk.Listbox(root, height=5, width=10, selectmode=tk.MULTIPLE)
fileList.grid(row=8, column=0, columnspan=2, sticky='we', padx=5)

# Delete button
deleteButton = tk.Button(root, text="Delete", command=DeleteSelectedFiles)
deleteButton.grid(row=9, column=0, sticky='w', padx=5)

# Delete button
deleteButton2 = tk.Button(root, text="Delete", command=DeleteSelectedFilesPackage)
deleteButton2.grid(row=9, column=3, sticky='w', padx=5)

# Send button
sendButton = tk.Button(root, text="Send                         ", command=SendEmail)
sendButton.grid(row=10, column=1, sticky='e', padx=10, pady=10)

# Listbox for file list
fileListLabel2 = tk.Label(root, text="Receiver File List :")
fileListLabel2.grid(row=7, column=3, sticky='w')
receiverFileList = tk.Listbox(root, height=5, width=40, selectmode=tk.MULTIPLE)
receiverFileList.grid(row=8, column=3, columnspan=2, sticky='we', padx=5)

# Attach file button
attachButton2 = tk.Button(root, text="Attach File                ", command=AttachFilePackage)
attachButton2.grid(row=9, column=4, sticky='w', padx=5, pady=5)

# Update file list
UpdateFileList()
UpdateReceiverFileList()

# Keep the window open
root.mainloop()
