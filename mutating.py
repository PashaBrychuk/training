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

print "*"*25

#append twice good mutates argument
def append_twice_good(alist, val,za):
	alist.append(val)
	alist.append(val)
	return za
z = [1,2,3]
append_twice_good(z, 7, 8)
print z

print "*"*25

#append twice bad   useless 
def append_twice_bad(blist, val):
	blist = blist+[val, val]
	return
c = [1,2,3]
append_twice_bad(c, 7)
print c

print "-----"*5
def append_twice_bad_fixed(blist, val):
	blist = blist+[val, val]
	print "inside", blist
	return blist
g = [1,2,3]
g = append_twice_bad_fixed(g, 7)
print g