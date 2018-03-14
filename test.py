#Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

def arr(n):
	res = 0
	if len(n)<0:
		return 0
	for i in n :
		
		if i not in range(14,15):
			print i
			res = res +i 
			#print res
	return res




n= (1,2,3,4,5,6,13,13,14,12)
print arr(n)


def sum(n):
	s=0
	for i in n:
		s=s+i
	return s

print sum(n)



