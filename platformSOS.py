import platform
import os
import datetime

plat = "Platform: " + platform.platform()

a = platform.system()
if (a == "Linux"):
    x = datetime.datetime.now()
    timeL  = x.strftime("%c")
    print (timeL)

    f1 = open(r'root/Desktop/entries_Lin.log', 'w')

    os.chdir(r'/lib')

    f1.write(plat + "\n" + timeL + "\n")

    for root, dirs, files in os.walk("/usr/lib"):
        for file in files:
            if file.endswith(".bin"):
                print(file)
                f1.write(file + "\n")

elif (a == "Windows"):

    x = datetime.datetime.now()
    timeW1 = x.strftime("%d" "-" "%b" "-" "%y")
    timeW2 = x.strftime("%I" ":" "%M" " " "%p")
    print(timeW1  + "\n" + timeW2)

    f2 = open(r'C:\Desktop\entries_Win10.log', 'w') 

    os.chdir(r'C:\Windows\system32')

    f2.write(plat + "\n" + timeW1 + "\n" + timeW2 + "\n" )

    for root, dirs, files in os.walk("C:\Windows\system32"):
        for file in files:
            if file.endswith(".exe"):
                print(file)
                f2.write(file + "\n")

elif (a == "Darwin"):

    x = datetime.datetime.now()
    mactime = x.strftime("%d" "-" "%b" "-" "%y")
    mactime2 = x.strftime("%I" ":" "%M" " " "%p")
    print(mactime + "\n" + mactime2)

    f3 = open(r'/Users/sajjkavinda/entries_mac.log', 'w') 

    os.chdir(r'/Users/sajjkavinda/Downloads/')

    f3.write(plat + "\n" + mactime + "\n" + mactime2 + "\n" )

    for root, dirs, files in os.walk('/Users/sajjkavinda/Downloads/'):
        for file in files:
            if file.endswith(".pdf"):
                print(file)
                f3.write(file + "\n")
