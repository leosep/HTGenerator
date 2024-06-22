# @file views.py
# @author Leandro Sepulveda, www.leandrosepulveda.com
# @version 1.0
# ht generator! is free software.

#imports the generator.py file
from generators import *
#System Libs
import os

#Header
def printheader():
	print ('*****************************************')
	print ('*              ht generator             *')
	print ('*     version 1.0.0 August 15, 2011     *')
	print ('*        author Leandro Sepulveda       *')
	print ('*        www.leandrosepulveda.com       *')
	print ('*****************************************')
	return

#Main Menu
def printmainmenu():
	print ('\n')
	print ('Please type the number of the option and press ENTER:\n')
	print ('1. Htpasswd Generator')
	print ('2. Htaccess Authentication')
	print ('3. Hotlink protection of images')
	print ('4. Block IPs with .htaccess')
	print ('5. Block hitbots with .htaccess')
	print ('6. Exit')
	print ('\n')

	#Ask for options
	option = input('Option Number:')
	
	if option=="1":
		option1()
	elif option=="2":
		option2()
	elif option=="3":
		option3()
	elif option=="4":
		option4()
	elif option=="5":
		option5()
	elif option=="6":
		print ("See you!")
	else:
		printmainmenu()		

#Htpasswd Generator inputs
def option1():

	if os.name == "posix":
		print ('\n')
		print ('** Htpasswd Generator **')
		username = input('Type Username:')
		password = input('Type Password:')
		location = input('Type Folder Location to Generate the File(Default: generated\\):')
		generate_option1(username, password, location)
	else:
		print ("The Htpasswd Generator is only supported on Unix/Linux/MacOS/BSD/etc")
		printmainmenu()	
		

#Htaccess Authentication inputs
def option2():
    print ('\n')
    print ('** Htaccess Authentication **')
    authname = input('Type Auth Name:')
    filelocation = input('Type .htpasswd File Location:')
    location = input('Type Folder Location to Generate the File(Default: generated\\):')
    generate_option2(authname, filelocation, location)

#Hotlink protection of images inputs    
def option3():
    print ('\n')
    print ('** Hotlink protection of images **')
    domains = input('Type Allowed Domains(Separated by commas. No www.):')
    allowreferers = input('Allow Blank Referers(y/n):')
    files = input('Files To Protect(Separated by commas. Default: jpg,jpeg,png,gif):')
    location = input('Type Folder Location to Generate the File(Default: generated\\):')
    generate_option3(domains, allowreferers, files, location)

#Block IPs with .htaccess inputs
def option4():
    print ('\n')
    print ('** Block IPs with .htaccess **')
    ipadds = input('Type Blocked IPs(Separated by commas.):')
    location = input('Type Folder Location to Generate the File(Default: generated\\):')
    generate_option4(ipadds, location)

#Block hitbots with .htaccess inputs
def option5():
    print ('\n')
    print ('** Block hitbots with .htaccess **')
    domains = input('Type Blocked Domains(Separated by commas. No www.):')
    rdurl = input('Redirection URL(Leave blank to just block hits.):')
    location = input('Type Folder Location to Generate the File(Default: generated\\):')
    generate_option5(domains, rdurl, location)
    
    