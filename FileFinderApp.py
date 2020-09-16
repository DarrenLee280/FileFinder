#This program is the window for the File Finder app
import os
import tkinter as tk
import fileFunctions as fFunctions
import fileOrganizer

class FileFinderApp(tk.Tk):
    def __init__(self,drive,extension):
        #tk.Tk.__init__(self)
        #self.parent = parent
        self.drive = drive
        self.extension = extension
        self.initialize()

    def initialize(self):
        #create a window and set the size
        window = tk.Tk()
        window.geometry("170x100")

        #declare strings
        path_var = tk.StringVar()

        #createing the title and entry box
        barcodeLine = tk.Label(window, text = "Enter WO Number:")
        entry = tk.Entry(window, textvariable = path_var)
        #barcodeLine.pack()
        barcodeLine.grid(row = 0, column = 2, columnspan = 2, padx = 20,sticky='NSEW')
        #entry.pack()
        entry.grid(row = 1, column = 2, columnspan = 2, padx = 20)

        #creating both buttons (open and cancel)
        open_button = tk.Button(window,text = "Open", command = lambda: fFunctions.submit(path_var.get(),
                                                                                          path_var,
                                                                                          self.drive,
                                                                                          self.extension))
        open_button.grid(row = 3, column = 1, columnspan = 2, padx=20,sticky='NSEW')


        cancel_button = tk.Button(window, text = "Cancel", command = lambda: fFunctions.cancel(path_var.get(),
                                                                                           window, path_var))
        cancel_button.grid(row = 3, column = 3, columnspan = 2, padx = 20,sticky='NSEW')

        #Bind Enter key to open
        #self.bind('<Return>',
                  #lambda event, path = path_var.get(), path2 = path_var, drive = self.drive, extension = self.extention:
                      #fFunctions.submit(path, path2, drive, extension))

        #configure the window 
        window.grid_columnconfigure(0,weight=1)
        window.grid_columnconfigure(1,weight=1)
        window.grid_columnconfigure(2,weight=1)
        window.grid_rowconfigure(0,weight=1)
        window.grid_rowconfigure(1,weight=1)


if __name__== "__main__":
    window = FileFinderMenu(drive, extension)
    window.title("File Finder")
    window.mainloop()

##def FileFinderMenu(drive, extension):
##    #create a window and set the size
##    window = tk.Tk()
##    window.geometry("170x100")
##
##    #declare strings
##    path_var = tk.StringVar()
##
##    #createing the title and entry box
##    barcodeLine = tk.Label(window, text = "Enter WO Number:")
##    entry = tk.Entry(window, textvariable = path_var)
##    #barcodeLine.pack()
##    barcodeLine.grid(row = 0, column = 2, columnspan = 2, padx = 20,sticky='NSEW')
##    #entry.pack()
##    entry.grid(row = 1, column = 2, columnspan = 2, padx = 20)
##
##    #creating both buttons (open and cancel)
##    open_button = tk.Button(window,text = "Open", command = lambda: fFunctions.submit(path_var.get(),
##                                                                                      path_var, drive, extension))
##    open_button.grid(row = 3, column = 1, columnspan = 2, padx=20,sticky='NSEW')
##
##    cancel_button = tk.Button(window, text = "Cancel", command = lambda: fFunctions.cancel(path_var.get(),
##                                                                                           window, path_var))
##    cancel_button.grid(row = 3, column = 3, columnspan = 2, padx = 20,sticky='NSEW')
##
##    window.grid_columnconfigure(0,weight=1)
##    window.grid_columnconfigure(1,weight=1)
##    window.grid_columnconfigure(2,weight=1)
##    window.grid_rowconfigure(0,weight=1)
##    window.grid_rowconfigure(1,weight=1)
##
##    window.title("File Finder")
##    window.mainloop()

