import paramiko
ssh = paramiko.SSHClient()
ssh.known_hosts = None
ssh.connect("172.24.223.58", port =22, username="root",password ="root")