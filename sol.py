from pwn import *

io = process('sh')
io.sendline(b'echo Hello World')
object = io.recvline()
print(object)

