import json
import os
import os.path
from sys  import platform

class Utils:

    @staticmethod
    def getOS():
        if(platform == "linux") or(platform == "linux2"):    
            return "linux"
        elif(platform == "windows") or(platform == "win32"):
            return "windows"
        else:
            return "unknown"
