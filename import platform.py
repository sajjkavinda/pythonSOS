import platform
import os
import datetime

print("Platform: " + platform.platform())

a = platform.system()
if (a == "Linux"):
    x = datetime.datetime.now()
    print(x.strftime("%c"))

elif (a == "Windows"):

    x = datetime.datetime.now()
    print(x.strftime("%d" "-" "%b" "-" "%y"))
    print(x.strftime("%I" ":" "%M" " " "%p"))