import platform, os
import datetime, time

plat = "Platform: " + platform.platform()

a = platform.system()
if (a == "Linux"):
    x = datetime.datetime.now()
    timeL  = x.strftime("%a %b %m %H:%M:%S")
    timezone = time.timezone
    year = x.strftime("%Y \n")
    print (timeL + " "+ timezone + " " + year + "\n")

    f1 = open(r'root/Desktop/entries_Lin.log', 'w')

    os.chdir(r'/lib')

    f1.write(plat + "\n" + timeL + "\n")

    for root, dirs, files in os.walk("/usr/lib"):
        for file in files:
            if file.endswith(".bin"):
                print(os.getcwd() + (file))
                f1.write(os.getcwd() + file + "\n")

elif (a == "Windows"):

    x = datetime.datetime.now()
    timeW1 = x.strftime("%d" "-" "%b" "-" "%y")
    timeW2 = x.strftime("%I" ":" "%M" " " "%p")
    print(timeW1  + "\n" + timeW2 +"\n" + "\n Directries of C:\Windows\system32 \n")

    f2 = open(r'C:\\Desktop\entries_Win10.log', 'w')

    os.chdir(r'C:\Windows\system32')


    #f2.write(plat + "\n" + timeW1 + "\n" + timeW2 + "\n" + "Directries of C:\Windows\system32 \n" + "\n")

    for root, dirs, files in os.walk("C:\Windows\system32"):
        for file in files:
            if file.endswith(".exe"):
                a = str(os.path.getsize(file))
                b = str(time.ctime(os.path.getctime(file)))
                print(b + a.rjust(10) + " " + file)
                f2.write(b + a.rjust(10) + " " + file + "\n")

elif (a == "Darwin"):

    x = datetime.datetime.now()
    mactime = x.strftime("%d" "-" "%b" "-" "%y" "\n" "%I" ":" "%M" " " "%p")
    #print(mactime + "\n" + "\n Directries of C:\Windows\system32 \n")

    y = datetime.datetime.now()
    timeL  = x.strftime("%a %b %m %H:%M:%S")
    timezone = time.timezone
    year = x.strftime("%Y \n")
    print (timeL , timezone , year , "\n")
    #print(x.strftime('%a %b %m %H:%M:%S')), time.timezone , x.strftime( '%Y')

    f3 = open(r'/Users/sajjkavinda/entries_mac.log', 'w') 

    os.chdir(r'/Users/sajjkavinda/Downloads/')

    f3.write(plat + "\n" + mactime + "\n") 

    for root, dirs, files in os.walk('/Users/sajjkavinda/Downloads/'):
        for file in files:
            if file.endswith(".pdf"):
                a = str(os.path.getsize(file))
                b = str(time.ctime(os.path.getctime(file)))
                print( b + a.rjust(10) + " " + file)
                f3.write( b + a.rjust(10) + " " + file + "\n")
