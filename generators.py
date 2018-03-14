"""s = [1,2,3,4,5]
def gena(s):
	for i in s:
		yield i*i

z = gena(s)
print z
for i in z:
	print i"""

generator_that_looks_like_list_comprehansion = (x*x for x in [1,2,3,4,5] if x%2 ==0)
#print generator_that_looks_like_list_comprehansion
#print list(generator_that_looks_like_list_comprehansion)
#	print i
for i in generator_that_looks_like_list_comprehansion:
	print i
#print list(generator_that_looks_like_list_comprehansion)
for i in generator_that_looks_like_list_comprehansion:
	print i
#list_compheransion = [x*x for x in [1,2,3,4,5] if x%2 ==0]
#print list_compheransion
