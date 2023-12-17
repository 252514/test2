from datetime import date
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
        self.window.configure(background="#4A4A4A")
        self.years = [str(year) for year in range(1900, 2031)][::-1]

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

        self.scrollbar_horizontal = tk.Scrollbar(self.window, orient="")

        self.scrollbar_vertical = tk.Scrollbar(self.window, orient="vertical")
        self.expense_list_box_two = tk.Listbox(
            self.window,
            width=50,
            height=10,
            yscrollcommand=self.scrollbar_vertical.set,
            xscrollcommand=self.scrollbar_horizontal.set,
        )
        self.expense_list_box_two.grid(
            row=0, column=3, rowspan=5, padx=10, pady=10, sticky="nsew"
        )
        self.scrollbar_vertical.config(command=self.expense_list_box_two.yview)
        self.scrollbar_vertical.grid(row=3, column=3, sticky="ns")

        self.scrollbar_horizontal.config(command=self.expense_list_box_two.xview)
        self.scrollbar_horizontal.grid(row=5, column=3, sticky="ns")

        self.expense_list_box_two.config(yscrollcommand=self.scrollbar_vertical.set)
        self.scrollbar_vertical.config(command=self.expense_list_box_two.yview)

        self.view_balance = tk.Button(
            self.window, text="view balance", command=self.view_month_balance
        )
        self.view_balance.grid(row=3, column=0, padx=10, pady=10)

        self.view_balance = tk.Button(
            self.window, text="view list", command=self.view_month_balance_and_list
        )
        self.view_balance.grid(row=3, column=1, padx=10, pady=10)

        self.month_label = ttk.Label(self.window, text="Month:")
        self.month_label.grid(row=1, column=0, pady=10, padx=10, sticky="E")

        self.month_combobox = ttk.Combobox(
            self.window, values=self.months, state="readonly"
        )
        self.month_combobox.grid(row=1, column=1, padx=10, pady=5)
        self.month_combobox.set(self.months[0])

        self.year_label = ttk.Label(self.window, text="Year:")
        self.year_label.grid(row=2, column=0, pady=10, padx=10, sticky="E")

        self.year_combobox = ttk.Combobox(
            self.window, values=self.years, state="readonly"
        )
        self.year_combobox.grid(row=2, column=1, padx=10, pady=5)
        self.year_combobox.set(self.years[0])

        self.label_balance_month = ttk.Label(self.window, text="Balance of the month: ")
        self.label_balance_month.grid(row=4, column=0, pady=10, padx=10)

        self.balance_of_month = ttk.Label(self.window, text="0,0")
        self.balance_of_month.grid(row=4, column=1, pady=10, padx=10)

        self.label_total_balance_before = ttk.Label(
            self.window, text="Total balance before the month: "
        )
        self.label_total_balance_before.grid(row=5, column=0, pady=10, padx=10)

        self.total_balance_before = ttk.Label(self.window, text="0.0")
        self.total_balance_before.grid(row=5, column=1, pady=10, padx=10)

        self.label_total_balance_before = ttk.Label(
            self.window, text="Total balance after the month: "
        )
        self.label_total_balance_before.grid(row=6, column=0, pady=10, padx=10)

        self.total_balance_after = ttk.Label(self.window, text="0.0")
        self.total_balance_after.grid(row=6, column=1, pady=10, padx=10)

    def get_date(self):
        selected_month = self.month_combobox.get()
        selected_year = self.year_combobox.get()
        year_number = int(selected_year)
        month_number = list(calendar.month_name).index(selected_month)
        return month_number, year_number

    def view_month_balance(self):
        self.show_month_balance_label()
        self.total_balance_before_specific_month()
        self.total_balance_after_month()

    def view_month_balance_and_list(self):
        self.view_month_balance()
        self.show_month_expenses_list()

    def show_month_balance_label(self):
        month, year = self.get_date()
        self.list_month = self.analizer.get_month(self.controler.expenses, month, year)
        balance_month = self.analizer.get_balance(self.list_month)
        balance_month = balance_month / 100
        self.balance_of_month.config(text=balance_month)
        return balance_month

    def show_month_expenses_list(self):
        self.expense_list_box_two.delete(0, tk.END)
        if self.list_month == []:
            messagebox.showinfo("Empty", "In this month you do not have any expenses")
            return
        for expense in self.list_month:
            self.expense_list_box_two.insert(
                tk.END,
                f"Decription --> {expense.name}, date --> {expense.date}, amount --> {expense.price/100}",
            )

    def total_balance_before_specific_month(self):
        month, year = self.get_date()
        previous_months = self.analizer.get_previous_months(
            self.controler.expenses, month, year
        )
        balance_previous_monts = self.analizer.get_balance(previous_months)
        balance_previous_monts = balance_previous_monts / 100
        self.total_balance_before.config(text=balance_previous_monts)
        return balance_previous_monts

    def total_balance_after_month(self):
        month_balance = self.show_month_balance_label()
        balance_previous_monts = self.total_balance_before_specific_month()
        total_balance = balance_previous_monts + month_balance
        total_balance = total_balance
        self.total_balance_after.config(text=total_balance)
