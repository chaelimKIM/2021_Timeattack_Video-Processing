import os
import shutil

def create(directory):
    try:
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.mkdir(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)
