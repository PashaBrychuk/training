helloWorld= ["a",1,"b",2]
lis = ["a",1,"b",2]
# Convert to a dictionary
helloWorldDictionary = dict(zip(helloWorld[0::2], helloWorld[1::2]))

# Print out the result

x = lis[::2]
print x

y = lis[1::2]
print y
print(helloWorldDictionary)

print list(zip(x,y))


s = [3,1,2]

print sorted(s)

b = [1,3,5]
g = b
print id(b)
print id(g)

b.append(7)

print b
print g


old=[1,2,3]
new = old[:]
print old
print new
print old is new


lista=[0,1,2,3,4,5,6]

g=list(filter(lambda x: x%2==0, lista))

print g


m= [x for x in lista if x%2==0]

print m


