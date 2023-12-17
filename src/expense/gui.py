import tkinter as tk
import os
from tkinter import messagebox, ttk
from expense.expence_analizer import ExpenseAnalizer
from expense.helpers import (
    check_price,
    convert_price_int100_string,
    convert_price_string_int100,
)
from tkcalendar import DateEntry
from expense.expence_serializator import ExpenceSerializator
from expense.expanse_controller import ExpanseController
from expense.expense import Expense
from expense.new_window_gui import NewWindowGui


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
            "TLabel", font=("Helvetica", 12), background="#4A4A4A"
        )
        style.configure(
            "TEntry",
            font=("Helvetica", 12),
            fieldbackground="#666666",
        )
        style.configure(
            "TButton", font=("Helvetica", 12), background="#66BB6A"
        )

        self.expense_input_name_label = tk.Label(
            self.ts, width=10, text="Description:"
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
            self.ts,
            width=20,
            foreground="white",
            borderwidth=2,
            state="readonly",
            date_pattern="d/m/yyyy",
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
        self.expense_add_button.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.save_buttom = tk.Button(self.ts, width=6, text="Save", command=self.save)
        self.save_buttom.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        self.expense_delete_button = tk.Button(
            self.ts, width=6, text="Delete", command=self.delete_expense
        )
        self.expense_delete_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")

        self.expense_balance_button = tk.Button(
            self.ts, width=6, text="Balance", command=self.balance
        )
        self.expense_balance_button.grid(row=4, column=1, padx=10, pady=10, sticky="e")

        self.expense_month_button = tk.Button(
            self.ts,
            width=6,
            text="Month",
            command=self.new_window
        )
        self.expense_month_button.grid(row=5, column=1, padx=10, pady=10, sticky="e")

        self.expense_list_box = tk.Listbox(
            self.ts, width=50, height=10
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
            return
        elif len(name) > 25:
            messagebox.showerror("Too much words","Please, describe expense shorter :)")
            return
        try:
            check_price(price)
        except Exception:
            messagebox.showerror("Error", "Error: Wrong price")
            return

        expense = Expense(name, convert_price_string_int100(price), date)
        self.controller.add(expense)
        self.update_expense_list()

    def update_expense_list(self):
        self.expense_list_box.delete(0, tk.END)
        for expense in self.controller.expenses:
            self.expense_list_box.insert(
                tk.END,
                f"Decription --> {expense.name}, date --> {expense.date}, amount --> {expense.price/100}",
            )

    def min_year(self):
        self.minimum_year = 0
        for expense in self.controller.expenses:
            if int(expense.date) > self.minimum_year:
                self.minimum_year = 0
                self.minimum_year += int(expense.date)
        return self.minimum_year

    def load(self):
        if os.path.isfile(self.filename):
            self.controller.expenses = self.serializator.deserializate()
            self.update_expense_list()

    def save(self):
        self.serializator.serializate(self.controller.expenses)

    def balance(self):
        balance = self.analyzer.get_balance(self.controller.expenses)
        messagebox.showinfo("Balance", f"Your Balance is {balance/100}")

    def new_window(self):
        new_window: NewWindowGui = NewWindowGui(self.controller.expenses)
