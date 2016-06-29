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

def get_window():
    screen = wnck.screen_get_default()

    ## ensures get_windows() isn't empty --> http://stackoverflow.com/a/5364596/997624
    while gtk.events_pending():
        gtk.main_iteration()

    window_list = screen.get_windows()


    ## get saved_pid
    cwd = os.path.dirname(os.path.realpath(__file__))
    pid_filename = cwd + "/windowsummon_pid.dat"
    pid_file = open(pid_filename, 'rw')
    pid_file_contents = pid_file.read()
    pid_file.close()

    if pid_file_contents != '':
        saved_pid = int(pid_file_contents)
    else:
        saved_pid = None


    active_window = screen.get_active_window()

    aw_pid = None
    if active_window:
        aw_pid = active_window.get_pid()

    # msg = aw_pid, "(" + str(saved_pid) + ")"
    # print msg
    # msgbox(msg)

    if aw_pid == saved_pid:
        # hide the window
        active_window.minimize()
        print "window minimized"
        main.quit()
        return

    else:
        for window in window_list:

            # msg = window.get_name(), window.get_pid(), "(" + str(saved_pid) + ")"
            # print msg
            # msgbox(msg)

            if window.get_pid() == saved_pid:
                # msg = "MATCH FOUND, GET_PID = SAVED_PID"
                # print msg
                # msgbox(msg)

                window.pin()
                window.activate(0)

                main.quit()
                return
        print "NO MATCH FOUND, GET_PID != SAVED_PID"
        # proc = subprocess.Popen(sys.argv[1:], shell=False)
        # time.sleep(3)
        # pid = proc.pid
        # window_list = screen.get_windows()
        # for window in window_list:
        #     pdb.set_trace()
        #     if window.is_most_recently_activated():
        #         aw_pid = window.get_pid()
        # #active_window = screen.get_active_window()
        # #aw_pid = active_window.get_pid()
        # for window in window_list: print window.get_pid()
        # print "aw_pid: ", aw_pid

        # pid_file = open(pid_filename, 'w+')
        # pid_file.write(str(aw_pid))
        # pid_file.close()

    main.quit()
    return

glib.idle_add(get_window)
main.run()