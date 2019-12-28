setInform.py
=========================
This is a Python script to set the inform address on multiple Ubiquiti devices automatically.

Set the variables, `sshUser` and `sshPass` with your SSH cridentials and fill the `informAddr` array with the IPs of devices you wish to configure. The SSH cridentials is your Unifi Controller login and Site password, which is found at "Settings -> Site" near the bottom, "Device Password". Put your curser in the password field to reveal it. Add your AP's IP addresses to the `clients` list and execute the script.

### Requirements
 - Linux OS (Haven't tested it on Windows, but I don't see why it wouldn't work)
 - Python 2.7.*
 - Paramiko (Python module - Easy install with pip)

### Installation
```
sudo apt-get install python python-dev python-pip
```
```
sudo pip install paramiko pycrypto ecdsa
```

### Example

```
kerwood@Kerwood:~$ python setInform.py 

Connecting to devices....

 [+] Adoption request sent to http://10.0.0.130:8080/inform from 10.0.0.10 
 [+] Adoption request sent to http://10.0.0.130:8080/inform from 10.0.0.11 
 [+] Adoption request sent to http://10.0.0.130:8080/inform from 10.0.0.12
 ```

DiscoverUbiquiti.py
=========================

This is a Python script I wrote to discover Ubiquiti products. Since I've only been able to get my hands on a few devices, the device support list i rather short, see list below. 

What the script does, is fairly simple. It ping sweeps the LAN and checks the arp table for matching MAC addresses. It then try's to make a SSH connection to get the device model name, firmware version and controller inform address etc. etc.

To make the SSH connection, you must specify the login credentials, either in the script or by arguments. For AP's, it is the specifyed site login. You will find it in "Settings -> Site" at the bottom, "Device Password". Put your curser in the password field to reveal it. And for other non-controlled devices, like the NanoBeam, it's the login to the actual device.

My experience is that the ping sweep works better, if the computer you are using, is cabled to the network, instead of using WiFi.

### Requirements
 - Linux OS
 - Python 2.7.*
 - Paramiko (Python module - Easy install with pip)
 - Nmap

### Installation
```
sudo apt-get install python python-dev python-pip nmap
```
```
sudo pip install paramiko pycrypto ecdsa
```

### Supported devices
Basicly the script should work with any device with a MAC starting with `24:a4:3c`, `04:18:d6` or `dc:9f:db`.
The devices I have tested is the following.
 - UAP
 - UAP-LR
 - UAP-AC-LR
 - UAP-Pro
 - UAP‑AC‑PRO
 - UAP-Outdoor+
 - mPort
 - NanoBeamM5
 - US-48-500W
 - US-8-60W
 - US-16-150W
 - US-24-250W
 - USG
 - USG‑PRO‑4

### Example

There are 3 parameters that can be set. `-n` for the network/subnet to ping sweep, `-u` for the SSH user and `-p` for at SSH password. All are optional but you should at least run `-n` once to fill up the arp table. If you dont want to specify the SSH credentials as paramters you can set dem manually in the script as variables.  

Below is an exampel of the script in use.



```
kerwood@Kerwood:~$ python DiscoverUbiquiti.py -n 10.0.0.0/24 -u admin -p passw0rd

Ping sweep in progress...
Nmap done: 256 IP addresses (85 hosts up) scanned in 2.71 seconds

Ubiquiti Unifi Devices

IP               MAC                Model            Hostname           Version      Status     
10.0.0.179       24:a4:3c:b0:2b:18  UAP-Pro          Office             3.2.1.2601   Connected (http://10.0.0.130:8080/inform)    
10.0.0.215       24:a4:3c:94:4c:7d  UAP-Outdoor+     Yard               3.2.1.2601   Connected (http://10.0.0.130:8080/inform)
10.0.0.214       04:14:d6:4e:c8:c2  UAP              Back-Office        3.2.1.2601   Connected (http://10.0.0.130:8080/inform) 
10.0.0.15        04:18:d6:61:38:b9  NanoBeamM5       NB1                XW.v5.5.10                                                
10.0.0.16        04:18:d6:4a:ca:ad  NanoBeamM5       NB2                XW.v5.5.10                                                
10.0.0.213       04:18:d6:26:02:e1  mPort            mPortGarage        2.1.1.1290   http://10.0.0.220:6080/inform
```

### Licens
```
--------------------------------------------------------------------------------
  "THE BEER-WARE LICENSE" (Revision 42):
  <patrick@kerwood.dk> wrote this script. As long as you retain this notice you
  can do whatever you want with this stuff. If we meet some day, and you think
  this stuff is worth it, you can buy me a beer in return. 
  
     - Patrick Kerwood @ LinuxBloggen.dk
--------------------------------------------------------------------------------
```
