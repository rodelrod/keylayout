#!/bin/bash
TIMESTAMP=`date +%Y%m%d%H%M%S`
SCRIPTDIR=`dirname $0 | xargs realpath`
XKBDIR=/usr/share/X11/xkb

if [[ $USER != "root" ]]; then 
    echo "Please run as root.";
    exit; 
fi

if [[ -e $XKBDIR/rules/evdev.xml ]]; then
    mv $XKBDIR/rules/evdev.xml $XKBDIR/rules/evdev.xml.$TIMESTAMP.bkp;
fi
ln -s $SCRIPTDIR/evdev.xml $XKBDIR/rules/evdev.xml

if [[ -e $XKBDIR/symbols/pt_rod ]]; then
    mv $XKBDIR/symbols/pt_rod $XKBDIR/symbols/pt_rod.$TIMESTAMP.bkp;
fi
ln -s $SCRIPTDIR/pt_rod $XKBDIR/symbols/pt_rod

if [[ -e $XKBDIR/symbols/us_rod ]]; then
    mv $XKBDIR/symbols/us_rod $XKBDIR/symbols/us_rod.$TIMESTAMP.bkp;
fi
ln -s $SCRIPTDIR/us_rod $XKBDIR/symbols/us_rod
