#selection_sort.py


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
print selection_sort(n)