#This file contains the functions for the file finder app 
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def findFile(PDF, drive):
    paths = ""
    
    for root, dirs, files in os.walk(drive):
        for name in files:
            if name == PDF:
                paths = os.path.abspath(os.path.join(root, name))
                break
            
        if paths not in [""]:
            break
        
    return paths

def submit(file, path_var,drive, extension):
    #creating the file name with the extension
    file = file + extension

    path = ""
    if file not in [extension]:
        path = findFile(file, drive)
        if path not in [extension] and os.path.exists(path):
            os.startfile(path)
            #success
            tk.messagebox.showinfo('Success!', message='File Opened Successfully!')
        else:
            #failure
            tk.messagebox.showerror(message = 'File Name Wrong or Does Not Exist')
    else:
        #if empty
        tk.messagebox.showerror(message = 'File Name was empty')


    #clear the box
    path_var.set("")

def cancel(file, window, path_var):
    #file = path_var.get()

    if file in [""]:
        window.destroy()
    else:
        path_var.set("")


