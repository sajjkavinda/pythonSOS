import platform
import os
import datetime

print("Platform: " + platform.platform())

a = platform.system()
if (a == "Linux"):
    x = datetime.datetime.now()
    print(x.strftime("%c"))

    f1 = open(r'/Desktop/entries_Lin.log', 'w') 

    os.chdir(r'/lib')
    
    for root, dirs, files in os.walk("/lib"):
        for file in files:
            if file.endswith(".bin"):
                print(file)
                f1.write(file + "\n")

elif (a == "Windows"):

    x = datetime.datetime.now()
    print(x.strftime("%d" "-" "%b" "-" "%y"))
    print(x.strftime("%I" ":" "%M" " " "%p"))

    f2 = open(r'C:\entries_Win10.log', 'w') 

    os.chdir(r'C:\Windows\system32')

    for root, dirs, files in os.walk("C:\Windows\system32"):
        for file in files:
            if file.endswith(".exe"):
                print(file)
                f2.write(file + "\n")

elif (a == "Darwin"):

    x = datetime.datetime.now()
    print(x.strftime("%d" "-" "%b" "-" "%y"))
    print(x.strftime("%I" ":" "%M" " " "%p")) 

    f3 = open(r'/Users/sajjkavinda/entries_mac.log', 'w') 

    os.chdir(r'/Users/sajjkavinda/Downloads/')

    for root, dirs, files in os.walk('/Users/sajjkavinda/Downloads/'):
        for file in files:
            if file.endswith(".pdf"):
                print(file)
                f3.write(file + "\n")
