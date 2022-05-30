import ctypes

import faulthandler; faulthandler.enable()

ctypes.memset(0, 254, 1)
