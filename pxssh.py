#pxssh.py   https://www.youtube.com/watch?v=WELvXrXJeUk&list=PL6yBpeP80w3-1Mv3ZJEB5OP3QVoE-DNws
from pexpect import pxssh
s = pxssh.pxssh()
#print s
z = pxssh.pxssh()

#print s.login("172.24.223.58", "root","")
#s.logout()
s.pid=None
print s.login("172.24.223.58", "root","", original_prompt="root@congatec-qa3-64:~#")
print s.isalive()
#print help(s.login)

#print help(s)

"""print s.send("systemctl stop hilti-tag-observer\n")
print s.prompt()
print s.send("systemctl start hilti-tag-observer\n")
print s.prompt()"""

s.interact()

print "!"