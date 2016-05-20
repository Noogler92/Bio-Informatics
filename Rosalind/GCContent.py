from collections import Counter
from Bio import SeqIO
def determineGCCount(dnaString):
	count = Counter(dnaString)
	cCount = count['C']
	gCount = count['G']
	percentage = (gCount+cCount)/ len(dnaString)
	return percentage * 100


string = []
recordID = []
testDict = {}
with open("rosalind_gc.txt") as f:
	for record in SeqIO.parse(f, "fasta"):
		string.append("{}".format(record.seq))
		recordID.append(record.id)
f.close()

for x in range(0,len(string)):
	test = string[x]
	testDict.update({recordID[x]:determineGCCount(test)})

#print(string)
#print(recordID)
print(testDict)
