#Anger crackme CTF Documentation

##This doc outlines what the angr framework is as a whole and some of the steps taken to solve this challenge

###Background on Angr
* Angr is an open-source Binary analysis framework based in Python. It was developed by
  researchers from the Computer Security Lab at UC Santa Barbara in order to streamline
  the process of binary analysis and binary exploitation capabilities. Angr hs multiple
  features including but not limited to: automatic exploit generation, symbolic execution,
  and automatic ROP chain building, making it an incredibly powerful tool. 


###Problem Outline
* Normally, we'd use ghidra to decompile the file and analyze the source code. However,
  we downloaded the angr elf-crackme from the corresponding github page https://github.com/reversinghub/crackme-angr-elf/blob/master/README.md
  and from there, we had access to the crackme.c file. We used that in order to figure out
  our objective.


* Crackme.c is a password file verification challenge. To solve (secure the flag), we have
  to input a password that matches a specific 10-character sequence.

* After the user enters a 10-character password (the variable called flag), each character that we enter is used to
  index into a linked list structure (called myNode) that will construct a new string.

* After the new string is constructed, the string is compared to the predefined password
  that we're given. If they match, then we secure the flag and win the challenge. If 
  they're not the same, then we receive an error message.


###Solution
* To solve this, we must first understand how the linked list structure works.
  Again, each character that the user enters in the 10-character password is used as
  an index into a linked list structure that constructs a new string.

* After the new string is constructed, we compare the predefined password to our new
  password and determine their similarity.

* Write out a Python script to determine the similarity of the passwords and record
 their validity.

* #!/usr/bin/python3

import angr
import claripy

proj = angr.Project(
        'crackme', 
        main_opts = {'base_addr': 0x0}, 
        load_options = {'auto_load_libs': False}
)

# Flag is 10 characters
flag = claripy.BVS("flag", 8 * 10)

state = proj.factory.entry_state(stdin = flag) 

# Silence the warnings
state.options.add(angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY)

# Flags consists only on numbers ('0' -> '9')
for i in range(10):
    state.solver.add(flag.get_byte(i) >= 48)
    state.solver.add(flag.get_byte(i) <= 57)

sm = proj.factory.simulation_manager(state)

FIND_ADDR = 0x1219   # 'Congratualtions ...' message
AVOID_ADDR = 0x1227  # 'Try again ...' message

sm.explore(find = FIND_ADDR, avoid = AVOID_ADDR)

print("[*] Flag found: " + sm.found[0].posix.dumps(0).decode("utf-8")) 

