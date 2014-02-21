'''
Created on Oct 18, 2013

@author: Dan LaDuke
'''




import cherrypy
import os.path
import sys
import argparse
import socket
from Tkinter import *
import tkFileDialog
import server
from cherrypy.lib import static
from os import listdir
import threading


        
    


# Checks to make sure the filepath is correct and SiLaS can access it
# TODO: Add all path/permission checks
def validPath(filePath):
    #TODO
    return True

# Extracts cmd line args and passes filenames to the server
def handleArgs():
    parser = argparse.ArgumentParser(description='Host files for the local network. Connect and download with any supported browser')
    parser.add_argument('-f','--files',action='store',dest='files',nargs='*',help='Fully qualified path(s) to files. eg: /path/to/file/one, /path/to/file/two',required=False)
    #Additional args go here.
    args = parser.parse_args()
    for f in args.files:
        if validPath(f):
            thisServer.addFile(f)
        else:
            print("Arg error")
            # Handle arg error
            # TODO
    startServing()

# Tkinter loop for graphical mode
# TODO 
def startGUI():
    rootWindow = Tk()
    #rootWindow.geometry("600x400")
    rootWindow.title("SiLaS")
    v = StringVar()
    Label(rootWindow, textvariable=v).pack()
    text = Text(rootWindow)
    v.set("Select the files you wish to share using the 'File Select' button. \nWhen you have selected all the files click the 'Host Files' Button.")
    listbox = Listbox(rootWindow)
    listbox.width = 75
    listbox.pack(fill=BOTH, expand=1)
    selectButton = Button(rootWindow, text="File Select", command = lambda: _selectFileGUI(rootWindow,listbox))
    selectButton.pack(side=LEFT, padx=5, pady=5)
    hostButton = Button(rootWindow, text="Host Files", command = lambda: _startServingGUI(hostButton,selectButton,v))
    hostButton.pack(side=LEFT, padx=5, pady=5)
    rootWindow.mainloop()

def _selectFileGUI(root,listbox):
    file_path_string = tkFileDialog.askopenfilename(parent=root,title='Choose a file')
    #print(file_path_string) # Check path
    listbox.insert(1,file_path_string)
    thisServer.addFile(file_path_string)
    return file_path_string
def _exitGUI():
    sys.exit()
def startServing():
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    #args.list
    print("Control-c to stop serving")
    #TODO Add config options to CLI/GUI. So user can change port.
    cherrypy.config.update({'server.socket_host': '0.0.0.0','server.socket_port': 8080, 'server.thread_pool' : 10})
    cherrypy.quickstart(thisServer)

# Launch the server from the GUI
# This method handles threading and avoids networking on the GUI thread
def _startServingGUI(button, button2,v):
    t = threading.Thread(target=startServing)
    t.daemon = True
    t.start()
    button.destroy()
    button2.destroy()
    text = "You are now serving files\n To retrive the files navigate your browser to "+str(getThisIP())+":8080 \nExit this window to stop serving."
    v.set(text)

# returns the IP of the machine running the code
# Assuming the computer is connected to the internet we return the IP of the connected interface
# TODO Pick a better solution
#      Test on all platforms
#      Error handle
def getThisIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("google.com",80))
    ip = s.getsockname()[0]
    s.close()
    return ip



if __name__ == '__main__':

    thisServer = server.server()
    fileCount = 0
    if (len(sys.argv)>1):
    	handleArgs()
    else:
    	startGUI()
else:
    print(__name__)
    print("Testing")
    


