###############################################################################
# Program: authorplea
# Type: Python 3 Script
# Author: Steven J. Clipman
# Description: This program prefixes all .docx files in the working directory
# with the last name of the user who authored it.
# License: GPL-3

# Usage: Place all .docx files you wish to rename in a directory.
# cd to that directory and excute the python script
# Example: > cd ~/Desktop/Rename_these_files
#          > python3 ~/scripts/authorplea.py
###############################################################################


import zipfile, lxml.etree
import os

def getFiles(path):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)
        break
    return(files)

def getAuthor(filename):
    zf = zipfile.ZipFile(filename)
    doc = lxml.etree.fromstring(zf.read('docProps/core.xml'))
    ns={'dc': 'http://purl.org/dc/elements/1.1/'}
    creator = doc.xpath('//dc:creator', namespaces=ns)[0].text
    return(creator)

def main():
    files = getFiles(os.getcwd())
    for file in files:
        if file[-5:] == '.docx':
            author = getAuthor(file).split()[1]
            rename = author+'_'+file
            os.rename(file,rename)
    print("Files in",os.getcwd(),"have been renamed.") 
main()