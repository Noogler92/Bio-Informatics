
def rabbitPairs(months,rabbits):
	#print(months)
	if months is 1:
		return 1
	elif months is 2:
		return rabbits

	genOne = rabbitPairs(months-1, rabbits)
	
	genTwo = rabbitPairs(months-2, rabbits)
	#print("Gen 1",genOne)
	#print("Gen 2", genTwo)
	

	if months <=4:
		#print("Sum",genOne + genTwo)
		return genOne + genTwo
	#print(genOne +(genTwo * rabbits))
	return genOne +(genTwo * rabbits)


print(rabbitPairs(34,4))