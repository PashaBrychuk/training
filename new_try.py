#new_try.py





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


print len(m)

import dateutil.parser as dp
stasya=[]
number_of_mismatched=0
m.sort()
for i in m:
	parsed_i = dp.parse(i)
	#print parsed_i
	t_in_seconds = parsed_i.strftime('%s')
	stasya.append(t_in_seconds)

#print stasya


for i in range(len(stasya)-1):

	if int(stasya[i+1])-int(stasya[i]) not in range(110,131):
		print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
		print stasya[i]
		print stasya[i+1]

		print "Number of suspicious times is:"
		number_of_mismatched=number_of_mismatched+1

print number_of_mismatched
""">>> t = '1984-06-02T19:05:00.000Z'
>>> parsed_t = dp.parse(t)
>>> t_in_seconds = parsed_t.strftime('%s')"""