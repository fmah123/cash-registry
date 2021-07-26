import tkinter as tk
from entryAdder import add_entry

class add_GUI(tk.Frame):
    def __init__(self, parent, child, *args, **kwargs):
        super().__init__(child)
        self.parent = parent
        self.child = child
        self.pack(fill=tk.NONE, expand=1)
        self.child.title("Add Cash Entry")
        self.child.geometry("350x400")
        self.BuildWidgets()
        self.date = ""
        self.cash_amount = ""
        self.card_amount = ""
        self.expense_amount = ""
    
    def BuildWidgets(self):
        self.frame = tk.Frame(self)

        self.okButton = tk.Button(
            self.frame, 
            text = "Ok",
            command = self.addEntry,
            padx = 10
        )
        
        self.cancelButton = tk.Button(
            self.frame,
            text = "Cancel"
        )

        self.DateLabel = tk.Label(
            self.frame,
            text = "Date:"
        )

        self.CashLabel = tk.Label(
            self.frame,
            text = "Cash Amount (£):"
        )

        self.CardLabel = tk.Label(
            self.frame,
            text = "Card Amount (£):"
        )

        self.ExpenseLabel = tk.Label(
            self.frame,
            text = "Expense Total:"
        )

        self.dateEntry = tk.Entry(self.frame)
        self.cashEntry = tk.Entry(self.frame)
        self.cardEntry = tk.Entry(self.frame)
        self.expenseEntry = tk.Entry(self.frame)

        self.CashLabel.grid(column = 0, row = 1, pady = 10)
        self.ExpenseLabel.grid(column = 0, row = 3, pady = 10)
        self.CardLabel.grid(column = 0, row = 2, pady = 10)
        self.DateLabel.grid(column = 0, row = 0, pady = 10)
        self.okButton.grid(column = 0, row = 4, pady = 10)
        self.cancelButton.grid(column = 1, row = 4)
        self.dateEntry.grid(column=1, row=0)
        self.cashEntry.grid(column=1, row=1, padx=5)
        self.cardEntry.grid(column=1, row=2, padx=5)
        self.expenseEntry.grid(column=1, row=3)
        self.frame.pack(fill = tk.BOTH, expand = 1)
        
    def addEntry(self):
        self.date = self.dateEntry.get()
        self.cash_amount = self.cashEntry.get()
        self.card_amount = self.cardEntry.get()
        self.expense_amount = self.expenseEntry.get()
        add_entry(
            self.date,
            self.cash_amount,
            self.card_amount,
            self.expense_amount
        )
        self.child.destroy()    