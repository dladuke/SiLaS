<h1> SiLaS </h1>
Simple Lan Server

Transfering files between different platforms can be a slow process.
You could install and configure SSH on each individual machine and use SCP to transfer...
You could install a FTP server on one machine and FTP clients on dozens or hundreds of other machines...
You could pass around physical media after properly configuring NTFS-3g... 
You could install Dropbox or use Google drive if the files are small...

- No installation: Just download and run.
- Minimal configuration: Select a file and click 'host'.
- No client needed: All machines on the LAN can download the files using only a browser.
- No size restriction: Quickly transfer huge files between machines using just your router.

<h1> Downloading </h1>

Standalone executables are available under the directory 'out/'.
Right click the appropriate version and select 'save as'.


<h1> Building </h1>

To build a new standalone executable you will need:
- Python 2.7: http://www.python.org/downloads/
- PIP: http://pip.readthedocs.org/en/latest/installing.html
- Pyinstaller 2.1: pip install pyinstaller
- Cherrypy: pip install cherrypy

<h1> Coming soon </h1>
- A standalone executable for OSX
- A GUI that doesn't look quite so bad
- Encryption & password protection options

