

import os
#os.system("sudo -n scp 172.24.223.58:/home/root/check_output.txt /home/pavlobrychuk/training/")



sudoPassword = 'solYma8067'
command = 'sudo -n scp 172.24.223.58:/home/root/check_output.txt /home/pavlobrychuk/training/'
p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
def count_lines():

	s = []
	count_TID_11280604_300005510=0
	count_TID_11280604_300005512=0
	count_TID_11280604_300005529=0
	count_TID_11280604_300005530=0
	count_TID_11280604_300005532=0
	count_TID_11280604_300005533=0
	count_TID_11280604_300005534=0
	count_TID_11280604_300005535=0
	count_TID_11280604_300005538=0
	count_TID_11280604_300005540=0
	count_TID_11280604_300005541=0
	count_TID_11280604_300005542=0
	count_TID_11280604_300005543=0
	count_TID_11280604_300005546=0
	count_TID_11280604_300005547=0
	count_TID_11280604_300005548=0
	count_TID_11280604_300005552=0
	for line in open("/home/pavlobrychuk/training/check_output.txt", 'r'):
		

		if "5510" in line:
			count_TID_11280604_300005510 = count_TID_11280604_300005510+1 

		if "5512" in line:
			count_TID_11280604_300005512 = count_TID_11280604_300005512+1 

		if "5529" in line:
			count_TID_11280604_300005529 = count_TID_11280604_300005529+1 

		if "5530" in line:
			count_TID_11280604_300005530 = count_TID_11280604_300005530+1

		if "5532" in line:
			count_TID_11280604_300005532 = count_TID_11280604_300005532+1 

		if "5533" in line:
			count_TID_11280604_300005533 = count_TID_11280604_300005533+1

		if "5534" in line:
			count_TID_11280604_300005534 = count_TID_11280604_300005534+1 

		if "5535" in line:
			count_TID_11280604_300005535 = count_TID_11280604_300005535+1 

		if "5538" in line:
			count_TID_11280604_300005538 = count_TID_11280604_300005538+1 

		if "5540" in line:
			count_TID_11280604_300005540 = count_TID_11280604_300005540+1 

		if "5541" in line:
			count_TID_11280604_300005541 = count_TID_11280604_300005541+1 

		if "5542" in line:
			count_TID_11280604_300005542 = count_TID_11280604_300005542+1 

		if "5543" in line:
			count_TID_11280604_300005543 = count_TID_11280604_300005543+1

		if "5546" in line:
			count_TID_11280604_300005546 = count_TID_11280604_300005546+1 

		if "5547" in line:
			count_TID_11280604_300005547 = count_TID_11280604_300005547+1 

		if "5548" in line:
			count_TID_11280604_300005548 = count_TID_11280604_300005548+1 

		if "5552" in line:
			count_TID_11280604_300005552 = count_TID_11280604_300005552+1 
	s.append(count_TID_11280604_300005510)
	s.append(count_TID_11280604_300005512)
	s.append(count_TID_11280604_300005529)
	s.append(count_TID_11280604_300005530)
	s.append(count_TID_11280604_300005532)
	s.append(count_TID_11280604_300005533)
	s.append(count_TID_11280604_300005534)
	s.append(count_TID_11280604_300005535)
	s.append(count_TID_11280604_300005538)
	s.append(count_TID_11280604_300005540)
	s.append(count_TID_11280604_300005541)
	s.append(count_TID_11280604_300005542)
	s.append(count_TID_11280604_300005543)
	s.append(count_TID_11280604_300005546)
	s.append(count_TID_11280604_300005547)
	s.append(count_TID_11280604_300005548)
	s.append(count_TID_11280604_300005552)
	#print s
	#print  max(s)
	#print min(s)

	"""if "error" in line:
									print line
									d = d+1
	return "there were %s lines with error in file drd.txt" %d """
	print "*****************************************************"
	print  "10"+" ", "12"+" " , "29"+" " , "30"+ " " , "32"+" ",  "33"+ " ", "34"+" ", "35"+" ", "38" + " ", "40"+ " ", "41"+" ", "42"+" ", "43" + " ", "46"+" ", "47"+" ", "48"+" ", "52"+" "
	print count_TID_11280604_300005510, count_TID_11280604_300005512,count_TID_11280604_300005529,count_TID_11280604_300005530,count_TID_11280604_300005532,count_TID_11280604_300005533,count_TID_11280604_300005534,count_TID_11280604_300005535,count_TID_11280604_300005538,count_TID_11280604_300005540,count_TID_11280604_300005541,count_TID_11280604_300005542, count_TID_11280604_300005543,count_TID_11280604_300005546,count_TID_11280604_300005547,count_TID_11280604_300005548,count_TID_11280604_300005552
	return "end of count on app side"
#	print "5510-%s, 5512-%s, 5529-%s, 5530-%s, 5532-%s, 5533-%s, 5534-%s, 5535-%s, 5538-%s, 5540-%s, 5541-%s, 5542-%s, 5543-%s, 5546-%s, 5547-%s, 5548-%s, 5552-%s" %count_TID_11280604_300005510, %count_TID_11280604_300005512,%count_TID_11280604_300005529,%count_TID_11280604_300005530,%count_TID_11280604_300005532,%count_TID_11280604_300005533,%count_TID_11280604_300005534,%count_TID_11280604_300005535,%count_TID_11280604_300005538,%count_TID_11280604_300005540,%count_TID_11280604_300005541,%count_TID_11280604_300005542, %count_TID_11280604_300005543,%count_TID_11280604_300005546,%count_TID_11280604_300005547,%count_TID_11280604_300005548,%count_TID_11280604_300005552

print count_lines()

def count_lines2():

	s = []
	count_TID_11280604_300005510=0
	count_TID_11280604_300005512=0
	count_TID_11280604_300005529=0
	count_TID_11280604_300005530=0
	count_TID_11280604_300005532=0
	count_TID_11280604_300005533=0
	count_TID_11280604_300005534=0
	count_TID_11280604_300005535=0
	count_TID_11280604_300005538=0
	count_TID_11280604_300005540=0
	count_TID_11280604_300005541=0
	count_TID_11280604_300005542=0
	count_TID_11280604_300005543=0
	count_TID_11280604_300005546=0
	count_TID_11280604_300005547=0
	count_TID_11280604_300005548=0
	count_TID_11280604_300005552=0
	for line in open("/home/pavlobrychuk/log.txt", 'r'):
		

		if "5510" in line:
			count_TID_11280604_300005510 = count_TID_11280604_300005510+1 

		if "5512" in line:
			count_TID_11280604_300005512 = count_TID_11280604_300005512+1 

		if "5529" in line:
			count_TID_11280604_300005529 = count_TID_11280604_300005529+1 

		if "5530" in line:
			count_TID_11280604_300005530 = count_TID_11280604_300005530+1

		if "5532" in line:
			count_TID_11280604_300005532 = count_TID_11280604_300005532+1 

		if "5533" in line:
			count_TID_11280604_300005533 = count_TID_11280604_300005533+1

		if "5534" in line:
			count_TID_11280604_300005534 = count_TID_11280604_300005534+1 

		if "5535" in line:
			count_TID_11280604_300005535 = count_TID_11280604_300005535+1 

		if "5538" in line:
			count_TID_11280604_300005538 = count_TID_11280604_300005538+1 

		if "5540" in line:
			count_TID_11280604_300005540 = count_TID_11280604_300005540+1 

		if "5541" in line:
			count_TID_11280604_300005541 = count_TID_11280604_300005541+1 

		if "5542" in line:
			count_TID_11280604_300005542 = count_TID_11280604_300005542+1 

		if "5543" in line:
			count_TID_11280604_300005543 = count_TID_11280604_300005543+1

		if "5546" in line:
			count_TID_11280604_300005546 = count_TID_11280604_300005546+1 

		if "5547" in line:
			count_TID_11280604_300005547 = count_TID_11280604_300005547+1 

		if "5548" in line:
			count_TID_11280604_300005548 = count_TID_11280604_300005548+1 

		if "5552" in line:
			count_TID_11280604_300005552 = count_TID_11280604_300005552+1 
	s.append(count_TID_11280604_300005510)
	s.append(count_TID_11280604_300005512)
	s.append(count_TID_11280604_300005529)
	s.append(count_TID_11280604_300005530)
	s.append(count_TID_11280604_300005532)
	s.append(count_TID_11280604_300005533)
	s.append(count_TID_11280604_300005534)
	s.append(count_TID_11280604_300005535)
	s.append(count_TID_11280604_300005538)
	s.append(count_TID_11280604_300005540)
	s.append(count_TID_11280604_300005541)
	s.append(count_TID_11280604_300005542)
	s.append(count_TID_11280604_300005543)
	s.append(count_TID_11280604_300005546)
	s.append(count_TID_11280604_300005547)
	s.append(count_TID_11280604_300005548)
	s.append(count_TID_11280604_300005552)
	#print s
	#print  max(s)
	#print min(s)

	"""if "error" in line:
									print line
									d = d+1
	return "there were %s lines with error in file drd.txt" %d """
	print "*****************************************************"
	#print  "10"+" "*(len(str(count_TID_11280604_300005510)))-1, "12"+" " , "29"+" ", "30"+ " " , "32"+" ",  "33"+ " ", "34"+" ", "35"+" ", "38" + " ", "40"+ " ", "41"+" ", "42"+" ", "43" + " ", "46"+" ", "47"+" ", "48"+" ", "52"+" "
	print count_TID_11280604_300005510, count_TID_11280604_300005512,count_TID_11280604_300005529,count_TID_11280604_300005530,count_TID_11280604_300005532,count_TID_11280604_300005533,count_TID_11280604_300005534,count_TID_11280604_300005535,count_TID_11280604_300005538,count_TID_11280604_300005540,count_TID_11280604_300005541,count_TID_11280604_300005542, count_TID_11280604_300005543,count_TID_11280604_300005546,count_TID_11280604_300005547,count_TID_11280604_300005548,count_TID_11280604_300005552
	#print "10"+ " "*(len(str(count_TID_11280604_300005510)))-1
	return "end of count on broker side"
print count_lines2()