import re
import HelpFunctions

# Divides the raw input file into 
def DivideIntoTimeAndData(fileName, origCharSeparator,newCharSeparator, origLevelSeparator, newLevelSeparator):
    HelpFunctions.SilentRemove("2_Times.txt")
    HelpFunctions.SilentRemove("3_Tasks.txt")
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
