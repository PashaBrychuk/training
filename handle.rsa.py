host = pxssh.pxssh()
host.login (hostname, username, password)
host.logfile = open(/tmp/logfile.txt, "w")
host.sendline("ls -l"