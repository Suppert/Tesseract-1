import os
from tesseract import Startup
from shutil import copyfile

exists = false
if os.path.isfile("settings.json"):
    exists = true


