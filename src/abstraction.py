# Абстракция
from abc import ABC, abstractmethod

class Transaction(ABC):
    """Транзакция

    Args:
        ABC (_type_): _description_
    """
    def __init__(self, display):
        self.display = display # Способ отображение 

        self.data = {
            "Декабрь":0,
            "Январь":0,
            "Февраль":0,
            "Март":0,
            "Апрель":0,
            "Май":0,
            "Июнь":0,
            "Июль":0,
            "Август":0,
            "Сентабрь":0,
            "Октябрь":0,
            "Ноябрь":0

        } # База данных
    
    @abstractmethod
    def form_numbers(self):
        """Формировать числа

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError