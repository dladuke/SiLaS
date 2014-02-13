'''
Created on Oct 18, 2013

@author: Dan LaDuke
'''




import cherrypy
import os.path
from tkinter import filedialog
import server
from cherrypy.lib import static
from os import listdir

localDir = os.path.dirname(__file__)
absDir = os.path.join(os.getcwd(), localDir)
fileDir = os.path.join(os.getcwd(), "files")
            
        
    
        
SiLaSconf = os.path.join(os.path.dirname(__file__), 'SiLaS.conf')



if __name__ == '__main__':
    print("Control-c to stop serving")
    file_path_string = filedialog.askopenfilename()
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    cherrypy.quickstart(server.server(), config=SiLaSconf)
else:
    print(__name__)
    print("Testing")
    
