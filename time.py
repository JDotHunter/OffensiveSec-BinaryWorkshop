#!/usr/bin/env python

from ctypes import CDLL

libc = CDLL("libc.so.6")

the_time = libc.srand(libc.time(0))

time = libc.rand()

print(time)
