
from expense.expanse_controller import ExpanseController
from expense.expense import Expense
from expense.gui import Gui
from datetime import datetime
from expense.expence_serializator import ExpenceSerializator


if __name__ == "__main__":
    e1 = Expense('1',5,"2000")
    e2 = Expense('2',78,"3000")
    gui = Gui("Expense Tracker","1000x800")
    # gui.expense_input_date_entry.insert(0, datetime.today().strftime('%d-%m-%Y'))

    gui.controller.add(e1)
    gui.controller.add(e2)
    # s = ExpenceSerializator("bob.txt")
    # expenses_list =s.deserializate()
    # s.serializate(gui.controller.expenses)
    gui.run()