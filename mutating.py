#rebinding
s = 1
print id(s)
b = s
s = 2
print id(s)
print s
print b



print "*"*25
#mutating
s = [1,2,3]
print id(s)
b = s
s.append(4)
print id(s)
print s
print b

print "*"*25

nums = [1,2,3]
for x in nums:
	x = x*10
	print x
	print "inside ", nums
print "outside ", nums


print "*"*25

nums = [1,2,3]
for x in range(len(nums)):
	nums[x] = nums[x]*10
	print "inside ", nums
print "outside ", nums