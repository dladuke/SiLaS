'''
Created on Oct 18, 2013

@author: Dan LaDuke
'''




import cherrypy
import os.path
import sys
import argparse
from tkinter import filedialog
import server
from cherrypy.lib import static
from os import listdir

localDir = os.path.dirname(__file__)
absDir = os.path.join(os.getcwd(), localDir)
fileDir = os.path.join(os.getcwd(), "files")
            
        
    
        
SiLaSconf = os.path.join(os.path.dirname(__file__), 'SiLaS.conf')

# Checks to make sure the filepath is correct and SiLaS can access it
# TODO
def validPath(filePath):
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

# Tkinter loop for graphical mode
# TODO
def startGUI():
	print("GUI not yet implemented")
	#file_path_string = filedialog.askopenfilename()




if __name__ == '__main__':

    thisServer = server.server()
    if (len(sys.argv)>1):
    	handleArgs()
    else:
    	startGUI()
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    #args.list
    print("Control-c to stop serving")
    cherrypy.quickstart(thisServer, config=SiLaSconf)
else:
    print(__name__)
    print("Testing")
    


