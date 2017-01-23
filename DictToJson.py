import json



		
fileStr = str(open('CategoriesDictionary.json').read())
data = json.loads(fileStr)

print data
#print d

for key in data.keys():
	print data[key]