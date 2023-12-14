import tkinter as tk
from tkinter import messagebox, ttk
import calendar
from expense.expence_analizer import ExpenseAnalizer
from expense.expanse_controller import ExpanseController
from expense.expense import Expense


class NewWindowGui:
    def __init__(self, expenses: list[Expense]) -> None:
        self.analizer: ExpenseAnalizer = ExpenseAnalizer()
        self.controler: ExpanseController = ExpanseController()
        self.controler.expenses = expenses
        self.window = tk.Toplevel()
        self.window.title("Bob")
        self.window.geometry("800x600")
        self.months = list(calendar.month_name[1:])
        self.years = [str(year) for year in range(2000, 2031)]
        self.expense_list_box_two = tk.Listbox(
            self.window, width=50, height=10, foreground="white"
        )
        self.expense_list_box_two.grid(
            row=0, column=3, rowspan=5, padx=10, pady=10, sticky="nsew"
        )
        self.view_balance = tk.Button(
            self.window, text="view balance", command=self.show_calendar
        )
        self.view_balance.grid(row=0, column=0, padx=10, pady=10)

        self.view_balance = tk.Button(self.window, text="Button2")
        self.view_balance.grid(row=0, column=1, padx=10, pady=10)

        self.month_label = ttk.Label(self.window, text="Month:")
        self.month_label.grid(row=1, column=0, pady=10, padx=10, sticky="E")

        self.month_combobox = ttk.Combobox(self.window, values=self.months)
        self.month_combobox.grid(row=1, column=1, padx=10, pady=5)

        self.year_label = ttk.Label(self.window, text="Year:")
        self.year_label.grid(row=2, column=0, pady=10, padx=10, sticky="E")

        self.year_combobox = ttk.Combobox(self.window, values=self.years)
        self.year_combobox.grid(row=2, column=1, padx=10, pady=5)

        self.calendar_label = ttk.Label(self.window, text="")
        self.calendar_label.grid(row=3, column=1, pady=10, padx=10)

    def show_calendar(self):
        self.selected_month = self.month_combobox.get()
        self.selected_year = self.year_combobox.get()
        self.year_number = int(self.selected_year[2:])
        self.month_number = list(calendar.month_name).index(self.selected_month)
        print(self.year_number, self.month_number)
        # self.cal_text = calendar.month(int(self.selected_year), self.year_number)
        self.list_month = self.analizer.get_month(
            self.controler.expenses, self.month_number, int(self.year_number)
        )
        balance_month = self.analizer.get_balance(self.list_month)
        self.calendar_label.config(text=balance_month)
        for expense in self.list_month:
            self.expense_list_box_two.insert(
                tk.END, f"{expense.date},{expense.price},{expense.name}"
            )
