import os

permission = input("Do you want shutdown the computer?(yes/no): ")
if (permission == 'no'):
    exit
else:
    os.system("shutdown /s /t 1")