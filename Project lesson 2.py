import sys

if sys.platform == 'win11':

    import ctypes
    user32 = ctypes.WinDLL('user32')
    user32.ExitWindowsEx(0x00000008, 0x00000000)

else:

    import os
    os.system('sudo shutdown now')