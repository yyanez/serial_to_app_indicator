#!/usr/bin/python
import os
import serial
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator

def main():
    indicator = appindicator.Indicator.new("customtray", "semi-starred-symbolic", appindicator.IndicatorCategory.APPLICATION_STATUS)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_label("23 ºC", "54% thrust")    
    indicator.set_menu(menu())
    gtk.main()

def menu():
    menu = gtk.Menu()
    exittray = gtk.MenuItem('Exit Tray')
    exittray.connect('activate', quit)
    menu.append(exittray)

    menu.show_all()
    return menu

def quit(_):
    gtk.main_quit()

if __name__ == "__main__":
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    data = ser.readline()
    print(data)    
    main()
