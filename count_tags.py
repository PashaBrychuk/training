#count_tags.py



import os
#os.system("sudo -n scp 172.24.223.58:/home/root/check_output.txt /home/pavlobrychuk/training/")



sudoPassword = 'solYma8067'
command = 'sudo -n scp 172.24.223.58:/home/root/check_output.txt /home/pavlobrychuk/training/'
p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
def count_lines():

	count_TID_11280604_300005510=0,
	count_TID_11280604_300005512=0,
	count_TID_11280604_300005529=0,
	count_TID_11280604_300005530=0,
	count_TID_11280604_300005532=0,
	count_TID_11280604_300005533=0,
	count_TID_11280604_300005534=0,
	count_TID_11280604_300005535=0,
	count_TID_11280604_300005538=0,
	count_TID_11280604_300005540=0,
	count_TID_11280604_300005541=0,
	count_TID_11280604_300005542=0,
	count_TID_11280604_300005543=0,
	count_TID_11280604_300005546=0,
	count_TID_11280604_300005547=0,
	count_TID_11280604_300005548=0,
	count_TID_11280604_300005552=0
	s= [count_TID_11280604_300005510,count_TID_11280604_300005512,count_TID_11280604_300005529,count_TID_11280604_300005530,count_TID_11280604_300005532,count_TID_11280604_300005533,count_TID_11280604_300005534,count_TID_11280604_300005535,count_TID_11280604_300005538,count_TID_11280604_300005540,count_TID_11280604_300005541,count_TID_11280604_300005542,count_TID_11280604_300005543,count_TID_11280604_300005546,count_TID_11280604_300005547,count_TID_11280604_300005548,count_TID_11280604_300005552]
	

	for i in s:
		for line in open("/home/pavlobrychuk/training/check_output.txt", 'r'):
			if i in line






	return len(s)	


print count_lines()