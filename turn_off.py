# fp
Turn off PC!
import os, time, sys, win32gui, win32con
from threading import Timer

class Turn_off:
    def __init__(self, time_limit):
         self.time_limit = time_limit
         eku = Timer(time_limit, self.force_exit)
         eku.start()
# вырубает экран. комп остается включенныймб только дисплей вырубает!
    def force_exit(self):
        my_display = 0xF170
        win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, my_display, 2)
       
#если хочкшь вырубить сам комп то вместо (def force_exit(self):.....) поставь     """def force_exit(self): os.system("shutdown /s /t 1")"""         
     
    """def force_exit(self):
        os.system("shutdown /s /t 1")"""
