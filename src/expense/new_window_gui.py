import tkinter as tk
from tkinter import messagebox, ttk

class NewWindowGui():
    def __init__(self) -> None:
        pass

    def new_window(self):
        self.window = tk.Toplevel()
        self.window.title("Bob")
        self.window.geometry("600x400")
        
        
        self.expense_list_box_two = tk.Listbox(
            self.window, width=50, height=10, foreground="white"
        )
        self.expense_list_box_two.grid(
            row=0, column=2, rowspan=5, padx=10, pady=10, sticky="nsew")
        
        
        
        