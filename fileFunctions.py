import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def findFile(PDF):
    paths = ""
    
    for root, dirs, files in os.walk(r"C:\\"):
        for name in files:
            if name == PDF:
                paths = os.path.abspath(os.path.join(root, name))
                break
            
        if paths not in [""]:
            break
        
    return paths

def submit(file, path_var):
    #file = path_var.get()
    
    ##File Extension##
    extension = ".txt"
    ##################

    #creating the file name with the extension
    file = file + extension

    path = ""
    if file not in [".txt"]:
        path = findFile(file)
        if path not in [".txt"] and os.path.exists(path):
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

###create a window and set the size
##window = tk.Tk()
##window.geometry("200x100")
##
###declare strings
##path_var = tk.StringVar()
##
###createing the title and entry box
##barcodeLine = tk.Label(window, text = "Enter WO Number:")
##entry = tk.Entry(window, textvariable = path_var)
##barcodeLine.pack()
##entry.pack()
##
###creating both buttons (open and cancel)
##open_button = tk.Button(window,text = "Open", command = submit)
##open_button.pack(side=tk.LEFT, padx=(50,0))
##
##cancel_button = tk.Button(window, text = "Cancel", command = cancel)
##cancel_button.pack(side=tk.RIGHT, padx=(0,50))
##
##window.mainloop()

