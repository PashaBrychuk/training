from pexpect import pxssh
import pexpect
host = pxssh.pxssh()

host.login ("172.24.223.58", "root")
#child.pexpect("rm -rf ssh-keygen -f /home/pavlobrychuk/.ssh/known_hosts -R 172.24.223.58")
host.logfile = open("/home/pavlobrychuk/tmp/logfile222.txt", "w")
host.sendline("ls -l")
print host.prompt()
child = pexpect.spawn("ssh root@172.24.223.58 mkdir \/home/root/certs")
child.expect_exact(pexpect.EOF, timeout=None)

child=pexpect.spawn('sudo scp /home/pavlobrychuk/Downloads/MQTT_Congatec/CREDENTIALS/hcpiotsap.cer  root@172.24.223.58:/home/root/certs')
child.expect("\[sudo\] password for pavlobrychuk:") 
child.sendline('solYma8067')
child.expect_exact(pexpect.EOF, timeout=None)

print "0"

child=pexpect.spawn('sudo scp /home/pavlobrychuk/Downloads/MQTT_Congatec/CREDENTIALS/TID-2182497-320000001.key root@172.24.223.58:/home/root/certs')
child.expect("\[sudo\] password for pavlobrychuk:") 
child.sendline('solYma8067')
child.expect_exact(pexpect.EOF, timeout=None)

print "1"

child1=pexpect.spawn('sudo scp /home/pavlobrychuk/dev/temp/tag-observer_with_TLS.conf  root@172.24.223.58:/etc/hilti')
child1.expect("\[sudo\] password for pavlobrychuk:") 
child1.sendline('solYma8067')
#child.logfile = sys.stdout
child.expect_exact(pexpect.EOF, timeout=None)

print "2"

child2 = pexpect.spawn('sudo scp /home/pavlobrychuk/Downloads/MQTT_Congatec/CREDENTIALS/TID-2182497-320000001.crt root@172.24.223.58:/home/root/certs')
child2.expect("\[sudo\] password for pavlobrychuk:") 
child2.sendline('solYma8067')
child2.expect_exact(pexpect.EOF, timeout=None)

print "3"