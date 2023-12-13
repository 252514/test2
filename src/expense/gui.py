import tkinter as tk
import os
from datetime import datetime
from tkinter import messagebox, ttk
from expense.expence_analizer import ExpenseAnalizer
from tkcalendar import DateEntry
from expense.expence_serializator import ExpenceSerializator
from expense.expanse_controller import ExpanseController
from expense.expense import Expense

FILENAME = ".expenses.txt"


class Gui:
    def __init__(self, title: str, resolution: str) -> None:
        self.controller: ExpanseController = ExpanseController()
        self.serializator: ExpenceSerializator = ExpenceSerializator(FILENAME)
        self.analyzer: ExpenseAnalizer = ExpenseAnalizer()
        self.filename = FILENAME
        self.ts = tk.Tk()
        self.ts.title(title)
        self.ts.geometry(resolution)
        self.ts.configure(background="#4A4A4A")

        style = ttk.Style()
        style.configure(
            "TLabel", font=("Helvetica", 12), foreground="white", background="#4A4A4A"
        )
        style.configure(
            "TEntry",
            font=("Helvetica", 12),
            fieldbackground="#666666",
            foreground="white",
        )
        style.configure(
            "TButton", font=("Helvetica", 12), background="#66BB6A", foreground="white"
        )

        self.expense_input_name_label = tk.Label(
            self.ts, width=10, foreground="white", text="Description:"
        )
        self.expense_input_name_label.grid(
            row=0, column=0, padx=10, pady=10, sticky="w"
        )

        self.expense_input_name_entry = tk.Entry(self.ts)
        self.expense_input_name_entry.grid(
            row=0, column=1, padx=10, pady=10, sticky="w"
        )

        self.expense_input_date_label = tk.Label(self.ts, width=10, text="Date:")
        self.expense_input_date_label.grid(
            row=1, column=0, padx=10, pady=10, sticky="w"
        )

        self.expense_input_date_entry = DateEntry(
            self.ts, width=20, foreground="white", borderwidth=2
        )
        self.expense_input_date_entry.grid(
            row=1, column=1, padx=10, pady=10, sticky="w"
        )

        self.expense_input_price_label = tk.Label(self.ts, width=10, text="Income:")
        self.expense_input_price_label.grid(
            row=2, column=0, padx=10, pady=10, sticky="w"
        )

        self.expense_input_price_entry = tk.Entry(self.ts)
        self.expense_input_price_entry.grid(
            row=2, column=1, padx=10, pady=10, sticky="w"
        )

        self.expense_add_button = tk.Button(
            self.ts, width=6, text="Add", command=self.add_expense
        )
        self.save_buttom = tk.Button(self.ts, width=6, text="Save", command=self.save)

        self.save_buttom.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        self.expense_add_button.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.expense_delete_button = tk.Button(
            self.ts, width=6, text="Delete", command=self.delete_expense
        )
        self.expense_delete_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")

        self.expense_delete_button = tk.Button(
            self.ts, width=6, text="Balance", command=self.balance
        )
        self.expense_delete_button.grid(row=4, column=1, padx=10, pady=10, sticky="e")
        self.expense_list_box = tk.Listbox(
            self.ts, width=50, height=10, foreground="white"
        )
        self.expense_list_box.grid(
            row=0, column=2, rowspan=5, padx=10, pady=10, sticky="nsew"
        )

        self.load()

    def run(self):
        self.ts.mainloop()

    def delete_expense(self):
        try:
            index = self.expense_list_box.curselection()[0]
            self.controller.delete(index)
            self.update_expense_list()
        except IndexError:
            messagebox.showerror("Error", "Please select an expense to delete.")

    def add_expense(self):
        name = self.expense_input_name_entry.get()
        price = self.expense_input_price_entry.get()
        date = self.expense_input_date_entry.get()

        if not name or not price or not date:
            messagebox.showerror(
                "Empty", "Error: Descripton, date or expense cannot be empty."
            )
        elif price[0] == "-":
            if not price[1:].isdigit():
                messagebox.showerror("Number", "Error: You should input a number.")
        elif not name or not price or not date:
            messagebox.showerror(
                "Empty", "Error: Descripton, date or expense cannot be empty."
            )
            return
        expense = Expense(name, int(price), date)
        self.controller.add(expense)
        self.update_expense_list()

    def update_expense_list(self):
        self.expense_list_box.delete(0, tk.END)
        for expense in self.controller.expenses:
            self.expense_list_box.insert(
                tk.END, f"{expense.name} {expense.price} {expense.date}"
            )

    def load(self):
        if os.path.isfile(self.filename):
            self.controller.expenses = self.serializator.deserializate()
            self.update_expense_list()
        # load from file -> list
        # self.controller.expenes + list

    def save(self):
        self.serializator.serializate(self.controller.expenses)

    def balance(self):
        balance = self.analyzer.get_balance(self.controller.expenses)
        messagebox.showinfo("Balance", f"Your Balance is {balance}")


# check how extend fucntion work
