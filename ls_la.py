#ls_la.py


from subprocess import *


call(["ls", "-la", "/home/pavlobrychuk/dev/empty"])


print call("exit 0", shell = True)


print call("exit 2", shell = True)


print call("exit 4", shell = True)