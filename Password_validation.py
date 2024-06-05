import re
flag=0

password=input("Enter the password")

if not re.search('[a-z]',password):
    flag=1
if not re.search('[A-Z]',password):
    flag=1
if not re.search('[0-9]',password):
    flag=1
if not re.search('[@#$%^&+=]',password):
    flag=1
if len(password)<8:
    flag=1


if flag==0:
    print("Password is valid")
else:
    print("Password is invalid")
