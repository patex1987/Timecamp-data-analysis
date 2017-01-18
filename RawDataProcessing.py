import re
import os, errno


# SilentRemove - removes the file, if the file doesnt exist then skips the exception
# Useful at the initialisation of the program, to delete the previosuly created files
def SilentRemove(filename):
    try:
        os.remove(filename)
    except OSError as e: # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occured

# Divides the raw input file into 
def DivideIntoTimeAndData(fileName, origCharSeparator,newCharSeparator, origLevelSeparator, newLevelSeparator):
    SilentRemove("2_Times.txt")
    SilentRemove("3_Tasks.txt")
    with open(fileName, 'r') as fHandle:
        for line in fHandle:
            line.rstrip()
            print line.rstrip()
            strActRow = line.split(origCharSeparator)
            #print strActRow[0]
            with open("2_Times.txt","a") as fTimes:
                fTimes.write(newCharSeparator.join(strActRow[1:]))
            with open("3_Tasks.txt","a") as fTasks:
                fTasks.write(strActRow[0].replace(origLevelSeparator, newLevelSeparator) + "\n")
    return

strfileName = raw_input("Enter file name containing the raw report from TimeCamp: ")

DivideIntoTimeAndData(strfileName, ";",";","\xa0\xa0\xa0\xa0\xa0","|")
