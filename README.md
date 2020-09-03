## This is My R-Pi Project
**Set up List**
-sudo apt-get update && sudo apt-get upgrade

**Remote Desktop** ([credit](shorturl.at/sNW06))
-sudo apt-get install xrdp            
-sudo apt-get install tightvncserver

**Static ip** ([credit](shorturl.at/fuBPU))
-sudo service dhcpcd status
-sudo service dhcpcd start
-sudo systemctl enable dhcpcd
-sudo nano /etc/dhcpcd.conf
-interface eth0
static ip_address=192.168.0.4/24
static routers=192.168.0.1
static domain_name_servers=192.168.0.1
-sudo reboot'




