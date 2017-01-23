import string
import re
import json

def json_load_byteified(file_handle):
    return _byteify(
        json.load(file_handle, object_hook=_byteify),
        ignore_dicts=True
    )

def json_loads_byteified(json_text):
    return _byteify(
        json.loads(json_text, object_hook=_byteify),
        ignore_dicts=True
    )

def _byteify(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data

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
	dctReplaceCategories = json_loads_byteified(str(open(strJsonFileName).read()))
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