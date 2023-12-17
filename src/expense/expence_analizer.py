from expense.expanse_controller import ExpanseController, Expense


class ExpenseAnalizer:
    def __init__(self) -> None:
        self.controller: ExpanseController = ExpanseController()

    def get_month(self, list_expense: list[Expense], month: int, year: int):
        self.month_list = []
        for expense in list_expense:
            only_month = int(expense.date.split("/")[1])
            only_year = int(expense.date.split("/")[2])
            if only_month == month and only_year == year:
                self.month_list.append(expense)
        return self.month_list

    def get_balance(self, list_expense: list[Expense]) -> int:
        balance: int = 0
        for expense in list_expense:
            price = expense.price
            balance += price
        return balance

    def get_previous_months(self, list_expense: list[Expense], month: int, year: int):
        previous_months = []
        # print(month, year)
        # print(type(month), type(year))
        for expense in list_expense:
            only_month = int(expense.date.split("/")[1])
            only_year = int(expense.date.split("/")[2])
            # print("curr:", only_month, only_year)
            if only_year < year:
                previous_months.append(expense)
            elif only_year == year:
                if only_month < month:
                    previous_months.append(expense)
        return previous_months
