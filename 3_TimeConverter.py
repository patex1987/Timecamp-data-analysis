import re
from datetime import timedelta
import time
import HelpFunctions

# opens the file containing the times in string format and saves it into the new file
def ConvertTimeStringToDateTime(strFileName, charDataSeparator, isTimeStringFormat,strOutputFileName):
	intLineCounter=0
	with open(strFileName,"r") as fileInputTime:
		with open(strOutputFileName,"a") as fileOutputTime:
			
			for line in fileInputTime:
				intLineCounter+=1
				strWriteData = ""
				lineDatas = line.rstrip().replace("-","0").split(";")
				print lineDatas
				if intLineCounter>1:
					if isTimeStringFormat:
						strWriteData = charDataSeparator.join([str("{0:.2f}".format(to_timedelta(x).total_seconds()/60)) for x in lineDatas])
					else:
						pass #This part needs to be changed
				else:
					strWriteData = line.rstrip()
				print strWriteData
				fileOutputTime.write(strWriteData + "\n")
			

# This method converts time stored in string format to timedelta object
# E.g. "150h 30m 15s" to 150:30:15 
def to_timedelta(time_string):
	if time_string == "0":
		return timedelta(seconds=0)
	else:
		units = {'h': 'hours', 'd': 'days', 'm': 'minutes', 's': 'seconds'}
		#print {units[x[-1]]: int(x[:-1]) for x in time_string.split()}
		return timedelta(**{units[x[-1]]: int(x[:-1]) for x in time_string.split()})
		

strOutputFileName="5_Converted_Time.txt"
HelpFunctions.SilentRemove(strOutputFileName)
ConvertTimeStringToDateTime("2_Times.txt",";",True,strOutputFileName)
