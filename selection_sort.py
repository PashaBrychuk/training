""""#selection_sort.py


def selection_sort(nums):
	#tmp = nums[0]
	for i in range(1, len(nums)):
		for j in range(i, len(nums)):
			print j
			tmp = nums[0]
			if nums[i]<tmp:
			
				tmp = nums[i]
			nums[i] = tmp
	return nums


n = [3,2,4,7,1, -124,3,8]
print selection_sort(n)"""


"""def selection_sort(seq):
    for i in range(len(seq)):
        position = i
        for j in range(i,len(seq)):
            if seq[position] > seq[j]:
                position = j
        if position != i:
            tmp = seq[position]
            seq[position] = seq[i]
            seq[i] = tmp
    return seq



seq = [3,2,4,7,1, -124,3,8]
print selection_sort(seq)"""



a = 5
if a ==5:
	a = 6
print a