#subprocesses.py
from pexpect import pxssh
import pexpect
from subprocess import *
call(["rm", "-rf", "/home/pavlobrychuk/.ssh/known_hosts"])


host=pxssh.pxssh()
host.login ("172.24.223.58", "root", "toor")

"""child.pexpect("rm -rf ssh-keygen -f /home/pavlobrychuk/.ssh/known_hosts -R 172.24.223.58")host.logfile = open("/home/pavlobrychuk/tmp/logfile222.txt", "w")
host.sendline("ls -l")"""

child = pexpect.spawn("ssh root@172.24.223.58 mkdir \/home/root/certs")
child.expect_exact(pexpect.EOF, timeout=None)"""


if call(["scp", "/home/pavlobrychuk/Downloads/MQTT_Congatec/CREDENTIALS/hcpiotsap.cer",  "root@172.24.223.58:/home/root/certs"])==0:
	print "hcpiotsap.cer has been successfully copied"

if call(["scp", "/home/pavlobrychuk/Downloads/MQTT_Congatec/CREDENTIALS/TID-2182497-320000001.crt",  "root@172.24.223.58:/home/root/certs"])==0:
	print "TID-2182497-320000001.crt has been successfully copied"

if call(["scp", "/home/pavlobrychuk/Downloads/MQTT_Congatec/CREDENTIALS/TID-2182497-320000001.key",  "root@172.24.223.58:/home/root/certs"])==0:
	print "TID-2182497-320000001.key has been successfully copied"

if call (["scp", "/home/pavlobrychuk/dev/temp/tag-observer_with_TLS.conf", "root@172.24.223.58:/etc/hilti"])==0:
	print "tag-observer_with_TLS.conf has been successfully copied"



child = pexpect.spawn("ssh root@172.24.223.58 rm -rf /etc/hilti/tag-observer.conf")
child.expect_exact(pexpect.EOF, timeout=None)
child = pexpect.spawn("ssh root@172.24.223.58 mv /etc/hilti/tag-observer_with_TLS.conf /etc/hilti/tag-observer.conf")
child.expect_exact(pexpect.EOF, timeout=None)




print "!"*50
print "Everything is done, master"
child.expect_exact(pexpect.EOF, timeout=None)"""