#new_attempt_to_work_with_certificates.py

from pexpect import pxssh
import pexpect
from subprocess import *
print  call(["rm", "-rf", "/home/pavlobrychuk/dev/temp/dmesg.txt"])
call(["scp", "/home/pavlobrychuk/Downloads/MQTT_Congatec/CREDENTIALS/hcpiotsap.cer", "root@172.24.223.58:/home/root/certs"])

"""
child.expect("\[sudo\] password for pavlobrychuk:") 
child.sendline('solYma8067')
child.expect_exact(pexpect.EOF, timeout=None)"""