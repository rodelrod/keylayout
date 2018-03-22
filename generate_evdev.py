#!/usr/bin/env python
from __future__ import print_function
import os
import sys
import shutil
import time
import xml.etree.ElementTree as ET
from os.path import dirname, realpath
import argparse

SCRIPT_DIR = dirname(realpath(__file__))
XKB_RULES_DIR = "/usr/share/X11/xkb"

timestamp = str(int(time.time()))
evdev_file = os.path.join(XKB_RULES_DIR, "rules", "evdev.xml")
local_evdev = os.path.join(SCRIPT_DIR, "evdev.xml")

if os.getuid() != 0:
    print("Please run as root.")
    sys.exit()
if not os.path.exists(evdev_file):
    if os.path.exists(evdev_file + ".bkp"):
        shutil.copy(evdev_file + ".bkp", evdev_file)
    else:
        print("Your system must have a `evdev.xml` file.")
        sys.exit()
if os.path.exists(local_evdev):
    shutil.move(local_evdev, local_evdev + ".%s.bkp" % (timestamp,))

tree = ET.parse(evdev_file)
root = tree.getroot()
layouts = root.find("layoutList")

pt_rod = ET.fromstring("""
<layout>
     <configItem>
       <name>pt_rod</name>
       <shortDescription>ptrod</shortDescription>
       <description>Rod (PT based)</description>
       <languageList>
          <iso639Id>por</iso639Id>
       </languageList>
     </configItem>
     <variantList />
</layout>
""")

us_rod = ET.fromstring("""
<layout>
     <configItem>
       <name>us_rod</name>
       <shortDescription>usrod</shortDescription>
       <description>Rod (US based)</description>
       <languageList>
          <iso639Id>eng</iso639Id>
       </languageList>
     </configItem>
     <variantList />
</layout>
""")

gb_rod = ET.fromstring("""
<layout>
     <configItem>
       <name>gb_rod</name>
       <shortDescription>gbrod</shortDescription>
       <description>Rod (UK based)</description>
       <languageList>
          <iso639Id>eng</iso639Id>
       </languageList>
     </configItem>
     <variantList />
</layout>
""")

new_layouts = {
    'pt_rod': pt_rod,
    'us_rod': us_rod,
    'gb_rod': gb_rod,
}

for nl in new_layouts.keys():
    nl_element = layouts.find("./layout/configItem[name='%s']/.." % (nl,))
    if nl_element is not None:
        layouts.remove(nl_element)
    layouts.append(new_layouts[nl])

tree.write(local_evdev)
