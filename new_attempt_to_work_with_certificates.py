#new_attempt_to_work_with_certificates.py

from pexpect import pxssh
import pexpect
from subprocess import *
#print  call(["rm", "-rf", "/home/pavlobrychuk/dev/temp/dmesg.txt"])
#call(["scp", "/home/pavlobrychuk/Downloads/MQTT_Congatec/CREDENTIALS/hcpiotsap.cer", "root@172.24.223.58:/home/root/certs"])

m = check_output(["ls pasha; exit 0"], stderr=STDOUT, shell=True)
print m