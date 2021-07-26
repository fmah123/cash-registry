import tkinter as tk
from tkinter import *
from tkinter import filedialog
#from importer import ImportCSV --> need to fix import

class import_GUI(tk.Frame):
   def __init__(self, parent, *args, **kwargs): 
      tk.Frame.__init__(self)   
      self.parent = parent
      self.pack(fill=tk.BOTH, expand=1)
      self.BuildWidgets()
      
   def GetCSVFile(self): 
      self.filename = filedialog.askopenfilename(title="Select File", filetypes=(("CSV Files", "*.csv"),))
      self.file_label.config(text = str(self.filename)) 
      self.file_name = self.filename
     
   def ImportCSVFile(self):
      print("imported csv file")
     # lst = self.file_name.split("/")
     # importer = ImportCSV(self)
     # importer.importCSV(lst[len(lst) - 1])
      # --> need to fix function
      
   def BuildWidgets(self):
      self.frame1 = tk.LabelFrame(self, padx=5, pady=5)
      self.frame2 = tk.Frame(self)
           
      #Label Object
      self.file_label = tk.Label(self.frame1)
      self.file_label['text'] = "Import csv file"
      self.file_label.grid(column=0, row=0, padx=5, pady=5)
      
      #Buttons Objects below 
      
      self.select_file = tk.Button(self.frame2, justify = tk.CENTER, command=self.GetCSVFile)
      self.select_file["text"] = "Select File"
      self.select_file.grid(column=0, row=0, padx=10)
      
      self.import_button = tk.Button(self.frame2, justify=tk.RIGHT, command=self.ImportCSVFile)
      self.import_button["text"] = "Import File"
      self.import_button.grid(column=1, row=0, padx=10)
      
      self.frame1.pack(padx=10, pady=20)
      self.frame2.pack(padx=10, pady=10)
     
      
    

