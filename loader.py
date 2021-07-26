import csv 
import os
import sqlite3
import sys

"""
   import.py function is to change csv file data to sql database data. 
"""

class LoadCSV(object):
   def __init__(self):
      self.conn = None
      
   #Creates the database for use.   
   def createDB(self, db_name):
      try:
         conn = sqlite3.connect(db_name)
      except sqlite3.Error as e:
         print(e)      
      return conn
   
   #runs sql statement
   def runSQL(self, con, sql, *args, **kwargs):
       con.cursor().execute(sql, args)
       
   #Transfer data from csv file over to a sqlite database.    
   def csvToDb(self, filename, con, sql, *args, **kwargs):
      with open(filename, newline='') as csv_file:
         try:
            csvReader = csv.reader(csv_file)
            for row in csvReader:
               runSQL(con, sql, tuple(row))
         except csv.Error as e:
             sys.exit("file {}, line {}: {}".format(filename, csvReader.line_num, e))   
   
   #imports csv content to database
   def loadCSV(self, filename):
       self.conn = self.createDB("cash_registry.db")
       cur = self.conn.cursor()
       cur.execute(""" CREATE TABLE IF NOT EXISTS CASH_REGISTRY (
       id INTEGER NOT NULL PRIMARY KEY,date TEXT, cash_amount TEXT, card_amount TEXT, total_expense TEXT); """)
       self.CsvToDb(filename, self.conn, "INSERT INTO CASH_REGISTRY ('date', 'cash_amount', 'card_amount', 'total_expense') VALUES (?, ?, ? ,?);")
       self.conn.commit()        
       self.conn.close()
       
       
        