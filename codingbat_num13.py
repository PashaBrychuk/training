def sum13(nums):
  s = 0
  for i in range(len(nums)-2):
    if nums[i]==13:
      nums.remove(nums[i])
      nums.remove(nums[i+1])
  for i in nums:
    s = s+i
  return s, nums


g = [1,2,2,1,13,134]
print sum13(g)