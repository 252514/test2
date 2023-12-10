from expense.expense import Expense


class ExpenceSerializator:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def serializate(self, expenses: list[Expense]):
        with open(self.filename, "w+") as f:
            for expense in expenses:
                s = f"{expense.name},{expense.price},{expense.date}\n"
                f.write(s)

    def deserializate(self) -> list[Expense]:
        with open(self.filename, "r") as f:
            string_expenses = f.readlines()
        list_expenses = []
        for expense in string_expenses:
            name, price, data = expense.rstrip().split(",")
            e = Expense(name, int(price), data)
            list_expenses.append(e)
        return list_expenses
