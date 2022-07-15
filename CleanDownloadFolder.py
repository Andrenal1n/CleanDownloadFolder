###
# IMPORTS
###
import os
import shutil
from extensions import *
from paths import *

###
# DIRECT TO DOWNLOADS FOLDER
###
os.chdir("C:/Users/andre/Downloads")
download_files = os.listdir()
print(download_files)

###
# FUNCTION - CLEAN DOWNLOADS
###
def clean():
    for files in download_files:
        if files.endswith(pic_extensions):
            path = path_pictures
            pof = os.path.join(os.getcwd(),files)
            shutil.copy(pof, path)
        elif files.endswith(doc_extensions):
            path = path_documents
            pof = os.path.join(os.getcwd(), files)
            shutil.copy(pof, path) 
        elif files.endswith(exe_extensions):
            path = path_executives
            pof = os.path.join(os.getcwd(), files)
            shutil.copy(pof, path)
        elif files.endswith(cad_extensions):
            path = path_cad
            pof = os.path.join(os.getcwd(), files)
            shutil.copy(pof, path)
        else:
            path = path_base 
            pof = os.path.join(os.getcwd(), files)
            shutil.copy(pof, path) 
        os.remove(files)

###
# Execute
###
clean()


