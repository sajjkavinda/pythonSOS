# K.G.S.K. Kirindeniya | IT20614058 | Y2S1 CS

import platform, os
import datetime, time

#platform information
plat = "Platform: " + platform.platform() + "\n"
print (plat)

a = platform.system() #platform type extract

if (a == "Linux"): #check the platform type

    #initialize , sort and print the system time and year
    x = datetime.datetime.now()
    timeL  = x.strftime("%a %b %m %H:%M:%S")
    timezone = time.strftime(str(time.timezone))
    year = x.strftime("%Y")

    f1 = open(os.path.expanduser("~/Desktop/Entries_Lin.log"), "w") #create a log file to write details

    f1.write(plat + "\n" + timeL + timezone + year + "\n \n") #write the platform date and time details in the log file
    
    os.chdir(r"/usr/lib/")
    
    #access folders and subfolders in /usr/lib path -> print in the shell and write into the log file
    details = os.popen('sudo find /lib/ -name "*.bin" -type f')
    
    for records in details:
        f1.write(records)

elif (a == "Windows"): #check the platform type

    #initialize , sort and print the system time
    x = datetime.datetime.now()
    timeW1 = x.strftime("%d" "-" "%b" "-" "%y")
    timeW2 = x.strftime("%I" ":" "%M" " " "%p")

    f2 = open(os.path.expanduser("~\Desktop\Entries_Win10.log"), "w") #create a log file to write details

    f2.write(plat + "\n" + timeW1 + "\n" + timeW2 + "\n") #write the platform, date and time details in the log file

    details = os.popen('cmd /k "dir C:\\Windows\system32\*.exe"') #run the shell command for sort out .exe files

    #print and redirect the shell output
    for records in details:
        f2.write(records)
