# tesseract.py
#!/usr/bin/env python
from pyraklib.server import PyRakLibServer
from pyraklib.server import ServerHandler
import sys
import os
import json
import os.path
from tesseract.resources import Config

# PART OF THIS STARTUP TAKEN FROM THE SPIFFY PROJECT
if sys.version_info<(3,0,0):
  sys.stderr.write("You must use Python <= 3.5")
  exit(1)
  
config = config.handle_config()
server = PyRakLibServer(config['port'])
serverInstance = Handler()
handler = ServerHandler(server, serverInstance)
handler.sendOption("name", "MCPE;" + config['name'] + ";82 82;0.15.4;0;20")
print("starting server on *:" + str(config['port']))
