# fp
Turn off PC!
import os, time, sys, win32gui, win32con
from threading import Timer

class Turn_off:
    def __init__(self, time_limit):
         self.time_limit = time_limit
         eku = Timer(time_limit, self.force_exit)
         eku.start()

    def force_exit(self):
        my_display = 0xF170
        win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, my_display, 2)

    """def force_exit(self):
        os.system("shutdown /s /t 1")"""
