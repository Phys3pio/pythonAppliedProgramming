class KgToPounds:
    def __init__(self, kg=0):
        # Используем свойство через декоратор для задания начального значения
        self.kg = kg

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')

    def to_pounds(self):
        return self.__kg * 2.20462
weight = KgToPounds(12)
print(weight.to_pounds())
print(weight.kg)
weight.kg = 41
print(weight.kg)
weight.kg = 'десять'