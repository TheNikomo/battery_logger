#!/usr/bin/env python3
import configparser
import glob
import os


class Battery(object):
    """
    Battery object, stores path to sysfs
    device and properties about the device
    NYI: The properties
    """
    def __init__(self, path):
        self.path = path

if __name__ == "__main__":
    # Check that we actually have tp_smapi before doing anything
    if os.path.isdir('/sys/devices/platform/smapi'):
        print('tp_smapi sysfs found')
        os.chdir('/sys/devices/platform/smapi')
    else:
        quit('tp_smapi sysfs not found - maybe not installed?')

    # Read the config
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Get the batteries we have in the system
    batteries = []
    for battery_device in glob.glob('BAT*'):
        batteries.append(Battery(os.path.abspath(battery_device)))
