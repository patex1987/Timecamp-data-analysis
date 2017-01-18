import string
import re

def CreateListFromFile(strFileName, charLevelSeparator, lstRemoveChars):
	lstTasks = list()
	with open(strFileName,"r") as inputFile:
		for line in inputFile:
			#print line
			line = line.translate(None,charLevelSeparator)
			line = line.translate(string.maketrans(str(lstRemoveChars)," "*len(lstRemoveChars)))
			for word in line.split():
				if len(word)>1:
					if word[-1] in string.punctuation:
						word = word[:-1]
					if word[0] in string.punctuation:
						word = word[1:]
					lstTasks.append(word.lower())						
	return lstTasks
			
			
lstTasks = CreateListFromFile("3_Tasks.txt","|",r"""!"#$%&'()*+,./:;<=>?@[\]^`{|}~""")
dctWordCount = dict()

for task in lstTasks:
	dctWordCount[task] = dctWordCount.get(task,0) + 1

#lstOrderedTasks = sorted([(occurence,task) for task,occurence in dctWordCount.items()],reverse=True)
lstOrderedTasks = sorted(dctWordCount.items(), key=lambda x:x[1],reverse=True)

with open("SimpleWordOccurence.txt","w") as outputFile:
	for val in lstOrderedTasks:		
			outputFile.write("\t".join([str(x) for x in val]) + "\n")