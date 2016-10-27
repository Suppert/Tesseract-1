# tesseract.py
#!/usr/bin/env python
from pyraklib.server import PyRakLibServer
from pyraklib.server import ServerHandler
import sys
import os
from tesseract.resources import Config

# STARTUP TAKEN FROM THE SPIFFY PROJECT
config = config.handle_config()
server = PyRakLibServer(config['port'])
serverInstance = Handler()
handler = ServerHandler(server, serverInstance)
handler.sendOption("name", "MCPE;" + config['name'] + ";82 82;0.15.4;0;20")
print("starting server on *:" + str(config['port']))
