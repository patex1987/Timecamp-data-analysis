import string
import re
import json
import jsonbyteify

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
			
def ReplaceCategoriesFromJson(strJsonFileName, dctWordCount):
	#dctReplaceCategories = json.loads(str(open(strJsonFileName).read()))
	dctReplaceCategories = jsonbyteify.json_loads_byteified(str(open(strJsonFileName).read()))
	for curWord in dctWordCount.keys():
		for mainCategory in dctReplaceCategories.keys():
			for replaceCategory in dctReplaceCategories[mainCategory]:
				if replaceCategory == curWord:
					#print mainCategory, replaceCategory, curWord, dctWordCount[mainCategory], dctWordCount[curWord]
					dctWordCount[mainCategory] = dctWordCount.get(mainCategory,0) + dctWordCount[curWord]
					del dctWordCount[replaceCategory]
					#print mainCategory, dctWordCount[mainCategory]
			
lstTasks = CreateListFromFile("3_Tasks.txt","|",r"""!"#$%&'()*+,./:;<=>?@[\]^`{|}~""")
dctWordCount = dict()

for task in lstTasks:
	dctWordCount[task] = dctWordCount.get(task,0) + 1

ReplaceCategoriesFromJson("CategoriesDictionary.json", dctWordCount)

#lstOrderedTasks = sorted([(occurence,task) for task,occurence in dctWordCount.items()],reverse=True)
lstOrderedTasks = sorted(dctWordCount.items(), key=lambda x:x[1],reverse=True)

with open("4_SimpleWordOccurence.txt","w") as outputFile:
	for val in lstOrderedTasks:		
			outputFile.write("\t".join([str(x) for x in val]) + "\n")