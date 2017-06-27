"""factors = []
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


"""
"""if i % j ==0:
        print "smthg"
        count = count+1
        if count >=2:
          print "Pasha"
          factors.remove(i)

import pymongo
from pymongo import Connection

connection = Connection('mongouat.wdsserve.com', 27017)
print connection
db = connection.etdb_uat
db.authenticate('dev', 'password')
collection = db.events
print collection
z = collection.find_one('01-82fd5bc7-6029-47d6-93b6-49f8fddfe40e')
print z"""
""""""


def check_prime_factors(factors):
  for i in factors:
    #print "i =", i
    count = 0
    for j in range(1, i):
      #print "j", j

      if i % j ==0:
        print "i=", i
        count = count+1
        print "count =", count
        if count >=2:


          #rint "Pasha"
          if i in factors:
            #print "i = ", i
            #print "factors.remove", i
            factors.remove(i)
            
            break
            print factors
  return factors

factors = [1,2,3,4,5,6,7,8,9,9,11,13,17,19,24,25,26,27,23,28,100,144,49,49]


print check_prime_factors(factors)