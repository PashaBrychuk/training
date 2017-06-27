def centered_average(nums):
  s = 0
  b =[]
  for i in range(len(nums)):
    if nums[i] not in b:
      b.append(nums[i])
  smallest = b[0]
  biggest  = b[0]
  for i in range(len(b)):
    if b[i]<smallest:
      small = b[i]
    if b[i]>biggest:
      biggest = b[i]
  b.remove(biggest)
  b.remove(smallest)
  for i in b:
    s = s+i
  return s, b
  
nums = [1,2,3,4,5,6,7,2,2,2,2,2]
print centered_average(nums)