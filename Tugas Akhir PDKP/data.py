from ctypes import resize
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import *
from PIL import ImageTk, Image
import os

class Data:
    global fileList
    fileList = os.listdir()
    global datalist
    def listData():
        
        datalist = ""
        for name in fileList:
            if name == ".vscode":
                continue
            elif name == "Cpp":
                continue
            elif name == "Java":
                continue
            elif name == "Python":
                continue
            elif name == "Tugas Akhir PDKP":
                continue
            
            datalist += name + "\n"

        return (datalist)

        
