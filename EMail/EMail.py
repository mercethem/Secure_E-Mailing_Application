import glob
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class Email():
    def __init__(self, emailFrom, password, emailList):
        self.__emailFrom = emailFrom
        self.__password = password
        self.__emailList = emailList

    def GetEmailFrom(self):
        return self.__emailFrom

    def GetPassword(self):
        return self.__password

    def GetEmailList(self):
        return self.__emailList

    def SetEmailFrom(self, emailFrom):
        self.__emailFrom = emailFrom

    def SetPassword(self, password):
        self.__password = password

    def SetEmailList(self, emailList):
        self.__emailList = emailList

    def SendEmail(emailFrom, password, emailList):
        smtpPort = 587
        smtpServer = 'smtp-mail.outlook.com'
        body = f""" 
        
                """  # For mail body

        message = MIMEMultipart()
        message['Subject'] = 'Encrypted'
        message['From'] = emailFrom
        message['To'] = emailList

        message.attach(MIMEText(body, 'plain'))

        # filename = "../instancePhoto.jpg"
        packageFiles = glob.glob(os.path.join("../", '*.pck'))
        filename = str(packageFiles.pop())

        attachment = open(filename, "rb")

        attachmentPackage = MIMEBase('application', 'octet-stream')
        attachmentPackage.set_payload((attachment).read())
        encoders.encode_base64(attachmentPackage)
        attachmentPackage.add_header('Content-Disposition', "attachment; filename=" + filename)
        message.attach(attachmentPackage)

        text = message.as_string()

        # print("Connecting to server")
        TIEServer = smtplib.SMTP(smtpServer, smtpPort)
        TIEServer.starttls()
        TIEServer.login(str(emailFrom), password)
        # print("Successfully connected to server")
        # print()

        # print(f"Sending email to {emailList}")
        TIEServer.sendmail(str(emailFrom), emailList, text)
        # print(f"Email sent to {emailList}")
        # print()
        TIEServer.quit()

    # SendEmail(emailFrom, password, emailList)
