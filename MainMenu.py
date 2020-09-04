import os, string
import tkinter as tk
from tkinter import ttk
import FileFinderApp as ffa

class mainMenu_tk(tk.Tk):
    def __init__(self,parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        #Create the Drive label and dropdown line
        driveLabel = tk.Label(self, text="Drive:").grid(row=0)
        available_drives = ['%s:/' % d for d in string.ascii_uppercase if os.path.exists('%s:/' % d)]
        driveDropdown = ttk.Combobox(self, values = available_drives)
        driveDropdown.grid(row=0, column=1)
        driveDropdown.current(0)

        #Create the Extension label and dropdown line
        extensionLabel = tk.Label(self, text="Extension:").grid(row=1)
        extensionDropdown = ttk.Combobox(self, values = (".pdf", ".txt"))
        extensionDropdown.grid(row=1,column=1)
        extensionDropdown.current(0)

        #Continue Button
        continue_button = tk.Button(self, text = "Continue",
                                    command = lambda: self.continueCmd(driveDropdown.get(),
                                                                       extensionDropdown.get()))
        continue_button.grid(row = 3)

        #Close button
        close_button = tk.Button(self, text = "Close", command = self.closeCmd)
        close_button.grid(row = 3, column = 1, columnspan = 2)

    def continueCmd(self, drive, extension):
        self.destroy()
        ffa.FileFinderMenu(drive, extension)

    def closeCmd(self):
        self.destroy()

    
if __name__ == "__main__":
    app = mainMenu_tk(None)
    app.title("Main Menu")
    app.mainloop()
