ABOUT CLOCREPOY.PY
==========================

The general purpose of this script is to generate a cloc output
from a specified repository and email the results to the given email.

Guide
==========================

The user will be prompted to input an Email Recipient and a repository url.
Once input, the script will create a temp folder in the working directory
and download the repository into the temp folder it has created. Once 
downloaded the script will use the cloc module to produce a LOC analysis 
and send the results to the email recipient provided. After the results 
have been successfully emailed, the script will delete the temp folder and
all of its contents. 

Email Information
==========================

A gmail account was created for the purposes of email the results to the
specified email recipient. 
The account created is: mgonzalez.emailer@gmail.com
This account can be changed within the script if needed.

Possible Issues
==========================

The scipt will run into errors if the email address provided is not valid
or if the repository url given is invalid.