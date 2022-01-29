import os
import sys
import time
import threading
import serial
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator
thread_flag = None


def Report(s):
    print(s)
    sys.stdout.flush() # helps to ensure messages from different threads appear in the right order

def Stop():
    global thread_flag
    thread_flag = 'stop'

def Task1(ser, indicator):

    Report("Inside Thread 1")
    global thread_flag
    thread_flag = 'go'

    while True:

        Report("Thread 1 waiting for permission to read")
        while thread_flag != 'go': time.sleep( 0.001 )

        while thread_flag == 'go':
            data = ser.readline().decode('utf-8')
            indicator.set_label(data, "hola")
            Report(data)
            time.sleep(1)

        if thread_flag == 'stop': break
        else: thread_flag = 'paused'   # signals that the inner loop is done

    Report("Thread 1 complete")

def menu():
    menu = gtk.Menu()
    exittray = gtk.MenuItem(label='Exit Tray')
    exittray.connect('activate', quit)
    menu.append(exittray)

    menu.show_all()
    return menu

def quit(_):
    gtk.main_quit()
    
def Main():
    ser = serial.Serial("/dev/ttyACM0", 9600)
    currpath = os.path.dirname(os.path.realpath(__file__))
    iconpath = currpath+"/image.png"
    # indicator = appindicator.Indicator.new("customtray", "semi-starred-symbolic", appindicator.IndicatorCategory.APPLICATION_STATUS)
    indicator = appindicator.Indicator.new("customtray", iconpath, appindicator.IndicatorCategory.APPLICATION_STATUS)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_label("Start", "hola")    
    indicator.set_menu(menu())
    
    t1 = threading.Thread(target = Task1, args=[ser, indicator])
    Report("Starting Thread 1")
    t1.start()

    gtk.main()


if __name__ == '__main__':

    Main()