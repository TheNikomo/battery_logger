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
        self.path = path + "/"
        self.name = os.path.basename(path)

    def properties(self):
        property_dict = {}
        for property in os.listdir(self.path):
            try:
                property_dict[property] = open(
                    self.path + property).read().rstrip()
            except OSError:
                property_dict[property] = None
        return property_dict

if __name__ == "__main__":
    # Check that we actually have tp_smapi before doing anything
    if os.path.isdir('/sys/devices/platform/smapi'):
        print('tp_smapi sysfs found')
    else:
        quit('tp_smapi sysfs not found - maybe not installed?')

    # Read the config
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Get the batteries we have in the system
    batteries = []
    for battery_device in glob.glob('/sys/devices/platform/smapi/BAT*'):
        batteries.append(Battery(os.path.abspath(battery_device)))

    # Remove untracked batteries from the list
    for battery in batteries:
        if battery.name not in config["general"]["tracked"]:
            batteries.remove(battery)
