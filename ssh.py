import os
#os.system("sudo -n scp 172.24.223.58:/home/root/check_output.txt /home/pavlobrychuk/training/")



sudoPassword = 'solYma8067'
command = 'sudo -n scp 172.24.223.58:/home/root/check_output.txt /home/pavlobrychuk/training/'
p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))