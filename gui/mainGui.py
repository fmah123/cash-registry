import tkinter as tk
from tkinter.ttk import *
from importGui import import_GUI
from addGui import add_GUI 
from entryAdder import check_db

class Main_GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("500x300+500+50")
        self.pack(fill=tk.BOTH, expand=0, ipadx=50)
        self.master.title("Cash Registry")
        #Added the tab control for easier navigation.
        self.tab = tk.ttk.Notebook(self.master, pad=15)
        self.tab.pack(expand=1, fill=tk.BOTH)
        self.BuildWidgets()

    def addEntry(self):
        self.addEntryWindow = tk.Toplevel(self.master)
        self.addClass = add_GUI(self.master, self.addEntryWindow)    
       
    
    def editEntry(self):
        print("Edit Data")

    
    def showData(self):
        check_db()
                    

    def BuildWidgets(self):
        self.frame1 =tk.Frame(self.tab)

        #adding import window frame
        self.import_frame = import_GUI(self.tab)

      
        self.add_button = tk.Button(
            self.frame1, 
            text = "Add Cash Entry",
            command = self.addEntry,
            padx = 5,
            pady = 10,
            activeforeground = "green",
            activebackground = "skyblue"
        )

        self.edit_button = tk.Button(
            self.frame1,
            text = "Edit Cash Entry",
            command = self.editEntry,
            padx = 5,
            pady = 10,  
            activeforeground = "green",
            activebackground = "skyblue"            
        )

        

        self.show_data_button = tk.Button(
            self.frame1,
            text = "Show Registry Data",
            command = self.showData,
            padx = 5,
            pady = 10,
            activeforeground = "green",
            activebackground = "skyblue"
        )


        self.add_button.pack(padx=10, pady=5)
        self.edit_button.pack(padx=10, pady=5)
        self.show_data_button.pack(padx=10, pady=5)

        self.frame1.pack(fill=tk.BOTH, expand=1, padx = 150, pady = 150)   
        self.tab.add(self.frame1, text="Main")
        self.tab.add(self.import_frame, text=" Import CSV")

if __name__ == "__main__":
    app = tk.Tk()
    Main_GUI(app)
    app.mainloop()
