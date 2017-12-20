Installation
============

Run `sudo install.sh`

The current installer replaces the xkb keyboard layout registration file
(`evdev.xml`) with its own, based on Ubuntu 16.06 LTS. You are better off not
using this installer in your own setup  unless you have a pristine Ubuntu 16.06
environment.

A better version of the installer would inject the new keyboard definitions
into the existing evdev.xml file.

All the replaced files are backed up at `<original_dir>/<original_filename>.bkp`.
