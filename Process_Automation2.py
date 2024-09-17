######################################################################
# importing requried package 
######################################################################
import psutil
from sys import *

######################################################################
# Function name :- ProcessDisplay
# Description :- create a list which contain info about running process
# Input :- Nothing
# Output :- generate list
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def ProcessDisplay():
    listprocess = list()   
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
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

    if(len(argv) ==  2):
        if(argv[1] == "-h" or argv[1] == "-H"): # help
            print("This automation script is ues for display information of running proceesses as its name, PID, Username")
            exit()

        elif(argv[1] == "-u" or argv[1] == "-U"): # Usage
            print("Usage : Name_of_script ")
            print("Example : Process_Automation1.py")
            exit()    
        else:
            print("There is such option to handle")
            exit()

    
    elif(len(argv) == 1):
        list1 = list()
        list1 = ProcessDisplay()
        for element in list1:
            print(element)           
        print("Total Numbers of running process : ",len(list1))

    else:
        print("Error : Invaild numbers of arguments")
        exit()   

######################################################################
# Application stater
######################################################################
if __name__ == "__main__":
    main()    