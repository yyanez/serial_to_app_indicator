#!/bin/bash

# Check if we are in SUDO mode

if [ ! -z "$SUDO_USER" ]; then
    apt-get install -y gir1.2-appindicator3
    apt-get install -y python3-pip
    pip install pyserial==3.3
    usermod -a -G dialout $(logname)
    mkdir /opt/serial_to_app_indicator/
    cp serial_to_app_indicator.py /opt/serial_to_app_indicator/serial_to_app_indicator.py
    chmod 777 /opt/serial_to_app_indicator/serial_to_app_indicator.py
    cp image.png /opt/serial_to_app_indicator/image.png
    echo "================================================================"
    echo "================================================================"
    echo "You must restart the session to get USB - serial port privileges"
    echo "================================================================"
    echo "================================================================"    
else
	echo "The script must be executed with root privileges"
fi
