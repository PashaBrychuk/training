#pxssh.py   https://www.youtube.com/watch?v=WELvXrXJeUk&list=PL6yBpeP80w3-1Mv3ZJEB5OP3QVoE-DNws
from pexpect import pxssh
s = pxssh.pxssh()
#print s
z = pxssh.pxssh()

print s.login("172.24.223.58", "root","")
s.logout()
s.pid=None
print s.login("172.24.223.58", "root","")
print help(s.login)