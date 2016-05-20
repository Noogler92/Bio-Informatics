
def recurrence(n,a):
	if n == 0 or n == 1:
		return n
	else:
		return recurrence(n-1) + recurrence(a)


print(recurrence(5-1,3) + (5-2,3))
