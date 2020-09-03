## This is My R-Pi Project
###Set up List
- sudo apt-get update && sudo apt-get upgrade

**Remote Desktop** ([credit](https://www.youtube.com/watch?v=0I5DYtx2WKQ))
- sudo apt-get install xrdp            
- sudo apt-get install tightvncserver

**Static ip** ([credit](https://www.ionos.com/digitalguide/server/configuration/provide-raspberry-pi-with-a-static-ip-address/))
- sudo service dhcpcd status
- sudo service dhcpcd start
- sudo systemctl enable dhcpcd
- sudo nano /etc/dhcpcd.conf
```
interface eth0
static ip_address=192.168.0.4/24
static routers=192.168.0.1
static domain_name_servers=192.168.0.1
```
- sudo reboot

**Root user**
- 

**Wake on Lan** ([credit](https://notenoughtech.com/raspberry-pi/use-raspberry-pi-wol/))
- sudo apt-get install etherwake

**Git**
- sudo apt install git

**Pi-hole**
- curl -sSL https://install.pi-hole.net | bash




