# Linux Password Cracker &quot;Hash Crack&quot;

Brian Leschke 2016

## **Overview**

This python program can be used to detect hashing algorithms of specified users in the /etc/shadow file and attempt to crack those hashes. The attack vector is a dictionary attack and uses the dictionary file &quot;phpbb.txt&quot; which is found at [https://wiki.skullsecurity.org/Passwords](https://wiki.skullsecurity.org/Passwords)

### **Prerequisities**

You will need:

1. Any modern version/flavor of Linux/Unix
2. System privileges to access  /etc/shadow
3. Python 2.7 (unknown compatibility with higher versions)

### **Usage**

In order to use this code you will have to download and unpackage this repository listed below:

        https://github.com/Bleschke/LinuxPasswordCracker.git

All files need to placed in the same file location/folder in order for the program to run (unless you specify the file location).

To run the program, type the following in a terminal window under the directory in which the files were placed:

        sudo python assignment2.py

### **Changing dictionary files and shadow locations**

To change the location of the shadow file, you will need to edit the &quot;assignment2.py&quot; file with a text editor of your choosing. You will need to edit these two variables located towards the top of the file to match your dictionary file and shadow file locations.

        PASSWD_DICT = 'phpbb.txt';   # path to password dictionary

        SHADOW_LOC = '/etc/shadow';  # path to shadow file

