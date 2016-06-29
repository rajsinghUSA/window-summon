#!/usr/bin/env python

import gtk
import wnck
import subprocess
import glib
#import gio
import os
import sys
import time
import json
import pdb


main = glib.MainLoop()

def set_window():

    screen = wnck.screen_get_default()

    ## ensures get_windows() isn't empty --> http://stackoverflow.com/a/5364596/997624
    while gtk.events_pending():
        gtk.main_iteration()

    # window_list = screen.get_windows()
    active_window = screen.get_active_window()
    aw_pid = active_window.get_pid()

    print "SAVED PID ", aw_pid

    cwd = os.path.dirname(os.path.realpath(__file__))
    pid_filename = cwd + "/windowsummon_pid.dat"
    pid_file = open(pid_filename, 'w')

    pid_file.write(str(aw_pid))
    pid_file.close()

    main.quit()
    return


glib.idle_add(set_window)
main.run()
