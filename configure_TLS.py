"""# /usr/bin/env python
import subprocess

term1 = subprocess.Popen(["open",  "Terminal"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
term1.communicate(input="pwd")"""

"""
import subprocess
process1 = subprocess.Popen(["sudo scp /home/pavlobrychuk/dev/temp/tag-observer_with_TLS.conf root@172.24.223.58:/etc/hilti"])
process2 = subprocess.Popen(["ls", "-l"])"""

"""import subprocess

proc = subprocess.Popen(['/bin/bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#z=proc.communicate("ssh-keygen -f \"/home/pavlobrychuk/.ssh/known_hosts\" -R 172.24.223.58")
#proc.stdin.write('solYma8067\n')

stdout = proc.communicate("sudo scp /home/pavlobrychuk/dev/temp/tag-observer_with_TLS.conf root@172.24.223.58:/etc/hilti")
proc.stdin.write('solYma8067\n')

print stdout"""

import pexpect

pexpect.spawn('rm -rf /home/pavlobrychuk/.ssh/known_hosts')




child=pexpect.spawn('sudo scp /home/pavlobrychuk/Downloads/MQTT_Congatec/CREDENTIALS/hcpiotsap.cer  root@172.24.223.58:/home/root/certs')
child.expect("\[sudo\] password for pavlobrychuk:") 
child.sendline('solYma8067')

child=pexpect.spawn('sudo scp /home/pavlobrychuk/Downloads/MQTT_Congatec/CREDENTIALS/TID-2182497-320000001.crt  root@172.24.223.58:/home/root/certs')
child.expect("\[sudo\] password for pavlobrychuk:") 
child.sendline('solYma8067')


child=pexpect.spawn('sudo scp /home/pavlobrychuk/dev/temp/tag-observer_with_tls.conf root@172.24.223.58:/etc/hilti')
child.expect("\[sudo\] password for pavlobrychuk:") 
child.sendline('solYma8067')
#child.logfile = sys.stdout

child = pexpect.spawn('sudo scp /home/pavlobrychuk/Downloads/MQTT_Congatec/CREDENTIALS/TID-2182497-320000001.key  root@172.24.223.58:/home/root/certs')
child.expect("\[sudo\] password for pavlobrychuk:") 
child.sendline('solYma8067')
"""
child.expect("\[sudo\] password for pavlobrychuk:") 


child.sendline('solYma8067')
"""
print "Done, master"
child.expect_exact(pexpect.EOF, timeout=None)
