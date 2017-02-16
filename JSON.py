class pet():
	def __init__(self, name, age, size):
		self.name = name
		self.age = age
		self.size = size
	def __repr__(self):
		return "{}, {}, {} ".format(self.age, self.size, self.name)

def sortir(animal):
	return animal.size

cat = pet("Tom", 12, "middle")
dog = pet("Guffi",13, "big")

listo = [cat, dog]
z  = sorted(listo, key = sortir)
print z
