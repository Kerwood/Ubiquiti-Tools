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
import subprocess
import argparse
import re

sshname = "admin"
sshpass = "CM6Frkk2MWvc21He"

def ping_sweep(network):
    print
    print "Ping sweep in progress..."
    nmap = subprocess.check_output("nmap -n -sP %s" % network, shell=True)
    
    nsplit = []
    nsplit = nmap.split("\n")
    for line in nsplit:
        if "done" in line:
            print(line)

def print_ubnt():   
    
    print
    print "Ubiquiti Unifi Devices\n"
    
    arp = subprocess.check_output("arp -a", shell=True)
    
    splitted = []
    splitted = arp.split("\n")
    
    FORMAT = '%-16s %-18s %-16s %-18s %-12s %-45s'
    print(FORMAT % ('IP', 'MAC', 'Model', 'Hostname', 'Version', 'Status'))
    
    for line in splitted:  
        if "24:a4:3c" in line or "04:18:d6" in line:           
            ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line, re.I).group()
            mac = re.search(r'([0-9A-F]{2}[:-]){5}([0-9A-F]{2})', line, re.I).group()
            model = ""
            version = ""
            hostname = ""
            status = ""
            
            try:
                client = paramiko.SSHClient()
                client.load_system_host_keys()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(ip, username=sshname, password=sshpass, allow_agent=False)
                stdin, stdout, stderr = client.exec_command('mca-cli <<EOF\ninfo\nquit\nEOF')
                
                if stdout.channel.recv_exit_status() == 0:
                    for line in stdout:   
                        if "Model" in line:
                            model = line.rsplit(None, 1)[-1]
                        elif "Version" in line:
                            version = line.rsplit(None, 1)[-1]
                        elif "Hostname" in line:
                            hostname = line.rsplit(None, 1)[-1]
                        elif "Status" in line or "Inform" in line:                        
                            status = line.rsplit(None, 2)[-2] + " " + line.rsplit(None, 1)[-1]
                        
                        if hostname == "":
                            stdin, stdout, stderr = client.exec_command('uname -a')
                            for line in stdout:
                                hostname = line.split(None, 2)[1]
                            
                        
                else:
                    stdin, stdout, stderr = client.exec_command('uname -a')
                    for line in stdout:
                        hostname = line.split(None, 2)[1]
                    
                    stdin, stdout, stderr = client.exec_command('cat /etc/version')                   
                    for line in stdout:
                        version = line.strip('\n')
                        
                    stdin, stdout, stderr = client.exec_command('cat /etc/board.info')                   
                    for line in stdout:
                        if "board.name" in line:
                            model = line.rsplit('=', 1)[-1].strip('\n')
                            
                
                    
                client.close()
            except paramiko.AuthenticationException:
                status = "Authentication failed!"
            except:
                status = "Error trying to connect!"
                                
            print(str(FORMAT % (ip, mac, model, hostname, version, status)))
        

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--network", help="Make a ping sweep on subnet Eg. -n 10.0.0.0/24")
args = parser.parse_args()

if args.network:
    ping_sweep(args.network)

print_ubnt()
print
