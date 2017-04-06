def close_far(a, b, c):
  if isFar(a,b) and  isFar(a,c) or isFar(b,c):
    return True
  """if isFar(a,c) and not isFar(a,b) or not isFar(b,c):
          return True
        if isFar(b,c) and not isFar(a,b) or not isFar(a,c):
          return True"""
  return False
def isFar(n,m):
  s = abs(n)- abs(m) in range(-1,2)
  return s
    

print False and True