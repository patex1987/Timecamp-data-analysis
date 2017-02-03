from itertools import izip

def JoinFiles(strTaskFile, strTimeFile,charSeparator, strOutputFile):
	with open(strOutputFile, 'w') as fOut, open(strTaskFile) as fIn1, open(strTimeFile) as fIn2:
		for line1, line2 in zip(fIn1, fIn2):
			fOut.write(("{}" + charSeparator + "{}\n").format(line1.rstrip(), line2.rstrip()))
			
JoinFiles("3_Tasks.txt","5_Converted_Time.txt",";","6_Recombination.txt")