# OffensiveSec-BinaryWorkshop


## A Basic tutorial in binary analysis/binary exploitation along with working within the Kali Linux Terminal to complete various CTF style tasks.

Our first task involves a function called time. To begin, we imported a file called time from https://github.com/guyinatuxedo/nightmare.git into ghidra and then viewed the source code to understand how random numbers were being generated.
Next, we connected the remote repo to our local repos so we could push our commits to the remote repo. 
Following the setup process, we created a file known as sol.py in a text editor of choice and began working on getting our input to sync into the time challenge crackme on GitHub by copying the time binary into our terminal and utilizing pwntools to help us connect Python code to the command line.
Next, we created a another file called time.py and utilized ctypes in order to utilize C-based functions such as rand() and srand() in Python. After importing code in from StackOverflow, we generated random numbers within time.py.
After getting the separate parts working, we copied and pasted the time.py code into sol.py and synced up the random number in time.py to the random frequency of numbers in sol.py to secure the flag. 
  
   




