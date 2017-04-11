import unittest

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


if make_bricks(3, 1, 8)==  True:
	print "OK"
else:
	print "Fail"
if make_bricks(3, 1, 9)==  False:
	print "OK"
else:
	print "Fail"
if make_bricks(3, 2, 10)== True:
    print "OK"
else:
	print "Fail"
if make_bricks(3, 2, 8)== True:
	print "OK"
else:
	print "Fail"
if make_bricks(3, 2, 9) == False:
	print "OK"
else:
	print "Fail"
if make_bricks(6, 1, 11) == True:
	print "OK"
else:
	print "Fail"
if make_bricks(6, 0, 11)  == False:
	print "OK"
else:
	print "Fail"
if make_bricks(1, 4, 11) == True:
	print "OK"
else:
	print "Fail"
if make_bricks(0, 3, 10) == True:
	print "OK"
else:
	print "Fail"
if make_bricks(1, 4, 12) == False:
	print "OK"
else:
	print "Fail"
if make_bricks(3, 1, 7) == True:
	print "OK"
else:
	print "Fail"
if make_bricks(1, 1, 7) == False:
	print "OK"
else:
	print "Fail"	
if  make_bricks(2, 1, 7) == True:
	print "OK"
else:
	print "Fail"
if make_bricks(7, 1, 11) == True:
	print "OK"
else:
	print "Fail"
if  make_bricks(7, 1, 8) == True:
	print "OK"
else:
	print "Fail"
if make_bricks(7, 1, 13) == False:
	print "OK"
else:
	print "Fail"
if make_bricks(43, 1, 46) == True:
	print "OK"
else:
	print "Fail"
if make_bricks(40, 1, 46) == False:
	print "OK"
else:
	print "Fail"
if make_bricks(40, 2, 47) == True:
	print "OK"
else:
	print "Fail"
if make_bricks(40, 2, 50) == True:
	print "OK"
else:
	print "Fail"
if make_bricks(40, 2, 52) == False:
	print "OK"
else:
	print "Fail"
if make_bricks(22, 2, 33) == False:
	print "OK"
else:
	print "Fail"
if make_bricks(0, 2, 10) == True:
	print "OK"
else:
	print "Fail"
if make_bricks(1000000, 1000, 1000100) == True:
	print "OK"
else:
	print "Fail"
if make_bricks(2, 1000000, 100003) == False:
	print "OK"
else:
	print "Fail"
if make_bricks(20, 0, 19) == True:
	print "OK"
else:
	print "Fail"
if make_bricks(20, 0, 21) == False:
	print "OK"
else:
	print "Fail"
if make_bricks(20, 4, 51) ==  False:
	print "OK"
else:
	print "Fail"	
if make_bricks(20, 4, 39) == True:
	print "OK"
else:
	print "Fail"






print "Final"
print make_bricks(20, 0, 19)