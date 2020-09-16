#This program is the main menu of the file finder app
import os, string
import tkinter as tk
import FileFinderApp as ffa
from tkinter import ttk

class mainMenu_tk(tk.Tk):
    def __init__(self,parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        #Create a title label
        titleLabel = tk.Label(self, text = "Please Specify Drive Letter and Extension").grid(columnspan = 2)
        
        #Create t6he Drive label and dropdown line
        driveLabel = tk.Label(self, text="Drive:").grid(row=1)
        available_drives = ['%s:\\' % d for d in string.ascii_uppercase if os.path.exists('%s:\\' % d)]
        driveDropdown = ttk.Combobox(self, values = available_drives)
        driveDropdown.grid(row=1, column=1)
        driveDropdown.current(0)

        #Create the Extension label and dropdown line
        extensionLabel = tk.Label(self, text="Extension:").grid(row=2)
        extensionDropdown = ttk.Combobox(self, values = (".pdf", ".txt"))
        extensionDropdown.grid(row=2,column=1)
        extensionDropdown.current(0)

        #Continue Button
        continue_button = tk.Button(self, text = "Continue",
                                    command = lambda: self.continueCmd(driveDropdown.get(),
                                                                       extensionDropdown.get()))
        continue_button.grid(row = 3)
        self.bind('<Return>',
                  lambda event, drive=driveDropdown.get(), extension = extensionDropdown.get():
                      self.continueCmd(drive, extension))

        #Close button
        close_button = tk.Button(self, text = "Close", command = self.closeCmd)
        close_button.grid(row = 3, column = 1, columnspan = 2)

    def continueCmd(self, drive, extension):
        self.destroy()
        ffa.FileFinderApp(drive, extension)

    def closeCmd(self):
        self.destroy()

    
if __name__ == "__main__":
    app = mainMenu_tk(None)
    app.title("Main Menu")
    app.mainloop()
