#select.py
def returna_ll():
	with open("/home/pavlobrychuk/dev/temp/jour1.txt") as file:
		res=[]
		for line in file:
			if "TID-2145807-300005552" in line:
				res.append(line)
				print line
	new_file =	open("5552.txt", "w")	
	for item in res:
		new_file.write("%s\n" % item)
	return 0




print returna_ll()