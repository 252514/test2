class Expense:
    def __init__(self, name: str, price: int, date: str):
        self.name: str = name
        self.price: int = price
        self.date: str = date

    def __str__(self) -> str:
        return f"Expense name: {self.name}, price: {self.price}, date: {self.date}"

    def __eq__(self, __value: object) -> bool:
        if (
            self.name == __value.name
            and self.price == __value.price
            and self.date == __value.date
        ):
            return True
        return False
