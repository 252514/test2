class Expense:
    def __init__(self,name: str, price: int, date: str):
        self.name: str = name
        self.price: int = price
        self.date: str = date
        
    def __str__(self) -> str:
        return f"Expense name: {self.name}, price: {self.price}, date: {self.date}"

        