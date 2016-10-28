#!/usr/bin/env python
# Brian Leschke
# COSC440
# Assignment 2
# This program will import /etc/shadow, its users and hashes,
# and attempt to crack the hash.

import crypt
import hashlib
import os 
import sys
from sys import argv

PASSWD_DICT = 'phpbb.txt'  # path to password dictionary
SHADOW_LOC = '/etc/shadow' # path to shadow file

def main():
	print(" .----------------------------. ")
	print(" | Welcome to Hash Crack!     | ")
	print(" | Brian Leschke '@bleschke'  | ")
	print(" | Version 1.0                | ")
	print(" | September 2016             | ")
	print(" '----------------------------' \n")

	if os.access(SHADOW_LOC, os.F_OK): #Make sure Shadow file exists.
		shadowRead = open(SHADOW_LOC, mode='r')
		print "Shadow Location: ", SHADOW_LOC
		print("\n Please specify a system user. \n")
		user = raw_input("Specify User Account: ")
		userFound = False
		for line in shadowRead.readlines(): #Make sure user exists
			if (user in line):
				userFound = True
				print "Selected User: ", user
				line = line.strip() #Remove blank space
				line = line.replace("\n","").split(":")
				if line[1] not in ['x','*','!']:
					user = line[0].strip()
					cryptPass = line[1].strip()
					crack_hash(cryptPass, user)
		if (userFound == False): #Alert if user does not exist
			print "User not found!"
			sys.exit()
	else: # Alert if shadow file does not exist
		print "Shadow file does not exist at ", SHADOW_LOC			

def crack_hash(cryptPass, user):
	if os.access(PASSWD_DICT, os.F_OK): #Make sure password dictionary file exists
		print "\nPassword Dictionary: ", PASSWD_DICT
		passDict = open(PASSWD_DICT, 'r')
		ctype = cryptPass.split("$")[1]
		if ctype == '1':
			print "Hash type: MD5 \n"
		elif ctype == '2a':
			print "Hash type: Blowfish\n "
		elif ctype == '5':
			print "Hash type: SHA-256 \n"
		elif ctype == '6':
			print "Hash type: SHA-512 \n"
		else:
			print "Unable to determine Hashing Algorithm \n"
			
		passFound = False
		salt = cryptPass.split("$")[2]
		insalt = "$" + ctype + "$" + salt + "$"
		print "\n Cracking password for: ", user
		for word in passDict.readlines():
			word.strip()
			word.strip('\n')
			cWord = crypt.crypt(word, insalt)
			if (cWord == cryptPass):
				passFound == True
				print "\nUsername", user
				print "Password", word
				sys.exit()
		if (passFound == False):
			print "Password not in dictionary file", PASSWD_DICT	
	else:
		print "Password Dictionary does not exist!"
		
if __name__ == '__main__':
	main()			
