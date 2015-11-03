#!/usr/bin/python

# -------------------------------------------------------------------------------
#  "THE BEER-WARE LICENSE" (Revision 42):
#  <patrick@kerwood.dk> wrote this script. As long as you retain this notice you
#  can do whatever you want with this stuff. If we meet some day, and you think
#  this stuff is worth it, you can buy me a beer in return. 
#
#     - Patrick Kerwood @ LinuxBloggen.dk
# -------------------------------------------------------------------------------

import paramiko

informAddr = "http://controller-ip:8080/inform"
sshUser = "admin"
sshPass = "passw0rd"

clients = [
    '10.0.0.10',
    '10.0.0.11',
    '10.0.0.12',
]

class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


print "\nConnecting to devices....\n"

for ip in clients:
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=sshUser, password=sshPass, allow_agent=False)
        stdin, stdout, stderr = client.exec_command("mca-cli <<EOF\nset-inform %s\nquit\nEOF" % informAddr)
        
        if stdout.channel.recv_exit_status() == 0:
            for line in stdout:
                if "Adoption request sent to" in line:
                    print " %s[+] Adoption request sent to %s from %s %s" % (bcolors.OKGREEN, informAddr, ip, bcolors.ENDC)
        
        
    except paramiko.AuthenticationException:
        print " %s[-] Authentication failed on %s!%s" % (bcolors.FAIL, ip, bcolors.ENDC)
    except:
        print " %s[-]Something went wrong on %s!%s" % (bcolors.FAIL, ip, bcolors.ENDC)
   
print