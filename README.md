Ubiquiti Discovery Script
=========================

This is a Python script i wrote to discover Ubiquiti products. Since I've only been able to get my hands on a few devices, the device support list i rather short, see list below. 

What the script does, is fairly simple. It ping sweeps the LAN and checks the arp table for matching MAC addresses. It then trys to make a SSH connection to get the device model name, firmware version and controller inform address if any.

To make the SSH connection, you must specify the login credentials in the script. For AP's, it is the specifyed site login. You will find it in "Settings -> Site" at the bottom, "Device Password". Put your curser in the password field to reveal it. And for other non-controlled devices, like the NanBeam, it is login to the actual device.

My experience is that the ping sweep works better, if the computer you are using, is cabled to the network, instead of using WiFi.

### Requirements
 - Linux OS
 - Python 2.7.*
 - Paramiko (Python module - Easy install with pip)
 - Nmap

### Supported devices
Basicly the script should work with any device with a MAC starting with `24:a4:3c` or `04:18:d6`.
The devices I have tested is the following.
 - UAP
 - UAP-LR
 - UAP-Pro
 - UAP-Outdoor+
 - mPort
 - NanoBeamM5

### Example

There are two ways you can run the script, with or without the ping sweep. Use the `-n` parameter to specify the network. It has to be the network ID. By default the script will ping a 24 bit subnet. If you need to change this, you will have to change it manually in the script.

Below is an exampel of the script in use.



```
kerwood@Kerwood:~$ python DiscoverUbiquiti.py -n 10.0.0.0

Ping sweep in progress...
Nmap done: 256 IP addresses (85 hosts up) scanned in 2.71 seconds

Ubiquiti Unifi APs

IP               MAC                Model            Version      Status                                       
10.0.0.179       24:a4:3c:b0:2b:18  UAP-Pro          3.2.1.2601   Connected (http://10.0.0.130:8080/inform)    
10.0.0.215       24:a4:3c:94:4c:7d  UAP-Outdoor+     3.2.1.2601   Connected (http://10.0.0.130:8080/inform)    


Other Ubiquiti Accessories

IP               MAC                Model            Version      Inform URL                                   
10.0.0.15        04:18:d6:61:38:b9  NanoBeamM5       XW.v5.5.10                                                
10.0.0.16        04:18:d6:4a:ca:ad  NanoBeamM5       XW.v5.5.10                                                
10.0.0.213       04:18:d6:26:02:e1  mPort            2.1.1.1290   http://10.0.0.220:6080/inform
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
