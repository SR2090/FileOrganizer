import os
from os import mkdir
from os import path
import shutil
# THE PROGRAM HAS PROBLEMS DO NOT USE IT

# Gets the current working directory
dirPath = os.getcwd()
# dirFiles = open('dirTxt.txt','w')
# lists all files in the current working directory
ImageFile = ('.jpg','.jpeg','.png')
TextFiles = ('.txt')
PdfFiles = ('.pdf')
Notebooks = ('.ipynb')
Shortcuts = ('.lnk')

def createPdf():
    try:
        os.mkdir("Pdf")
    except FileExistsError:
        print("File already Exists")

def createTxt():
    try:
        mkdir(os.path.join(os.getcwd(),"Txt"))
    except FileExistsError:
        print("File already Exists")
def createImg():
    try:
        os.mkdir("Images")
    except FileExistsError:
        print("File already Exists")

def createMisc():
    try:
        os.mkdir("ShortCuts")
        os.mkdir("Directory")
        os.mkdir("Misc")
    except FileExistsError:
        print("File already exists")
createMisc()
createImg()
createTxt()
createPdf()
for File in os.listdir():

    if path.isdir(File):
        shutil.move(File, "Directory")
    else if os.path.splitext(File)[1] in ImageFile:
        print(File)
        shutil.move(File, "Images")
    else if os.path.splitext(File)[1] in PdfFiles:
        shutil.move(File, "Pdf")
    else if os.path.splitext(File)[1] in TextFiles:
        shutil.move(File, "Images")
    else if os.path.splitext(File)[1] in Shortcuts:
        shutil.move(File, "ShortCuts")
    else:
        shutil.move(File, "Misc")
        
