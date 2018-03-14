
z = 13195
c = []
"""
def check_prime(a):
  for i in range(1, a+1): 
    if a%i ==0:
      
      c.append(i)
      print c
  if len(c)<=2:
        return True
  return False

#print check_prime(114)

def la(b):
  for i in range(1, z):
    if b%i ==0 and check_prime(i):
      a = i
  return a

print la(z)

"""
"""def la(b):
  for i in range(1, z):
    if b%i ==0:
       if b%i ==0:
      
      c.append(i)
      print c
  if len(c)<=2:
        return True
  return False
   

print la(z)"""



import pymongo
from pymongo import Connection

connection = Connection('mongouat.wdsserve.com', 27017)
print connection
db = connection.etdb_uat
db.authenticate('dev', 'password')
collection = db.events
print collection
z = collection.find_one('01-82fd5bc7-6029-47d6-93b6-49f8fddfe40e')
print z