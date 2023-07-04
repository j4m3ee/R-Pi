## This is My R-Pi Project

### Set up List
- sudo apt-get update && sudo apt-get upgrade

**Remote Desktop** ([credit](https://www.youtube.com/watch?v=0I5DYtx2WKQ))
- sudo apt-get install xrdp            
- sudo apt-get install tightvncserver

**Remmina**
- sudo apt-get install remmina remmina-plugin-rdp

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
- sudo passwd root

**Wake on Lan** ([credit](https://notenoughtech.com/raspberry-pi/use-raspberry-pi-wol/))
- sudo apt-get install etherwake

**Git**
- sudo apt install git

**Pi-hole**
- curl -sSL https://install.pi-hole.net | bash

**NAS** ([credit](https://www.youtube.com/watch?v=q_c7rvMdM_M))
- lsblk

**Web-Server** ([credit](https://www.raspberrypi.org/documentation/remote-access/web-server/apache.md))
- sudo apt-get install apache2 -y
- sudo apt install php libapache2-mod-php -y

**Set-up without Monitor**
- create file ```ssh.txt``` for open ssh
- create file ```wpa_supplicant.conf``` for connect wireless
 and put this text inside
 
 ```
 ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=<Insert 2 letter ISO 3166-1 country code here>

network={
 ssid="<Name of your wireless LAN>"
 psk="<Password for your wireless LAN>"
}
```
 
 **Install .deb file**
- sudo dpkg -i ```file_name.deb```




