#!/usr/bin/env python3
import configparser
import os


class Battery(object):
    """docstring for Battery"""
    def __init__(self, arg):
        super(Battery, self).__init__()
        self.arg = arg


if __name__ == "__main__":
    # Check that we actually have tp_smapi before doing anything
    if os.path.isdir('/sys/devices/platform/smapi'):
        print("tp_smapi sysfs found")
    else:
        quit("tp_smapi sysfs not found - maybe not installed?")

    config = configparser.ConfigParser()
    config.read("config.ini")
