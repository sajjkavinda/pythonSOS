# K.G.S.K. Kirindeniya | IT20614058 | Y2S1 CS

import platform, os
import datetime, time

#platform information
plat = "Platform: " + platform.platform() + "\n"
print (plat)

a = platform.system() #platform type extract

if (a == "Linux"): #check the platform type

    #initialize , sort and print the system time
    x = datetime.datetime.now()
    timeL  = x.strftime("%a %b %m %H:%M:%S" , str(time.timezone), "%Y")
    #timezone = time.strftime(str(time.timezone))
    #year = x.strftime("%Y")
    print (timeL + "\n")

    f1 = open(os.path.expanduser("~/Desktop/Entries_Lin.log"), "w") #create a log file to write details

    f1.write(plat + "\n" + timeL + "\n \n") #write the platform date and time details in the log file

    #access folders and subfolders in /usr/lib path -> print in the shell and write into the log file
    for root, dirs, files in os.walk("/usr/lib/"):
        for file in files:
            if file.endswith(".bin"): 
                print(os.getcwd() + ("/" + file)) 
                f1.write(os.getcwd() + "/" + file + "\n")

elif (a == "Windows"): #check the platform type

    #initialize , sort and print the system time
    x = datetime.datetime.now()
    timeW1 = x.strftime("%d" "-" "%b" "-" "%y")
    timeW2 = x.strftime("%I" ":" "%M" " " "%p")
    print(timeW1 + "\n" + timeW2 + "\n")

    f2 = open(os.path.expanduser("~\Desktop\Entries_Win10.log"), "w") #create a log file to write details

    f2.write(plat + "\n" + timeW1 + "\n" + timeW2 + "\n") #write the platform, date and time details in the log file

    details = os.popen('cmd /k "dir C:\\Windows\system32\*.exe"') #run the shell command for sort out .exe files

    #print and redirect the shell output
    for records in details:
        print(details)
        f2.write(details)

    #details = os.system('cmd /k "dir C:\\Windows\system32\*.exe"')

    '''for root, dirs, files in os.walk("C:\Windows\system32"):
        for file in files:
            if file.endswith(".exe"):
                a = str(os.path.getsize(file))
                b = str(time.ctime(os.path.getctime(file)))
                print(b + a.rjust(10) + " " + file)
                f2.write(b + a.rjust(10) + " " + file + "\n")'''

elif (a == "Darwin"):

    x = datetime.datetime.now()
    mactime = x.strftime("%d" "-" "%b" "-" "%y" "\n" "%I" ":" "%M" " " "%p")
    #print(mactime + "\n" + "\n Directries of C:\Windows\system32 \n")

    y = datetime.datetime.now()
    timeL  = x.strftime("%a %b %m %H:%M:%S")
    timezone = time.timezone
    year = x.strftime("%Y")
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