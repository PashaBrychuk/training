def append_twice_bad(a, b):
	a = a+[b,b]
	return a
nums = [1,2,3]
append_twice_bad(nums, 7)
print nums

def append_twice_correct(a,b):
	nums.append(b)
	nums.append(b)
	return
nums = [1,2,3]
append_twice_correct(nums, 7)
print nums