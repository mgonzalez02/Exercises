#import libraries
import os
from git import Repo
import subprocess
import shutil
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#emailer setup
import smtplib, ssl
port = 465 #for SSL
password = "Unic0rn$"
emailer = "mgonzalez.emailer@gmail.com"
#set variables
workDir = os.getcwd()
tempDir = workDir +"/temp"
email = input("Email Recipient: ")
repo = input("Please enter the url of the repository: ")
print("Gathering cloc information for", repo, "and emailing results to", email)
#check to see if temp folder already exists
if os.path.exists(tempDir):
    shutil.rmtree(tempDir)
#create temp folder for download
os.mkdir(tempDir)
#copy repo and get LOC
Repo.clone_from(repo, tempDir)
message_text = subprocess.run(["cloc", tempDir], stdout=subprocess.PIPE).stdout.decode("utf-8")

#Send the email
message = MIMEMultipart("alternative")
message["Subject"] = "cloc results for " + repo
message["From"] = emailer
message["To"] = email
body = MIMEText(message_text, "plain")
message.attach(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as server:
    server.login(emailer, password)
    server.sendmail(emailer, email, message.as_string())
#cleanup
shutil.rmtree(tempDir)