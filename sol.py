
from pwn import *
from ctypes import CDLL

libc = CDLL("libc.so.6")

the_time = libc.srand(libc.time(0))

time = libc.rand()

print(time)


io = process('./time')
print(io.recvuntil(b'Enter your number: '))
io.sendline(b'%d' % time)
display = io.recvline()
print(display)
print(io.recvall())


