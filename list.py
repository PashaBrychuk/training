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