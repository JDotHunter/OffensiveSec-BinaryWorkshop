#Angr r100 CTF Documentation

##This document outlines the steps and methodologies used to complete the angr r100 angr challenge including python, ghidra, the angr library, and virtual environments.


###Utilizing & Traversing Ghidra
What is Ghidra? Ghidra is an open-source reverse engineering tool developed by the NSA.
It is a powerful tool that allows us to disassemble, analyze, and execute binary files.

* To begin, we open up Ghidra within the Kali Linux terminal and create a new project

* We import the target binary (the angr file) into our project 

* We analyze and decompile the angr r100 file and sift through the functions to see if we
  find anything worth noting (A flag, a success message, a failure message, etc.)

* In the decompile function that shows us the source code, we find an important function.



###Analysis of the Code & File
The purpose behind analyzing the code in Ghidra is to identify any potential vulnerabilities
(if any at all). We're able to inspect function calls and calls that are made to other functions.

Observations:

* There are two function calls to puts. One that shows the user correctly guessing the password
  and presenting the user with the flag. The second call outputs an error message in the event
  the user guesses the password incorrectly. This tells us that if the we're able to determine
  the correct password, then we'll complete the challenge. Additionally, if we're able to
  determine where to go in memory, then we can directly access the win condition.

* The outcome of the file command on the r100 file: r100: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.24, BuildID[sha1]=0f464824cc8ee321ef9a80a799c70b1b6aec8168, stripped

* The outcome of the checksec command on the r100 file: RELRO STACK CANARY NX PIE RPATH RUNPATH SymbolsFORTIFY Fortified Fortifiable FILE Partial RELRO Canary found NX enabled No PIE No RPATH No RUNPATH No Symbols No 0 2 r100



###Identifying the Target Memory Address
After finding and exploiting the buffer overflow vulnerability, finding the desired memory address
that you want to return to is pivotal.  

* Analyze the Binary: Use ghidra to identify the memory address that we want to redirect execution to.

* Record the Address: After identifying the address, make a note of it somewhere as it will
  be used later in the payload to override the return address.

* Desired Address: The memory address that we want to reroute execution to.

* Incorrect Address: The address that we want to avoid; We should jot this down somewhere
  too for this reason.



###The Python Program
#  Import Angr
import angr

# Establish the Angr Project
target = angr.Project('r100')

# Specify the desired address which means we have the correct input
desired_adr = 0x400849

# Specify the address which if it executes means we don't have the correct input
wrong_adr = 0x40085a

# Establish the entry state
entry_state = target.factory.entry_state(args=["./fairlight"])

# Establish the simulation
simulation = target.factory.simulation_manager(entry_state)

# Start the simulation
simulation.explore(find = desired_adr, avoid = wrong_adr)

solution = simulation.found[0].posix.dumps(0)
print(solution)



###Conclusion
We ran into a roadblock in this process due to how Python3 is configured within our Kali Linux
terminal. This prevented commands that would normally work within the terminal to fail.
To work around this, we created a virtual environment that allows us to utilize the full
extension of the angr library as well as having access to all of the commands that we need.
This was the final step in getting the password that we wanted. To reiterate, this
document outlines all of the steps taken to complete the angr r100 ctf.
