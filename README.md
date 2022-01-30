# serial_to_app_indicator

Reads the incoming data from the /dev/ttyACM0/ USB serial port and prints it in the System Tray

## Requisites

The user must be in the dialout group. The system must be restarted after
```
sudo usermod -a -G dialout $USER
```

Install the following packages:
```
sudo apt-get install gir1.2-appindicator3
sudo apt-get install python3-pip
pip install pyserial==3.3
```
pyserial must be installed in the 3.3 version because it does not work in version 3.5.
To start it:

```
python3 serial_to_app_indicator.py
```

To start it automatically use (If using the install script, the path is "/opt/serial_to_app_indicator"): 
```
nohup python3 <path_to_the_app>/serial_to_app_indicator.py &
```

## References
* __AppIndicator API documentation:__ https://gjs-docs.gnome.org/appindicator301~0.1_api/
* __TopIcons Plus extension:__ https://extensions.gnome.org/extension/1031/topicons/
* __Tutorial on how to make a tray indicator app in Linux:__ https://fosspost.org/custom-system-tray-icon-indicator-linux/
* __How to use threads in python:__ https://stackoverflow.com/questions/39127158/small-example-for-pyserial-using-threading
"# serial_to_app_indicator" 
