#Babypwn Challenge

#Synopsis
* babypwn.c is the source file for the babypwn program; it shows what the program is
attempting to do and it allows us to identify some of the vulnerabilities that we see.

* babypwn prompts the user for a name as input. The program then takes that name and
compares it to a value 0x41414141 ("AAAA"). If the names match up, then the user will 
receive a flag, indicating their success.

* A vulnerability that I picked up on was in the number of bytes. The char array located
in babypwn.c can store a maximum of up to 32 bytes. However, the name that is input by the
user is read in via fgets() and that has a storage capacity of up to 64 bytes. The data that
is written to the char array exceeds the char array in size, which can cause important data 
to be overwritten entirely, and can even cause malicious code to be ran. Since the memory
for the user-controlled data is being mismanaged, attackers can exploit these vulnerabilities to gain unauthorized access, steal sensitive info, or execute code. 

* The input that we're exploiting is the name.check. Since the char array has 32 bytes of storage, if we input as least 32 A's we the stack with carve out memory for those 32 A's, bypass the program, and receive the flag, ensuring our success.

* However, if we put too many A's, we could potentially receive a segmentation fault.
Segmentation faults are errors that occur when a program tries to read, write, or execute 
memory that it shouldn't which can result in a crash.

* We just have to be mindful about the number of A's that we put (at least 32, but not much over that amount), and then we should receive a victory message from flag.txt.

0x00007fffffffdd88  →  0x0041414141414141 ("AAAAAAA"?)
$rbp   : 0x4141414141414141 ("AAAAAAAA"?)
$rsi   : 0x00007fffffffd780  →  "This is the flag, we win!!!\n"
$rdi   : 0x00007fffffffd750  →  0x00007fffffffd780  →  "This is the flag, we win!!!\n"
$rip   : 0x00000000004012c3  →  <main+00aa> ret 
