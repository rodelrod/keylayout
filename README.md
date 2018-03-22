Usage
=====

These instructions are valid in Ubuntu up to 16.04 at least. It may
break if you're using Wayland instead of X11.

 1. Copy the keyboard definition file (e.g. `us_rod`) to `/usr/share/X11/xkb/symbols`.
 
 2. Open the layouts file (`/usr/share/X11/xkb/rules/evdev.xml`), above the 
    `<layoutList/>` closing tag, paste the XML snippet with the layout definition
    (e.g. `us_rod_layout.xml`). 


Notes
-----

In the layout definition's `shortDescription` tag, only some results are accepted,
such as "en" or "pt". If you pick, for example, "us", the keyboard icon in the panel
indicator will still active, but will have a dark background.

To reload changes you must log in and out of the X session.
