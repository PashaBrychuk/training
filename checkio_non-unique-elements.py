"""def checkio(data):
  return  [x for x in data if data.count(x) >= 2]
"""


def checkio(data):
	sum = []
	for i in range(len(data)):
		for j in range(1, len(data)-i):
				
				if data[i] == data[j]:
					print  "i", i
					print "j", j
					print "-----"
					sum.append(data[i])
	return sum
z = [1,2,3,2,1,1,1,1,1]
print checkio(z)


