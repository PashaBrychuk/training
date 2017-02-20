factors = []
res = []
def find_factors(number):
  
  for i in range(1, number):
    if number%i ==0:
      factors.append(i)
  return factors




def check_prime_factors(factors):
  for i in factors:
    print "i", i
    count = 0
    for j in range(1, i+1):
      print "j", j
      if i % j ==0:
        print "smthg"
        count = count+1
        if count >=2:
          print i
          print "Pasha"
          factors.remove(i)
  return factors





  
g = [5,7,9,11,17,19,23,31,33,34,36]
print check_prime_factors(g)


"""if i % j ==0:
        print "smthg"
        count = count+1
        if count >=2:
          print "Pasha"
          factors.remove(i)

"""
"""import pymongo
from pymongo import Connection

connection = Connection('mongouat.wdsserve.com', 27017)
print connection
db = connection.etdb_uat
db.authenticate('dev', 'password')
collection = db.events
print collection
z = collection.find_one('01-82fd5bc7-6029-47d6-93b6-49f8fddfe40e')
print z"""