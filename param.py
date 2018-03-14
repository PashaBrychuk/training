import paramiko
ssh = paramiko.SSHClient()
ssh.known_hosts = None
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("172.24.223.58", port =22, username="root",password =None, pkey=None) 
