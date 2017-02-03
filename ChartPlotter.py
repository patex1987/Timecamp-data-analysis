#import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import random
#print random.randint(0, 5)

MaxRow = 50

def LoadDataIntoLists(strFileName, charSeparator):
	lst2dTaskOccurences = [[],[]]
	with open(strFileName,"r") as inputFile:
		for line in inputFile:
			line = line.rstrip()
			vals = line.split(charSeparator)
			#print vals
			lst2dTaskOccurences[0].append(vals[0])
			lst2dTaskOccurences[1].append(vals[1])
	return lst2dTaskOccurences
 
lstPlotData = LoadDataIntoLists("7_WeightedWordOccurence.txt",'\t')
 
objects = lstPlotData[0][:MaxRow]
#y_pos = np.arange(len(objects))
y_spacing = range(len(objects))
performance = lstPlotData[1][:MaxRow]

#print y_spacing

plt.barh(y_spacing, performance, align='center', alpha=0.5)
plt.yticks(y_spacing, objects)
#plt.ylabel('Usage')
plt.title('Most occuring tasks')
plt.ylim(min(y_spacing)-1, max(y_spacing)+1)
plt.gca().invert_yaxis()

plt.show()