factors = []
res = []
def find_factors(number):
  
  for i in range(1, number):
    if number%i ==0:
      factors.append(i)
  return factors

def check_prime_factors(factors):
 
  temp = []
  for i in factors:
    count = 0
    for z in range(1,i):
      
      if i%z ==0:
        print "i= ", i
        print "z= ", z
        count = count+1
        print count
        print "--------"
        if count <=1:
          temp.append(i)

  return temp
g = [1,5,7,9]
print check_prime_factors(g)



print 5%1




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