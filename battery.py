#!/usr/bin/env python3
import os

if __name__ == "__main__":
    if os.path.isdir('/sys/devices/platform/smapi'):
        print("tp_smapi sysfs found")
    else:
        quit("tp_smapi sysfs not found - maybe not installed?")
