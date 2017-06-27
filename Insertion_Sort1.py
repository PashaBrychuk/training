def insert(list):
	for index in range(1, len(list)):
		value = list[index]
		i = index-1
		while i>=0:
			if value<list[i]:
				list[i+1] = list[i]
				list[i] = value
				i = i-1
	return list
print insert([3,2,1,-176])