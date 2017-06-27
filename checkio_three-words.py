def checkio(words):
	s = 0
	print type(words)
	g =  words.split()
	print type(g)
	for i in g:
		print i
		if i.isalpha() == True:
			s = s+1
			print s
		else:
			s = 0
		if s >=3:
			return True
	return False

print checkio("Hello World PAsha 2")