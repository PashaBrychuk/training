def count_file_lines():
	s=0
	z=[]
	with open("tags.txt", "r") as file:
		for line in file:

			z.append((line.split( )[7]))
			s=s+1

	file = open("testfile.txt","w") 
	for i in z:
		file.write(i+ '\n')
	return file


print count_file_lines()