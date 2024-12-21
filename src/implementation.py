# Реализация

from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
from pandas import DataFrame


class Format(ABC):
    """Отоброжение данных
    """

    @abstractmethod
    def show(self, data):
        raise NotImplementedError


class Graphs(Format):
    """График

    Args:
        ABC (_type_): _description_
    """

    def show(self, data: dict):
        """Отобразить данные

        Args:
            numbers (_type_): _description_
        """
        list_key = []
        list_value = []
        for key, value in data.items():
            list_key.append(key[0:3])
            list_value.append(value)
        plt.plot(list_key, list_value)
        plt.show()


class Table(Format):
    """Таблица

    Args:
        Format (_type_): _description_
    """

    def show(self, data: dict):
        list_key = []
        list_value = []
        for key, value in data.items():
            list_key.append(key[0:3])
            list_value.append(value)

        table = DataFrame({"Деньги": list_key}, index=list_value)
        print(table)


# a = Graphs()
# a.show({"Декабрь":10,
#             "Январь":0,
#             "Февраль":0,
#             "Март":0,
#             "Апрель":0,
#             "Май":0,
#             "Июнь":0,
#             "Июль":0,
#             "Август":0,
#             "Сентабрь":0,
#             "Октябрь":0,
#             "Ноябрь":0})

# a = Table()
# a.show("Доход",{"Декабрь":10,
#             "Январь":0,
#             "Февраль":0,
#             "Март":0,
#             "Апрель":0,
#             "Май":0,
#             "Июнь":0,
#             "Июль":0,
#             "Август":0,
#             "Сентабрь":0,
#             "Октябрь":0,
#             "Ноябрь":0})
