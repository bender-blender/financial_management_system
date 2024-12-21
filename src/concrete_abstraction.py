
from abstraction import Transaction
from implementation import (
    Format,
    Table,
    Graphs
)
from random import randint

class Income(Transaction):
    """Доход

    Args:
        Transaction (_type_): _description_
    """
    def __init__(self, display: Format):
        self.display = display
        super().__init__(display)
    
    def form_numbers(self):
        for key in self.data.keys():
            self.data[key] = randint(10,1000)
        self.display.show(self.data)


class Expenses(Transaction):
    """Рассходы

    Args:
        Transaction (_type_): _description_
    """
    def __init__(self, display: Format):
        self.display = display
        super().__init__(display)
    
    def form_numbers(self):
        for key in self.data.keys():
            self.data[key] = randint(-100,0)
        self.display.show(self.data)

# a = Income(Table())
# a.form_numbers()

# a = Income(Graphs())
# a.form_numbers()

b = Expenses(Table())
b.form_numbers()

b = Expenses(Graphs())
b.form_numbers()


