from expense.expanse_controller import ExpanseController
from expense.expense import Expense
from expense.gui import Gui
from expense.expence_serializator import ExpenceSerializator


if __name__ == "__main__":
    gui = Gui("Expense Tracker", "1000x800")
    gui.run()
