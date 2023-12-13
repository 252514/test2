from __future__ import annotations
from expense.expense import Expense


class ExpanseController:
    def __init__(self) -> None:
        self.expenses: list[Expense] = []

    def add(self, expense: Expense) -> None:
        self.expenses.append(expense)

    def delete(self, index: int) -> None:
        if index > len(self.expenses):
            return
        del self.expenses[index]
