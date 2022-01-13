# Spoofer

Spoofer is a basic scanner that scans a target network to obtain the link-layer ( local IP and MAC ) addresses of the connected client's by sending a falsified ARP packet.


`Syntax : python <filename> <option> <IP of the default gateway>/<Subnet>`

> NOTE : Running this tool require root/admin privileges "runs in the command-line"


  
This tool require both libraries :

1. argparse
  
  ```
  $ pip install argparse
  ```
2. scapy 
  ```
  $ pip install scapy
  ```
  
