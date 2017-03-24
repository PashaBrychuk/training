def no_teen_sum(a, b, c):
  return fix_teen(a)+fix_teen(b)+fix_teen(c)
def fix_teen(n):
  if n in range(13,20) and n not in range(15,17):
    return n
  return 0
    
