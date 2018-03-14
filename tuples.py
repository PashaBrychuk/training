#tuples.py
# Unpacking values from tuple

person = ("Pasha", "Brychuk", 05050034343, "Renault Laguna", 1999)
name, surname, phone_number, car, car_year = person
print name
for i in person:
	print i