import psutil
from sys import *

######################################################################
# Function name :- ProcessDisplay
# Description :- create a list which contain info about running process
# Input :- Name of process
# Output :- generate list
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def ProcessDisplay(name):
    listprocess = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            if name.lower() in pinfo['name'].lower():
                listprocess.append(pinfo)

        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listprocess

######################################################################
# Function name :- main
# Description :- Main function from where execution starts
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def main():
    print("--------Process Automation using Python--------")
    print("Script Name :",argv[0])

    if(len(argv) == 2):
        if(((argv[1]) == "-H") or ((argv[1]) == "-h")):
            print("This Automation Script is ues for Display Information(name PID and Users) of process if it is running")
            exit()  

        elif(((argv[1]) == "-u") or ((argv[1]) == "-U")):
            print("Usage : Name_of_script Name_of_process")
            print("Example : ProcSreach.py Notepad")
            exit()
        else:
            list1 = []
            list1 = ProcessDisplay(argv[1])
            if(len(list1) == 0):
                print(argv[1],"is not currently running.")
            else:
                for element in list1:
                    print(element)  

    else:
        print("Error : Invalid Numbers of Arguments")
        exit()

######################################################################
# Application stater
######################################################################          
if __name__ == "__main__":
    main()    