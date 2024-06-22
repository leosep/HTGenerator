# @file init.py
# @author Leandro Sepulveda, www.leandrosepulveda.com
# @version 1.0
# ht generator! is free software.

#Libs
import os

#Clean the screen
def cleanscreen():
	if os.name == "posix":
		# Unix/Linux/MacOS/BSD/etc
		os.system('clear')
	if os.name in ("nt", "dos", "ce"):
		#DOS/Windows
		os.system('CLS')
	return



