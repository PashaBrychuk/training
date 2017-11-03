#subprocesses.py
from pexpect import pxssh
import pexpect
from subprocess import *
print  call(["rm", "-rf", "/home/pavlobrychuk/.ssh/known_hosts"])


host=pxssh.pxssh()
host.login ("172.24.223.58", "root")
#child.pexpect("rm -rf ssh-keygen -f /home/pavlobrychuk/.ssh/known_hosts -R 172.24.223.58")
host.logfile = open("/home/pavlobrychuk/tmp/logfile222.txt", "w")
host.sendline("ls -l")
print host.prompt()
child = pexpect.spawn("ssh root@172.24.223.58 mkdir \/home/root/certs1")
child.expect_exact(pexpect.EOF, timeout=None)


child=pexpect.spawn('sudo scp /home/pavlobrychuk/Downloads/MQTT_Congatec/CREDENTIALS/hcpiotsap.cer  root@172.24.223.58:/home/root/certs1')
child.expect("\[sudo\] password for pavlobrychuk:") 
child.sendline('solYma8067')
child.expect_exact(pexpect.EOF, timeout=None)

child=pexpect.spawn('sudo scp /home/pavlobrychuk/Downloads/MQTT_Congatec/CREDENTIALS/TID-2182497-320000001.crt  root@172.24.223.58:/home/root/certs1')
child.expect("\[sudo\] password for pavlobrychuk:") 
child.sendline('solYma8067')
child.expect_exact(pexpect.EOF, timeout=None)

child=pexpect.spawn('sudo scp /home/pavlobrychuk/dev/temp/tag-observer_with_TLS.conf root@172.24.223.58:/etc/hilti')
child.expect("\[sudo\] password for pavlobrychuk:") 
child.sendline('solYma8067')
child.expect_exact(pexpect.EOF, timeout=None)


child = pexpect.spawn('sudo scp /home/pavlobrychuk/Downloads/MQTT_Congatec/CREDENTIALS/TID-2182497-320000001.key  root@172.24.223.58:/home/root/certs1')
child.expect("\[sudo\] password for pavlobrychuk:") 

child.sendline('solYma8067')
"""
child.expect("\[sudo\] password for pavlobrychuk:") 


child.sendline('solYma8067')
"""
print "Done, master"
child.expect_exact(pexpect.EOF, timeout=None)