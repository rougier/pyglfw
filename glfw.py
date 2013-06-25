# -----------------------------------------------------------------------------
#  GLFW - An OpenGL framework
#  API version: 3.0.1
#  WWW:         http://www.glfw.org/
#  ----------------------------------------------------------------------------
#  Copyright (c) 2002-2006 Marcus Geelnard
#  Copyright (c) 2006-2010 Camilla Berglund
#
#  Python bindings - Copyright (c) 2013 Nicolas P. Rougier
#  
#  This software is provided 'as-is', without any express or implied
#  warranty. In no event will the authors be held liable for any damages
#  arising from the use of this software.
#  
#  Permission is granted to anyone to use this software for any purpose,
#  including commercial applications, and to alter it and redistribute it
#  freely, subject to the following restrictions:
#  
#  1. The origin of this software must not be misrepresented; you must not
#     claim that you wrote the original software. If you use this software
#     in a product, an acknowledgment in the product documentation would
#     be appreciated but is not required.
#  
#  2. Altered source versions must be plainly marked as such, and must not
#     be misrepresented as being the original software.
#  
#  3. This notice may not be removed or altered from any source
#     distribution.
#  
# -----------------------------------------------------------------------------
import os,sys
import ctypes
import ctypes.util
from ctypes import *

_glfw_file = None

# First if there is an environment variable pointing to the library
if 'GLFW_LIBRARY' in os.environ:
    if os.path.exists(os.environ['GLFW_LIBRARY']):
        _glfw_file = os.path.realpath(os.environ['GLFW_LIBRARY'])

# Else, try to find it
if _glfw_file is None:
    _glfw_file = ctypes.util.find_library('glfw')

# Else, we failed and exit
if _glfw_file is None:
    raise( RuntimeError, 'GLFW library not found' )

_glfw = CDLL(_glfw_file)



# --- Version -----------------------------------------------------------------
VERSION_MAJOR      = 3
VERSION_MINOR      = 0
VERSION_REVISION   = 1
__version__ = VERSION_MAJOR, VERSION_MINOR, VERSION_REVISION 

# --- Input handling definitions ----------------------------------------------
RELEASE            = 0
PRESS              = 1
REPEAT             = 2

# --- Keys --------------------------------------------------------------------

# --- The unknown key ---------------------------------------------------------
KEY_UNKNOWN          = -1

# --- Printable keys ----------------------------------------------------------
KEY_SPACE            = 32
KEY_APOSTROPHE       = 39 # ''
KEY_COMMA            = 44 # ,
KEY_MINUS            = 45 # -
KEY_PERIOD           = 46 # .
KEY_SLASH            = 47 # /
KEY_0                = 48
KEY_1                = 49
KEY_2                = 50
KEY_3                = 51
KEY_4                = 52
KEY_5                = 53
KEY_6                = 54
KEY_7                = 55
KEY_8                = 56
KEY_9                = 57
KEY_SEMICOLON        = 59 # ;
KEY_EQUAL            = 61 # =
KEY_A                = 65
KEY_B                = 66
KEY_C                = 67
KEY_D                = 68
KEY_E                = 69
KEY_F                = 70
KEY_G                = 71
KEY_H                = 72
KEY_I                = 73
KEY_J                = 74
KEY_K                = 75
KEY_L                = 76
KEY_M                = 77
KEY_N                = 78
KEY_O                = 79
KEY_P                = 80
KEY_Q                = 81
KEY_R                = 82
KEY_S                = 83
KEY_T                = 84
KEY_U                = 85
KEY_V                = 86
KEY_W                = 87
KEY_X                = 88
KEY_Y                = 89
KEY_Z                = 90
KEY_LEFT_BRACKET     = 91  # [
KEY_BACKSLASH        = 92  # \
KEY_RIGHT_BRACKET    = 93  # ]
KEY_GRAVE_ACCENT     = 96  # `
KEY_WORLD_1          = 161 # non-US #1
KEY_WORLD_2          = 162 # non-US #2

# --- Function keys -----------------------------------------------------------
KEY_ESCAPE           = 256
KEY_ENTER            = 257
KEY_TAB              = 258
KEY_BACKSPACE        = 259
KEY_INSERT           = 260
KEY_DELETE           = 261
KEY_RIGHT            = 262
KEY_LEFT             = 263
KEY_DOWN             = 264
KEY_UP               = 265
KEY_PAGE_UP          = 266
KEY_PAGE_DOWN        = 267
KEY_HOME             = 268
KEY_END              = 269
KEY_CAPS_LOCK        = 280
KEY_SCROLL_LOCK      = 281
KEY_NUM_LOCK         = 282
KEY_PRINT_SCREEN     = 283
KEY_PAUSE            = 284
KEY_F1               = 290
KEY_F2               = 291
KEY_F3               = 292
KEY_F4               = 293
KEY_F5               = 294
KEY_F6               = 295
KEY_F7               = 296
KEY_F8               = 297
KEY_F9               = 298
KEY_F10              = 299
KEY_F11              = 300
KEY_F12              = 301
KEY_F13              = 302
KEY_F14              = 303
KEY_F15              = 304
KEY_F16              = 305
KEY_F17              = 306
KEY_F18              = 307
KEY_F19              = 308
KEY_F20              = 309
KEY_F21              = 310
KEY_F22              = 311
KEY_F23              = 312
KEY_F24              = 313
KEY_F25              = 314
KEY_KP_0             = 320
KEY_KP_1             = 321
KEY_KP_2             = 322
KEY_KP_3             = 323
KEY_KP_4             = 324
KEY_KP_5             = 325
KEY_KP_6             = 326
KEY_KP_7             = 327
KEY_KP_8             = 328
KEY_KP_9             = 329
KEY_KP_DECIMAL       = 330
KEY_KP_DIVIDE        = 331
KEY_KP_MULTIPLY      = 332
KEY_KP_SUBTRACT      = 333
KEY_KP_ADD           = 334
KEY_KP_ENTER         = 335
KEY_KP_EQUAL         = 336
KEY_LEFT_SHIFT       = 340
KEY_LEFT_CONTROL     = 341
KEY_LEFT_ALT         = 342
KEY_LEFT_SUPER       = 343
KEY_RIGHT_SHIFT      = 344
KEY_RIGHT_CONTROL    = 345
KEY_RIGHT_ALT        = 346
KEY_RIGHT_SUPER      = 347
KEY_MENU             = 348
KEY_LAST             = KEY_MENU


# --- Modifiers ---------------------------------------------------------------
MOD_SHIFT            = 0x0001
MOD_CONTROL          = 0x0002
MOD_ALT              = 0x0004
MOD_SUPER            = 0x0008

# --- Mouse -------------------------------------------------------------------
MOUSE_BUTTON_1       = 0
MOUSE_BUTTON_2       = 1
MOUSE_BUTTON_3       = 2
MOUSE_BUTTON_4       = 3
MOUSE_BUTTON_5       = 4
MOUSE_BUTTON_6       = 5
MOUSE_BUTTON_7       = 6
MOUSE_BUTTON_8       = 7
MOUSE_BUTTON_LAST    = MOUSE_BUTTON_8
MOUSE_BUTTON_LEFT    = MOUSE_BUTTON_1
MOUSE_BUTTON_RIGHT   = MOUSE_BUTTON_2
MOUSE_BUTTON_MIDDLE  = MOUSE_BUTTON_3


# --- Joystick ----------------------------------------------------------------
JOYSTICK_1           = 0
JOYSTICK_2           = 1
JOYSTICK_3           = 2
JOYSTICK_4           = 3
JOYSTICK_5           = 4
JOYSTICK_6           = 5
JOYSTICK_7           = 6
JOYSTICK_8           = 7
JOYSTICK_9           = 8
JOYSTICK_10          = 9
JOYSTICK_11          = 10
JOYSTICK_12          = 11
JOYSTICK_13          = 12
JOYSTICK_14          = 13
JOYSTICK_15          = 14
JOYSTICK_16          = 15
JOYSTICK_LAST        = JOYSTICK_16


# --- Error codes -------------------------------------------------------------
NOT_INITIALIZED        = 0x00010001
NO_CURRENT_CONTEXT     = 0x00010002
INVALID_ENUM           = 0x00010003
INVALID_VALUE          = 0x00010004
OUT_OF_MEMORY          = 0x00010005
API_UNAVAILABLE        = 0x00010006
VERSION_UNAVAILABLE    = 0x00010007
PLATFORM_ERROR         = 0x00010008
FORMAT_UNAVAILABLE     = 0x00010009

# ---
FOCUSED                = 0x00020001
ICONIFIED              = 0x00020002
RESIZABLE              = 0x00020003
VISIBLE                = 0x00020004
DECORATED              = 0x00020005

# --- 
RED_BITS               = 0x00021001
GREEN_BITS             = 0x00021002
BLUE_BITS              = 0x00021003
ALPHA_BITS             = 0x00021004
DEPTH_BITS             = 0x00021005
STENCIL_BITS           = 0x00021006
ACCUM_RED_BITS         = 0x00021007
ACCUM_GREEN_BITS       = 0x00021008
ACCUM_BLUE_BITS        = 0x00021009
ACCUM_ALPHA_BITS       = 0x0002100A
AUX_BUFFERS            = 0x0002100B
STEREO                 = 0x0002100C
SAMPLES                = 0x0002100D
SRGB_CAPABLE           = 0x0002100E
REFRESH_RATE           = 0x0002100F

# --- 
CLIENT_API             = 0x00022001
CONTEXT_VERSION_MAJOR  = 0x00022002
CONTEXT_VERSION_MINOR  = 0x00022003
CONTEXT_REVISION       = 0x00022004
CONTEXT_ROBUSTNESS     = 0x00022005
OPENGL_FORWARD_COMPAT  = 0x00022006
OPENGL_DEBUG_CONTEXT   = 0x00022007
OPENGL_PROFILE         = 0x00022008

# --- 
OPENGL_API             = 0x00030001
OPENGL_ES_API          = 0x00030002

# --- 
NO_ROBUSTNESS          =          0
NO_RESET_NOTIFICATION  = 0x00031001
LOSE_CONTEXT_ON_RESET  = 0x00031002

# --- 
OPENGL_ANY_PROFILE     =          0
OPENGL_CORE_PROFILE    = 0x00032001
OPENGL_COMPAT_PROFILE  = 0x00032002

# --- 
CURSOR                 = 0x00033001
STICKY_KEYS            = 0x00033002
STICKY_MOUSE_BUTTONS   = 0x00033003

# --- 
CURSOR_NORMAL          = 0x00034001
CURSOR_HIDDEN          = 0x00034002
CURSOR_DISABLED        = 0x00034003

# --- 
CONNECTED              = 0x00040001
DISCONNECTED           = 0x00040002


# --- Structures --------------------------------------------------------------
class vidmode_st(Structure):
    _fields_ = [ ('width',       c_int),
                 ('height',      c_int),
                 ('redBits',     c_int),
                 ('greenBits',   c_int),
                 ('blueBits',    c_int),
                 ('refreshRate', c_int) ]

class gammaramp_st(Structure):
    _fields_ = [ ('red',     POINTER(c_ushort)),
                 ('green',   POINTER(c_ushort)),
                 ('blue',    POINTER(c_ushort)),
                 ('size',    c_int) ]

class window_st(Structure): pass
class monitor_st(Structure): pass

# --- Callbacks ---------------------------------------------------------------
errorfun           = CFUNCTYPE(None, c_int, c_char_p)
windowposfun       = CFUNCTYPE(None, POINTER(window_st), c_int, c_int)
windowsizefun      = CFUNCTYPE(None, POINTER(window_st), c_int, c_int)
windowclosefun     = CFUNCTYPE(None, POINTER(window_st))
windowrefreshfun   = CFUNCTYPE(None, POINTER(window_st))
windowfocusfun     = CFUNCTYPE(None, POINTER(window_st), c_int)
windowiconifyfun   = CFUNCTYPE(None, POINTER(window_st), c_int)
framebuffersizefun = CFUNCTYPE(None, POINTER(window_st), c_int, c_int)
mousebuttonfun     = CFUNCTYPE(None, POINTER(window_st), c_int, c_int, c_int)
cursorposfun       = CFUNCTYPE(None, POINTER(window_st), c_double, c_double)
cursorenterfun     = CFUNCTYPE(None, POINTER(window_st), c_int)
scrollfun          = CFUNCTYPE(None, POINTER(window_st), c_double, c_double)
keyfun             = CFUNCTYPE(None, POINTER(window_st), c_int, c_int, c_int, c_int)
charfun            = CFUNCTYPE(None, POINTER(window_st), c_uint)
monitorfun         = CFUNCTYPE(None, POINTER(monitor_st), c_int)

# --- Init --------------------------------------------------------------------
Init                        = _glfw.glfwInit
Terminate                   = _glfw.glfwTerminate
#GetVersion                 = _glfw.glfwGetVersion
GetVersionString            = _glfw.glfwGetVersionString
GetVersionString.restype    = c_char_p


# --- Error -------------------------------------------------------------------
#SetErrorCallback            = _glfw.glfwSetErrorCallback

# --- Monitor -----------------------------------------------------------------
# GetMonitors                 = _glfw.glfwGetMonitors
# GetMonitors.restype         = POINTER(monitor_st)
GetPrimaryMonitor           = _glfw.glfwGetPrimaryMonitor
# GetMonitorPos               = _glfw.glfwGetMonitorPos
# GetMonitorPhysicalSize      = _glfw.glfwGetMonitorPhysicalSize
GetMonitorName              = _glfw.glfwGetMonitorName
GetMonitorName.restype = c_char_p
#SetMonitorCallback          = _glfw.glfwSetMonitorCallback
#GetVideoModes               = _glfw.glfwGetVideoModes
#GetVideoMode                = _glfw.glfwGetVideoMode

# --- Gama --------------------------------------------------------------------
SetGamma                   = _glfw.glfwSetGamma
#GetGammaRamp               = _glfw.glfwGetGammaRamp
#SetGammaRamp               = _glfw.glfwSetGammaRamp

# --- Window ------------------------------------------------------------------
DefaultWindowHints         = _glfw.glfwDefaultWindowHints
WindowHint                 = _glfw.glfwWindowHint
# CreateWindow              = _glfw.glfwCreateWindow
# DestroyWindow              = _glfw.glfwDestroyWindow
WindowShouldClose          = _glfw.glfwWindowShouldClose
SetWindowShouldClose       = _glfw.glfwSetWindowShouldClose
SetWindowTitle             = _glfw.glfwSetWindowTitle
# GetWindowPos              = _glfw.glfwGetWindowPos
SetWindowPos               = _glfw.glfwSetWindowPos
# GetWindowSize             = _glfw.glfwGetWindowSize
SetWindowSize              = _glfw.glfwSetWindowSize
# GetFramebufferSize        = _glfw.glfwGetFramebufferSize
IconifyWindow              = _glfw.glfwIconifyWindow
RestoreWindow              = _glfw.glfwRestoreWindow
ShowWindow                 = _glfw.glfwShowWindow
HideWindow                 = _glfw.glfwHideWindow
GetWindowMonitor           = _glfw.glfwGetWindowMonitor
GetWindowAttrib            = _glfw.glfwGetWindowAttrib
SetWindowUserPointer       = _glfw.glfwSetWindowUserPointer
GetWindowUserPointer       = _glfw.glfwGetWindowUserPointer
#SetWindowPosCallback       = _glfw.glfwSetWindowPosCallback
#SetWindowSizeCallback      = _glfw.glfwSetWindowSizeCallback
#SetWindowCloseCallback     = _glfw.glfwSetWindowCloseCallback
#SetWindowRefreshCallback   = _glfw.glfwSetWindowRefreshCallback
#SetWindowFocusCallback     = _glfw.glfwSetWindowFocusCallback
#SetWindowIconifyCallback   = _glfw.glfwSetWindowIconifyCallback
#SetFramebufferSizeCallback = _glfw.glfwSetFramebufferSizeCallback
PollEvents                 = _glfw.glfwPollEvents
WaitEvents                 = _glfw.glfwWaitEvents

# --- Input -------------------------------------------------------------------
GetInputMode               = _glfw.glfwGetInputMode
SetInputMode               = _glfw.glfwSetInputMode
GetKey                     = _glfw.glfwGetKey
GetMouseButton             = _glfw.glfwGetMouseButton
#GetCursorPos               = _glfw.glfwGetCursorPos
SetCursorPos               = _glfw.glfwSetCursorPos
#SetKeyCallback             = _glfw.glfwSetKeyCallback
#SetCharCallback            = _glfw.glfwSetCharCallback
#SetMouseButtonCallback     = _glfw.glfwSetMouseButtonCallback
#SetCursorPosCallback       = _glfw.glfwSetCursorPosCallback
#SetCursorEnterCallback     = _glfw.glfwSetCursorEnterCallback
#SetScrollCallback          = _glfw.glfwSetScrollCallback
JoystickPresent            = _glfw.glfwJoystickPresent
# GetJoystickAxes            = _glfw.glfwGetJoystickAxes
# GetJoystickButtons         = _glfw.glfwGetJoystickButtons
GetJoystickName            = _glfw.glfwGetJoystickName
GetJoystickName.restype = c_char_p

# --- Clipboard ---------------------------------------------------------------
SetClipboardString         = _glfw.glfwSetClipboardString
GetClipboardString         = _glfw.glfwGetClipboardString
GetClipboardString.restype = c_char_p

# --- Timer -------------------------------------------------------------------
GetTime                    = _glfw.glfwGetTime
GetTime.restype = c_double
SetTime                    = _glfw.glfwSetTime

# --- Context -----------------------------------------------------------------
MakeContextCurrent         = _glfw.glfwMakeContextCurrent
GetCurrentContext          = _glfw.glfwGetCurrentContext
SwapBuffers                = _glfw.glfwSwapBuffers
SwapInterval               = _glfw.glfwSwapInterval
ExtensionSupported         = _glfw.glfwExtensionSupported
GetProcAddress             = _glfw.glfwGetProcAddress



# --- Pythonizer --------------------------------------------------------------

# This keeps track of current windows
__windows__ = []

# This is to prevent garbage collection on callbacks
__c_callbacks__ = {}
__py_callbacks__ = {}


def CreateWindow(width=640, height=480, title="GLFW Window", monitor=None, share=None):
    _glfw.glfwCreateWindow.restype = POINTER(window_st)
    window = _glfw.glfwCreateWindow(width,height,title,monitor,share)
    __windows__.append(window)
    index = __windows__.index(window)
    __c_callbacks__[index] = {}
    __py_callbacks__[index] = { 'errorfun'           : None,
                                'monitorfun'         : None,
                                'windowposfun'       : None,
                                'windowsizefun'      : None,
                                'windowclosefun'     : None,
                                'windowrefreshfun'   : None,
                                'windowfocusfun'     : None,
                                'windowiconifyfun'   : None,
                                'framebuffersizefun' : None,
                                'keyfun'             : None,
                                'charfun'            : None,
                                'mousebuttonfun'     : None,
                                'cursorposfun'       : None,
                                'cursorenterfun'     : None,
                                'scrollfun'          : None }
    return window

def DestroyWindow(window):
    index = __windows__.index(window)
    _glfw.glfwDestroyWindow(window)
    # We do not delete window from the list (or it would impact windows numbering)
    # del __windows__[index]
    del __c_callbacks__[index]
    del __py_callbacks__[index]


def GetVersion():
    major, minor, rev = c_int(0), c_int(0), c_int(0)
    _glfw.glfwGetVersion( byref(major), byref(minor), byref(rev) )
    return major.value, minor.value, rev.value

def GetWindowPos(window):
    xpos, ypos = c_int(0), c_int(0)
    _glfw.glfwGetWindowPos(window, byref(xpos), byref(ypos))
    return xpos.value, ypos.value

def GetCursorPos(window):
    xpos, ypos = c_int(0), c_int(0)
    _glfw.glfwGetCursorPos(window, byref(xpos), byref(ypos))
    return xpos.value, ypos.value

def GetWindowSize(window):
    width, height = c_int(0), c_int(0)
    _glfw.glfwGetWindowSize(window, byref(width), byref(height))
    return width.value, height.value

def GetFramebufferSize(window):
    width, height = c_int(0), c_int(0)
    _glfw.glfwGetFramebufferSize(window, byref(width), byref(height))
    return width.value, height.value


def GetMonitors():
    count = c_int(0)
    _glfw.glfwGetMonitors.restype = POINTER(POINTER(monitor_st))
    c_monitors = _glfw.glfwGetMonitors( byref(count) )
    return [c_monitors[i] for i in range(count.value)]

def GetVideoModes(monitor):
    count = c_int(0)
    _glfw.glfwGetVideoModes.restype = POINTER(vidmode_st)
    c_modes = _glfw.glfwGetVideoModes( monitor, byref(count) )
    modes = []
    for i in range(count.value):
        modes.append( (c_modes[i].width,
                       c_modes[i].height,
                       c_modes[i].redBits,
                       c_modes[i].blueBits,
                       c_modes[i].greenBits,
                       c_modes[i].refreshRate ) )
    return modes

def GetMonitorPos(monitor):
    xpos, ypos = c_int(0), c_int(0)
    _glfw.glfwGetMonitorPos(monitor, byref(xpos), byref(ypos))
    return xpos.value, ypos.value

def GetMonitorPhysicalSize(monitor):
    width, height = c_int(0), c_int(0)
    _glfw.glfwGetMonitorPhysicalSize(monitor, byref(width), byref(height))
    return width.value, height.value

def GetVideoMode(monitor):
    _glfw.glfwGetVideoMode.restype = POINTER(vidmode_st)
    c_mode = _glfw.glfwGetVideoModes(monitor)
    return (c_modes.width,
            c_modes.height,
            c_modes.redBits,
            c_modes.blueBits,
            c_modes.greenBits,
            c_modes.refreshRate )

def GetGammaRamp(monitor):
    _glfw.glfwGetGammaRamp.restype = POINTER(gammaramp_st)
    c_gamma = _glfw.glfwGetGammaRamp(monitor).contents
    gamma = {'red':[], 'green':[], 'blue':[]}
    if c_gamma:
        for i in range(c_gamma.size):
            gamma['red'].append(c_gamma.red[i])
            gamma['green'].append(c_gamma.green[i])
            gamma['blue'].append(c_gamma.blue[i])
    return gamma

def GetJoystickAxes(joy):
    count = c_int(0)
    _glfw.glfwGetJoystickAxes.restype = POINTER(c_float)
    c_axes = _glfw.glfwGetJoystickAxes(joy, byref(count))
    axes = [c_axes[i].value for i in range(count)]

def GetJoystickButtons(joy):
    count = c_int(0)
    _glfw.glfwGetJoystickButtons.restype = POINTER(c_int)
    c_buttons = _glfw.glfwGetJoystickButtons(joy, byref(count))
    buttons = [c_buttons[i].value for i in range(count)]


# --- Callbacks ---------------------------------------------------------------

def __callback__(name):
    callback = 'Set%sCallback' % name
    fun      = '%sfun' % name.lower()
    code = """
def %(callback)s(window, callback = None):
    index = __windows__.index(window)
    old_callback = __py_callbacks__[index]['%(fun)s']
    __py_callbacks__[index]['%(fun)s'] = callback
    if callback: callback = %(fun)s(callback)
    __c_callbacks__[index]['%(fun)s'] = callback
    _glfw.glfw%(callback)s(window, callback)
    return old_callback"""  % {'callback': callback, 'fun': fun}
    return code

exec __callback__('Error')
exec __callback__('Monitor')
exec __callback__('WindowPos')
exec __callback__('WindowSize')
exec __callback__('WindowClose')
exec __callback__('WindowRefresh')
exec __callback__('WindowFocus')
exec __callback__('WindowIconify')
exec __callback__('FramebufferSize')
exec __callback__('Key')
exec __callback__('Char')
exec __callback__('MouseButton')
exec __callback__('CursorPos')
exec __callback__('Scroll')
