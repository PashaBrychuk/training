
import pexpect
child = pexpect.spawn("sudo scp /home/pavlobrychuk/dev/temp/tag-observer_with_TLS.conf root@172.24.223.58:/etc/hilti")


child.expect("\[sudo\] password for pavlobrychuk:") 
child.sendline('solYma8067')
child.expect_exact(pexpect.EOF, timeout=None)

print "Done, master"


