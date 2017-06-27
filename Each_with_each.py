names = ["Pasha", "Dasha", "Masha"]
numbers = [1,2,3]
result_list = []
for name in range(len(names)):
	for number in range(len(numbers)):
		result_list.append((name, number))

print result_list
