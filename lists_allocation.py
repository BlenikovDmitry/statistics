import time
import numpy as np


def list_comp(num):
    return [i for i in range(num)]


def prealloc(num):
    lst = [None] * num
    for i in range(num):
        lst[i] = i
        
    return lst


def append_meth(num):
    lst = []
    for i in range(num):
        lst.append(i)

    return lst

def numpy_arr(num):
    return np.arange(1, num+1)

lst = []
time_start = time.time()
lst  = list_comp(100000000)
time_end = time.time()

print(f'list_comp {time_end - time_start}')

time_start = time.time()
lst  = prealloc(100000000)
time_end = time.time()

print(f'prealloc {time_end - time_start}')

time_start = time.time()
lst  = append_meth(100000000)
time_end = time.time()

print(f'append_meth {time_end - time_start}')

time_start = time.time()
lst  = numpy_arr(100000000)
time_end = time.time()

print(f'numpy_arr {time_end - time_start}')
