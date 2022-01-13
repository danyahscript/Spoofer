"""
#=========================================================#
# [+] Title: Simple ARP Spoofing                          #
# [+] Script: Spoofer.py                                  #
# [+] Creator : Danyah Alharthi                           #
#=========================================================#
"""

# This tool require root/admin privileges "run in the command-line"
# Syntax : python <filename> <option> <IP of the default gateway>/<Subnet>
import sys
import argparse
from scapy.all import *


class bcolors:
    FAIL = '\033[41m'
    HELP = '\033[42m'
    ENDC = '\033[0m'
    IP = '\033[36m'


parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description=print('\033[94m' + '''
                        
           
       ░██████╗██████╗░░█████╗░░█████╗░███████╗███████╗██████╗░
       ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
       ╚█████╗░██████╔╝██║░░██║██║░░██║█████╗░░█████╗░░██████╔╝
       ░╚═══██╗██╔═══╝░██║░░██║██║░░██║██╔══╝░░██╔══╝░░██╔══██╗
       ██████╔╝██║░░░░░╚█████╔╝╚█████╔╝██║░░░░░███████╗██║░░██║
       ╚═════╝░╚═╝░░░░░░╚════╝░░╚════╝░╚═╝░░░░░╚══════╝╚═╝░░╚═╝
                            
                           Tool :- Spoofer
                    Tool type :- ARP Spoofing
                    Created by :- Danyah Alharthi 
             Syntax :  python3 Spoofer.py -ip <IP>/<Subnet>
       ''' + '\033[0m'), )
parser.add_argument("-ip", "--ipaddress", help="IP Address/Subnet Mask")
args = parser.parse_args()

if not args.ipaddress:
    print(bcolors.FAIL+'Invalid Syntax'+bcolors.ENDC)
    print(bcolors.HELP+'Use --help or -h for options.'+bcolors.ENDC)
    sys.exit(1)

else:
    # pdst : destination IP address
    arp_request = scapy.layers.l2.ARP(pdst= args.ipaddress)
    broadcast_frame = scapy.layers.l2.Ether(dst="ff:ff:ff:ff:ff:ff")
    final_request = broadcast_frame/arp_request
    results_ans = scapy.layers.l2.srp(final_request, timeout=2, verbose=False)[0]
    results = []
    for i in range(0,len(results_ans)):
        # psrc : source IP Address
        # hwsrc : destination MAC Address
        clients = {"ip":results_ans[i][1].psrc," mac":results_ans[i][1].hwsrc}
        results.append(clients)
    for i in range(len(results)):
        print(results[i])
