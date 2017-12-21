Installation
============

This installation only works on Ubuntu 16.06 LTS and distributions
that have their xkb layout files in the same location.

First you generate an `evdev.xml` file locally. This file is based on the
current `evdev.xml` file in your system with the added support for the 
`pt_rod` and `us_rod` layouts.

```sh
sudo ./generate_evdev.py
```

Then you run `install.sh` to create the soft links from the appropriate 
XKB config location to the files in this script's directory.

```sh
Run `sudo ./install.sh`
```

All the replaced files are backed up at `<original_dir>/<original_filename>.bkp`.
