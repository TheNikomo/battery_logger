#!/usr/bin/env python3
import configparser
import glob
import os


class Battery(object):
    """
    Battery object
    Stores path to sysfs device
    and returns properties
    about the device
    """

    def __init__(self, path):
        self.path = path

    def properties(self):
        property_dict = {}
        os.chdir(self.path)
        for property in os.listdir():
            try:
                property_dict[property] = open(
                    os.path.abspath(property)).read().rstrip()
            except OSError:
                property_dict[property] = None
        return property_dict

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
