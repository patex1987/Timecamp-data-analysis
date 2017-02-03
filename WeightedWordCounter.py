import string
import re
import json
import jsonbyteify

def CreateListFromFile(strFileName, charLevelSeparator, lstRemoveChars, charSeparator):
	lstTasks = list()
	with open(strFileName,"r") as inputFile:
		for line in inputFile:
			lineDatas = line.rstrip().split(charSeparator)
			#print lineDatas
			#print line
			tasks = lineDatas[0].translate(None,charLevelSeparator)
			tasks = tasks.translate(string.maketrans(str(lstRemoveChars)," "*len(lstRemoveChars)))
			for word in tasks.split():
				if len(word)>1:
					if word[-1] in string.punctuation:
						word = word[:-1]
					if word[0] in string.punctuation:
						word = word[1:]
					lstTasks.append([word.lower(),lineDatas[1]])						
	return lstTasks

def DelTasksFromDict(strJsonFileName, dctWordCount):
	lstDeleteCategories = jsonbyteify.json_loads_byteified(str(open(strJsonFileName).read()))
	for curWord in dctWordCount.keys():
		if curWord in lstDeleteCategories:
			#print curWord
			del dctWordCount[curWord]
	
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
			
lstTasks = CreateListFromFile("6_Recombination.txt","|",r"""!"#$%&'()*+,./:;<=>?@[\]^`{|}~""",";")[1:-1]
dctWordCount = dict()

#print lstTasks

for task in lstTasks:
	dctWordCount[task[0]] = dctWordCount.get(task[0],0) + float(task[1])

for key in dctWordCount:
	dctWordCount[key] = dctWordCount[key]/(60*8)
	
#print dctWordCount

DelTasksFromDict("CategoriesToDelete.json",dctWordCount)
ReplaceCategoriesFromJson("CategoriesDictionary.json", dctWordCount)

lstOrderedTasks = sorted(dctWordCount.items(), key=lambda x:x[1],reverse=True)

print lstOrderedTasks

with open("7_WeightedWordOccurence.txt","w") as outputFile:
	for val in lstOrderedTasks:		
			outputFile.write("\t".join([str(x) for x in val]) + "\n")