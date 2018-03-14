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
#print k[14:-4]


m=[]
for i in s:
	m.append(i[14:-4])

setb= set(m)
print len(m)
print "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
#print m
#print m[0]

from datetime import datetime
dates = [datetime.strptime(i, "%Y-%m-%dT%H:%M:%S") for i in m]
print dates


seta=set(dates)
print len(seta)
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
final=[]
for d in dates:
	
	#d.toordinal()
	final.append(d.toordinal())

print final

#def compare_time(s):
#	return s


#print compare_time(s)

print "counter on duplicated messages"
print len(m) - len (setb)