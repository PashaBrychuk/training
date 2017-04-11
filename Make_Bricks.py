"""def make_bricks(small, big, goal):
  for i in range(1,big+1):
    if i*5+small==goal:
      return True
    if i*5 ==goal:
      return True
  return False

"""



def make_bricks(small, big, goal):
	if big !=0:
		for i in range(1,big+1):
			for j in range(0,small+1):
				if i*5+j==goal:
					return True
	return False


print make_bricks(3, 1, 8)
print make_bricks(3, 1, 9)
print make_bricks(3, 2, 10)
print make_bricks(3, 2, 8)
print make_bricks(3, 2, 9)
print make_bricks(6, 1, 11) 
print make_bricks(6, 0, 11) 
print make_bricks(1, 4, 11)
print make_bricks(0, 3, 10)
print make_bricks(1, 4, 12)
print make_bricks(3, 1, 7)
print make_bricks(1, 1, 7)
print make_bricks(2, 1, 7)
print make_bricks(7, 1, 11)
print make_bricks(7, 1, 8)
print make_bricks(7, 1, 13)
print make_bricks(43, 1, 46)
print make_bricks(40, 1, 46)
print make_bricks(40, 2, 47)
print make_bricks(40, 2, 50)
print make_bricks(40, 2, 52)
print make_bricks(22, 2, 33)
print make_bricks(0, 2, 10)
print make_bricks(1000000, 1000, 1000100)
print make_bricks(2, 1000000, 100003)
print make_bricks(20, 0, 19)
print make_bricks(20, 0, 21)
print make_bricks(20, 4, 51)
print make_bricks(20, 4, 39)