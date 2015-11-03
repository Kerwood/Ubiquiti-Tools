#!/bin/bash

# Formatting variables
BOLD=$(tput bold)
NORMAL=$(tput sgr0)
GREEN=$(tput setaf 2)
LBLUE=$(tput setaf 6)
RED=$(tput setaf 1)
PURPLE=$(tput setaf 5)

clear
echo "${BOLD}${LBLUE}Welcome to my Ubiquití scripts!${NORMAL}"
echo
echo "${BOLD}${LBLUE}DiscoverUbiquiti.py${NORMAL}"
echo "The DiscoverUbiquiti script, I wrote to discover Ubiquiti products on Layer 2."
echo "It ping sweeps the LAN and checks the arp table for matching MAC addresses."
echo "It then trys to make a SSH connection to the devices and pull hostname, model name," 
echo "controller inform address and etc.."
echo
echo "${GREEN}Usage:${NORMAL}"
echo "The --network parameter is optional. But you need to ping sweep at least once to fill your arp table."
echo "SSH username and password are also optional, you can set the two varables in the script instead"
echo
echo "    ${BOLD}./DiscoverUbiquiti.py -n 10.0.0.0/24 -u sshUsername -p sshPass${NORMAL}"
echo 
echo "       -n, Specifies the network to ping sweep. Optional"
echo "       -u, Specifies the SSH username. Optional"
echo "       -p, Specifies the SSH password. Optional"
echo 
echo "${BOLD}${LBLUE}setInform.py${NORMAL}"
echo "This script can set the inform address on multiple Ubiquiti devices automatically."
echo
echo "${GREEN}Usage:${NORMAL}"
echo "Set the variables sshUser and sshPass with our SSH cridentials, fill the informAddr array with"
echo "IPs from the devices you want to configure and run the script."
echo
echo "    ${BOLD}./setInform.py${NORMAL}"
echo
echo
echo "${LBLUE}Find more information at https://github.com/Kerwood/Ubiquiti-Tools"
echo "Patrick Kerwood @ https://linuxbloggen.dk/${NORMAL}"
echo
