import os
import smtplib
import shutil
from pathlib import Path
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime
# from runconfiguration import linux

# Read counter
def read_counter():
    # read counter
    path = Path(__file__).parent / "counter.txt"
    f = open(path, 'r+')
    data = int(f.read())
    return data


# Read and Update counter
def read_and_update_counter():
    # read counter
    path = Path(__file__).parent / "counter.txt"
    f = open(path, 'r+')
    data = int(f.read())
    # update counter
    newCounter = str(data + 1)
    # write new counter
    f.seek(0)
    f.write(newCounter)
    f.truncate()
    f.close()
    return newCounter


# Read current date
def read_date():
    return str(datetime.today().strftime('%Y-%m-%d'))


# Send mail
def sendmail(senderEmail, senderPassword, receiversEmail, mailSubject, mailBody, attachedFilePath, bccMail=''):
    # Mail content, format, encoding
    message = MIMEMultipart()
    message['From'] = senderEmail
    message['To'] = receiversEmail
    message['Subject'] = Header(mailSubject, 'utf-8')
    if bccMail:
        message['Bcc'] = bccMail
    message.attach(MIMEText(mailBody))

    # build the attachment
    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(open(attachedFilePath, 'rb').read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attachedFilePath))
    message.attach(attachment)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(senderEmail, senderPassword)
        server.send_message(message)
        # server.sendmail(senderemail, receivers, message.as_string())
        print("Send email successfully!!!")
        server.close()
    except smtplib.SMTPException:
        print("Failed to send mail!!!")


# Delete Folder and its content except last n number of dirs
def del_dir(num_of_dir):
    basedir = Path(__file__).resolve().parent.parent
    dirName = "ReportAllure"
    dirPath = os.path.join(basedir, dirName)
    # print(dirPath)
    # dirList = [f for f in sorted(os.listdir(dirPath))]
    dirList = [os.path.join(dirPath, f) for f in sorted(os.listdir(dirPath))]
    dirList = dirList[:len(dirList) - num_of_dir]
    # print(dirList)
    for folder in dirList:
        try:
            shutil.rmtree(folder)
            # print('delete: ' + delDir)
        except OSError as e:
            print("Error: %s : %s" % (folder, e.strerror))
        # print('dir deleted')


# Delete file except last n number of files
def del_file(num_of_file):
    basedir = Path(__file__).resolve().parent.parent
    dirName = "ReportHtml"
    dirPath = os.path.join(basedir, dirName)
    fileList = [os.path.join(dirPath, f) for f in sorted(os.listdir(dirPath))]
    fileList = fileList[:len(fileList) - num_of_file]
    # print(fileList)
    for file in fileList:
        os.remove(file)


def keep_reports(number):
    del_dir(number)
    del_file(number)

def sendemail(sender, password, receivers):
    bccemail = ''
    emailsubject = 'Test Report'
    emailbody = "Dear Sir, Please check this report."
    attachedfilepath = ''
    attachedfilepath = Path(__file__).parent / f"../ReportHtml/report_{readdate()}_{readcounter()}.html"
    # attachedfilepath = Path(__file__).parent / f"../ReportHtml/report_2021-05-05_47.html"
    sendmail(sender, password, receivers, emailsubject, emailbody, attachedfilepath, bccemail)


# def connectionoff():
#     if linux:
#         # connectionOff = "nmcli networking off"
#         connectionOff = "nmcli r wifi off"
#         os.system(connectionOff)
#     else:
#         connectionOff = "netsh wlan disconnect"
#         os.system(connectionOff)
#
#
# def connectionon():
#     if linux:
#         # connectionOn = "nmcli networking on"
#         connectionOn = "nmcli r wifi on"
#         os.system(connectionOn)
#     else:
#         connectionOn = 'netsh wlan connect name="network_name"'
#         os.system(connectionOn)
