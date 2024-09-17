# Description :- create log file that contain info about running process

######################################################################
# importing requried package 
######################################################################
import os
import time
import psutil
from sys import *

######################################################################
# Function name :- CheckAbs
# Description :- check file path is related or absolute
# Input :- Path of directory
# Output :- True(file path is absolute) / False(file path is not absolute)
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def CheckAbs(DirName):
    result = os.path.isabs(DirName)
    return result

######################################################################
# Function name :- AbsolutePath
# Description :- create absolute path of directory
# Input :- Path of directory
# Output :- Absolute Path of directory
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def AbsolutePath(DirName):
    path = os.path.abspath(DirName)
    return path 

######################################################################
# Function name :- CheckDir
# Description :- check directory exists or not
# Input :- Absolute path of directory
# Output :- True(file path is exists) / False(file path is not exists)
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def CheckDir(DirName):
    result = os.path.exists(DirName)
    return result

######################################################################
# Function name :- CreateDir
# Description :- To create directory
# Input :- Absolute path of directory
# Output :- create specified directory
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def CreateDir(DirName):
    try:
        os.mkdir(DirName)
    except:
        pass

######################################################################
# Function name :- PrintResult
# Description :- write the info about running process into the log file
# Input :- Path of directory
# Output :- generate log file that contain info about running process
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def PrintResult(DirName,listprocess):
    
    flag = CheckAbs(DirName)
    if flag == False:
        DirName = AbsolutePath(DirName)

    exist = CheckDir(DirName)
    if(exist == False):
        CreateDir(DirName)
  
    log_path = os.path.join(DirName,"Marvellous.log")
    seperator = "-" * 150
    fobj = open(log_path,'w')
    fobj.write(seperator + "\n")
    fobj.write("Processor loger : "+time.ctime() + "\n")
    fobj.write(seperator + "\n") 
    for element in listprocess:
        fobj.write("%s\n"% element)

    fobj.write(seperator + "\n")
    fobj.write("Total numbers of running process is %s"%len(listprocess) + "\n")
    fobj.write(seperator + "\n")
    fobj.close()   

    print("Log file successfully generated at location %s" %(log_path)) 

######################################################################
# Function name :- ProcessDisplay
# Description :- create a list which contain info about running process
# Input :- Nothing
# Output :- generate list
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def ProcessDisplay():
    listprocess = []
    
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
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
            print("This Automation Script is ues for Display Information(name PID and Users) of all running Process")
            exit()  

        elif(((argv[1]) == "-u") or ((argv[1]) == "-U")):
            print("Usage : Name_of_Scrpit Absolute_path_of_Directory")
            print("Example : ProcInfoLog.py Anuraj")
            exit()

        else:
            list1 = list()
            list1 = ProcessDisplay()
            PrintResult(argv[1],list1)
            
    else:
        print("Error : Invalid Numbers of Arguments")
        exit()

######################################################################
# Application stater
######################################################################
if __name__ == "__main__":
    main()    