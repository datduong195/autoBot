import ctypes
import time
hllDll = ctypes.WinDLL ("User32.dll")
W = 0x11
A = 0x1E
S = 0x1F
D = 0x20
UP = 0xC8
LEFT = 0xCB
RIGHT = 0xCD
DOWN = 0xD0
ENTER = 0x1C
ESC = 0x01
TWO = 0x03
NUMLCK = 0x45
LCTRL = 0x1D#define DIK_LCONTROL        0x1D
VK_NUMLOCK = 0x90

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
def pressKey(key):
    PressKey(key)
    time.sleep(1)
    ReleaseKey(key)
    time.sleep(1)
def pattern_1():
    pressKey(LEFT)
    pressKey(LEFT)
    pressKey(LCTRL)
    pressKey(LCTRL)
    pressKey(LEFT)
    pressKey(LEFT)
    pressKey(W)
    pressKey(A)
    pressKey(RIGHT)
    pressKey(RIGHT)
    pressKey(D)
    pressKey(S)
def pattern_2():
    pressKey(LEFT)
    pressKey(LEFT)
    pressKey(D)
    pressKey(A)
    pressKey(LEFT)
    pressKey(LEFT)
    pressKey(W)
    pressKey(S)  
    pressKey(RIGHT)
    pressKey(RIGHT)
    pressKey(LCTRL)
    pressKey(LCTRL)
# directx scan codes
# http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
if __name__ == '__main__':
    
    if(hllDll.GetKeyState(VK_NUMLOCK)):
        pressKey(NUMLCK)
    while (True):
        pattern_1()
        pattern_2()
        



#https://guidedhacking.com/threads/creating-a-c-bot-that-sends-keystrokes-and-mouse-movement.11837/
#https://guidedhacking.com/threads/maplestory-packet-hack-ngs-bypass.14202/
#https://bitbucket.org/mambda/maple-syrup/src/master/Maple%20Syrup/
