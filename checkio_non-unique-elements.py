"""def checkio(data):
  return  [x for x in data if data.count(x) >= 2]
"""


def checkio(data):
	sum = []
	for i in range(len(data)):
		for j in range (i+1, len(data)):
				if data[i] == data[j]:
					if data[i] not in sum:
						print  "i", i
						print "j", j
						print "-----"
						sum.append(data[i])
					
	return sum
z = [1,2,3,1,3]
print checkio(z)


