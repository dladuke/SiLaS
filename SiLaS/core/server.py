'''
Created on Oct 18, 2013

@author: Dan LaDuke
'''

import os.path
from cherrypy.lib import static
from os import listdir
from os.path import isfile, join

localDir = os.path.dirname(__file__)
absDir = os.path.join(os.getcwd(), localDir)
fileDir = os.path.join(os.getcwd(), "files")


class server:
    
    fileList = ""

    def index(self):
        return "".join(["<html><body>","<h2>Downloads</h2>",self.fileList,"</body></html>"])
            

    def download(self, fileName):
        #path = os.path.join(absDir, "files/"+fileName) # Files folder
        path = os.path.join("", fileName) # No files folder.
        return static.serve_file(path, "application/x-download", "attachment", os.path.basename(path))
        
    # Obsolete method
    # TODO remove
    def listFiles(self):
        onlyfiles = [ f for f in listdir(fileDir) if isfile(join(fileDir,f)) ]
        return (onlyfiles)

    # Obsolete
    # TODO update
    def _createHTML(self):
        retVal = self.fileList
        for x in self.listFiles():
            retVal = retVal + "<a href='download?fileName=" +x+ "'>"+x+"</a><br>"
        return retVal

    # Terminate server remotely
    # TODO this should be a toggle/option
    def stopServer(self):
        cherrypy.engine.exit()
        return ""

    #Creates a new listing for the file passed
    def addFile(self, filePath):
        self.fileList = self.fileList + "<a href='download?fileName=" +filePath+ "'>"+filePath+"</a><br>"


    #stopServer.exposed = True # Optional
    listFiles.exposed = True
    download.exposed = True
    index.exposed = True