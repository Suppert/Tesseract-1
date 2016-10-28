import os
from tesseract import Startup
from shutil import copyfile
from tesseract import Server

exists = False
if os.path.isfile("settings.json":
    exists = True
if exists:
    Startup.start(True)

else:
    print("Welcome to the Tesseract Install Wizard!")
    print("Before starting your new server you must accept the license\n Tesseract is licensed under the GNU v2 License")
    print("You can view the license inside the LICENSE file")
    license = raw_input("Do you accept the license? [Y/n]")
    while license
        if (license == "y") or (license == "yes"):
            accept = True
        elif (license == "n") or (license == "no"):
            accept = False
     if accept == False:
         print("You must accept the License to continue with the Tesseract setup")
         exit(1)
     else:
        name = raw_input("Please select a name for your Tesseract server")
        Server.setName(name)
        port = raw_input("Please select the port you would like your Tesseract server to run on")
        Server.setPort(port)
        print("Creating directorys...")
        if not os.path.exists('worlds'):
	        os.makedirs('worlds')
	    if not os.path.exists('plugins'):
	        os.makedirs('plugins')
	    if not os.path.exists('crashes'):
	        os.makedirs('crashlog')
        if not os.path.exists('players'):
	        os.makedirs('players')
        print 'Setup complete!'
        
                  
    
                        


