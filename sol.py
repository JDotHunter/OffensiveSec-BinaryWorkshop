from pwn import *

io = process('./time')
print(io.recvuntil(b'Enter your number: '))
io.sendline(b'90')
display = io.recvline()
print(display)


