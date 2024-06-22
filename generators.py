# @file generators.py
# @author Leandro Sepulveda, www.leandrosepulveda.com
# @version 1.0
# ht generator! is free software.

#system Libs
import os

#Set default file path
if os.name == "posix":
		# Unix/Linux/MacOS/BSD/etc
		dafault_path = "generated/"
if os.name in ("nt", "dos", "ce"):
		#DOS/Windows
		dafault_path = "generated\\"

#Htpasswd Generator Function
def generate_option1(username, password, location):
    
    import crypt
    import sys  

    if location.strip()== "":
        location = dafault_path
        
    # Open a file
    path = location.strip()+"rename.htpasswd"
    fo = open(path, "w")
    fo.write("%s:%s" % (username, crypt.crypt(password, password)))

    # Close opend file
    fo.close()
    print ('Done. Generated in: '+path)
    from views import printmainmenu
    printmainmenu()

    
#Htaccess Authentication Function
def generate_option2(authname, filelocation, location):
   

    if location.strip()== "":
        location = dafault_path

    # Open a file
    path = location+"rename.htaccess"
    fo = open(path, "w")
    htstring = 'AuthType Basic\nAuthName "'+authname+'"\nAuthUserFile '+filelocation+'\nRequire valid-user'
    fo.write(htstring)

    # Close opend file
    fo.close()
    print ('Done. Generated in: '+path)
    from views import printmainmenu
    printmainmenu()


#Hotlink protection of images Function
def generate_option3(domains, allowreferers, files, location):
    

    if location.strip()== "":
        location = dafault_path

    content = "RewriteEngine on\n"

    if allowreferers.lower() == "y":
        content = content+"RewriteCond %{HTTP_REFERER} !^$\n"
   
    domainarr = domains.split( "," )

    for domain in domainarr:        
        content = content+"RewriteCond %{HTTP_REFERER} !^http(s)?://(www\.)?"+domain.strip()+" [NC]\n"

    images = files.strip()

    if files.strip()== "":
        content = content+"RewriteRule \.(jpg|jpeg|png|gif)$ - [NC,F,L]"
    else:
        content = content+"RewriteRule \.("+images.replace(",","|")+")$ - [NC,F,L]" 

    # Open a file
    path = location+"rename.htaccess"
    fo = open(path, "w")
    fo.write(content)

    # Close opend file
    fo.close()
    print ('Done. Generated in: '+path)
    from views import printmainmenu
    printmainmenu()

#Block IPs with .htaccess Function
def generate_option4(ipadds, location):
   

    if location.strip()== "":
        location = dafault_path

    content = "Order Deny,Allow\n"

    iparr = ipadds.split( "," )

    for ipadd in iparr:        
        content = content+"Deny from "+ipadd.strip()+"\n"

    # Open a file
    path = location+"rename.htaccess"
    fo = open(path, "w")
    fo.write(content)

    # Close opend file
    fo.close()
    print ('Done. Generated in: '+path)
    from views import printmainmenu
    printmainmenu()

#Block hitbots with .htaccess Function
def generate_option5(domains, rdurl, location):
   

    if location.strip()== "":
        location = dafault_path

    content = "RewriteEngine on\n"
   
    domainarr = domains.split( "," )
    countarr = len(domainarr)
    counter = 0

    for domain in domainarr:        
        
        content = content+"RewriteCond %{HTTP_REFERER} ^http(s)?://(www\.)?"+domain.strip()
        counter = counter + 1

        if counter < countarr:
            content = content+" [NC,OR]\n"
        elif counter == countarr:
            content = content+" [NC]\n"
 
    if rdurl.strip()== "":
        content = content+"RewriteRule .* - [F,L]"
    else:
        content = content+"RewriteRule .* "+rdurl.strip()+" [R,L]" 

    # Open a file
    path = location+"rename.htaccess"
    fo = open(path, "w")
    fo.write(content)

    # Close opend file
    fo.close()
    print ('Done. Generated in: '+path)
    from views import printmainmenu
    printmainmenu()
