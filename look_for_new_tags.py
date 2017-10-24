#count_tags.py
def looking_for_tag_with_status_new():
	c = 0
	for line in open("/home/pavlobrychuk/training/file_mosquitto1.txt", 'r'):
			if  "batterylevel" in line:
				print line
				c =c +1
	return c


print looking_for_tag_with_status_new()