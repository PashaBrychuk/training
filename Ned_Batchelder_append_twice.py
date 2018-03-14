"""#here is direct link to this video ion Youtube https://www.youtube.com/watch?v=_AEJHKGk9ns


def append_twice_bad(a, b):
	print id(a)
	a = a+[b,b]
	print id(a)
	return 
nums = [1,2,3]

s = append_twice_bad(nums, 7)
print s

def append_twice_correct(a,b):
	nums.append(b)
	nums.append(b)
	return
nums = [1,2,3]
append_twice_correct(nums, 7)
print nums
nums = 3
print id(nums)
other = nums
print id(other)
nums = 3+2
print id(nums)
print nums
print other"""
"""def string_match(a, b):
  c = 0
  for i in range(len(a)-1):
     print a[i:i+2]
     print b[i:i+2]
     if a[i:i+2]==b[i:i+2]:
      c = c+1
  return c



print string_match('abc', 'abc')"""

"""
a = "hello"
a = a.upper()
print a
"""

print True or False,
print True and False