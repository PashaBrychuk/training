x = 5
print id(x)
x = x+5
print id(x)

z = [1,2,3]
print z
print id(z)
z = z.remove(3)
print z
print id(z)

k = [1,3]
c = [2,4]
k = k+c
print k

print c.append(4)
print c