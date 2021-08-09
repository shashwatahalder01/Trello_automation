import os
from utils.uitlsfunction import read_date, read_and_update_counter, keep_reports

reportFolderName = f"{read_date()}_{read_and_update_counter()}"

# For running testCases
command = f"pytest -s --alluredir=ReportAllure/{reportFolderName} --html=ReportHtml/report_{reportFolderName}.html --self-contained-html testcases"
os.system(command)

#  Send email
sender = 'asif.augmedix@gmail.com'
password = 'asdfqwer#12'
receivers = 'asif.rouf@augmedix.com, rouf.asifur@gmail.com'
# sendemail(sender, password, receivers)

# number of allure & html reports to keep
number = 2
keep_reports(number)

# For generating report
command = f"allure serve ReportAllure/{reportFolderName}"
os.system(command)
