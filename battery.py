#!/usr/bin/python
import os

os.chdir("/sys/devices/platform/smapi/BAT0/")
objects = sorted(os.listdir())
for object in objects:
    with open(object) as f:
        try:
            content = f.read()
        except OSError:
            content = "Not supported\n"

    print("{}: {}".format(object, content), end='')
