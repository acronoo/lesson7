# 2 Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, parameter):
        self.parameter = parameter   # self.parameter это соответственно размер или рост

    @abstractmethod
    def expense(self):  # Расход ткани абстрактный метод, который реализуем в дочернем классе
        pass

    def __str__(self):
        return str(self.parameter)


class Coat(Clothes):  # Пальто

    @property
    def expense(self):
        return self.parameter / 6.5 + 0.5


class Suit(Clothes):  # Костюм

    @property
    def expense(self):
        return self.parameter * 2 + 0.3


a = Coat(52)  # Пальто а с размером 52
b = Suit(1.80)  # Костюм с ростом 1.80
print(a)
print(a.expense)
print(b.expense)
