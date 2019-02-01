
#import libraries
import os
from git import Repo

#set variables
email = input("Email: ")
print("Your email is: ", email)

repo = input("Please enter the url of the repository: ")
print("repository url: ", repo)

workDir = os.getcwd()
print("The current working directory is: ", workDir)

tempDir = workDir +"/temp"
os.mkdir(tempDir)

Repo.clone_from(repo, tempDir)