# VM-Back-Up
Example of Windows compiled python code, used for backing up my VM's

Test of a .py to .exe complier

Function 
1. Read VM directory every 4 hours 
2. Compare VM files from one directory to another to check for a change
3. If there is a change 
   1. Confirm VM is in a off or paused state
   2. Copy VM files to a new directory marked with date and time
   3. Show on screen progress
