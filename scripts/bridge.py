import ctypes
import os

LIB_PATH = os.path.join(os.path.dirname(__file__), "../core/libengine.so")

def get_engine():
    lib = ctypes.CDLL(LIB_PATH)
    
    # Existing get_distance config
    lib.get_distance.restype = ctypes.c_float
    lib.get_distance.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float]
    
    # NEW: Configure the march function
    # Arguments: roX, roY, roZ (origin), rdX, rdY, rdZ (direction)
    lib.march.restype = ctypes.c_float
    lib.march.argtypes = [ctypes.c_float]*6
    
    return lib
