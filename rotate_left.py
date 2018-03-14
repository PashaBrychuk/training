def rotate_left(nums):
	z = nums[0]
	for i in range(len(nums)-1):
		z = nums[i]
		nums[i] = nums[i-1]
		nums[i-1] = z
	return nums

a = [1,2,3,4,5]
print rotate_left(a)