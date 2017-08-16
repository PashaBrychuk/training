s=[]
res=[]
for line in open('top_results.txt','r'):
	print line
	
	s.append(line)
				
	for i in s:
		g=i.split(" ")
		res.append(g)
print res
						