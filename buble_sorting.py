def sort(n):
	for j in range(0,len(n)):
		for i in range(len(n)-j-1):
			tmp = 0
			if n[i+1]<n[i]:
				tmp = n[i+1]
				n[i+1] = n[i]
				n[i] = tmp
	return n


n = [3,2,4,7,1, -124,3,8]
print sort(n)