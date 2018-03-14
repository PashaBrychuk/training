#find_time_missmatch.py


s = []
def find_time():
	
	with open('gw_messages.log') as f:
		for line in f:
			if "_time" in line:
				global s
				s.append(line)
				
	return s



find_time()


k= s[0]
print k[14:-4]


m=[]
for i in s:
	m.append(i[14:-4])
print m
print m[0]
#def compare_time(s):
#	return s


#print compare_time(s)