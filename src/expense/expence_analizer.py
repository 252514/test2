from expense.expanse_controller import Expense


class ExpenseAnalizer:
    def __init__(self) -> None:
        pass

    def get_month(self, list_expense: list[Expense], month: int, year: int):
        self.month_list = []
        for expense in list_expense:
            only_month = int(expense.date.split("/")[0])
            only_year = int(expense.date.split("/")[2])
            if only_month == month and only_year == year:
                self.month_list.append(expense)
        return self.month_list

    def get_balance(self, list_expense: list[Expense]) -> int:
        balance: int = 0
        for expense in list_expense:
            price = expense.price
            balance += price
        print(balance)
        return balance
