import ctypes
from ctypes import POINTER

so_file = "./csort.so"
c_sort = ctypes.CDLL(so_file)
pysort = c_sort.sort
pysort.argtypes = [POINTER(ctypes.c_int), ctypes.c_size_t, ctypes.c_char]  # TODO
pysort.restype = POINTER(ctypes.c_int)

def csort(in_arr: list[int], order: int) -> None:
    """
    Call C program to perform sorting function

    Args:
        in_arr (list[int]): integer array to sort
        order (int): 0 for ascending. 1 or otherwise for descending

    Returns:
        list[int]: sorted array
    """
    arr_size = len(in_arr)
    
    #ctype conversions
    size = ctypes.c_size_t(arr_size)
    def_arr = (ctypes.c_int * arr_size)(*in_arr)
    c_order = ctypes.c_char(order)

    pysort(def_arr, size, c_order)

    in_arr[:] = def_arr[:arr_size]
        
    #return sorted_arr
