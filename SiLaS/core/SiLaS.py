'''
Created on Oct 18, 2013

@author: Dan LaDuke
'''




import cherrypy
import os.path
# from core.server import server
from cherrypy.lib import static
from os import listdir

localDir = os.path.dirname(__file__)
absDir = os.path.join(os.getcwd(), localDir)
fileDir = os.path.join(os.getcwd(), "files")

class server:


    def index(self):
        return "".join(["<html><body>", "<h2>Downloads</h2>", self._createHTML(), "<a href='listFiles'>List filesefs</a>", "</body></html>"])
    

            

    def download(self, fileName):
        path = os.path.join(absDir, "files/" + fileName)
        return static.serve_file(path, "application/x-download",
                                 "attachment", os.path.basename(path))
        
    def listFiles(self):
        from os.path import isfile, join
        onlyfiles = [ f for f in listdir(fileDir) if isfile(join(fileDir, f)) ]
        return (onlyfiles)
    
    def _createHTML(self):
        retVal = ""
        for x in self.listFiles():
            retVal = retVal + "<a href='download?fileName=" + x + "'>" + x + "</a><br>"
            return retVal
            
    def stopServer(self):
        cherrypy.engine.exit()
        return ""
        
            
            
        
    stopServer.exposed = True
    listFiles.exposed = True
    download.exposed = True
    index.exposed = True
        
SiLaSconf = os.path.join(os.path.dirname(__file__), 'SiLaS.conf')



if __name__ == '__main__':
    print("Control-c to stop serving")
    
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    cherrypy.quickstart(server(), config=SiLaSconf)
else:
    print(__name__)
    print("Testing")
    
