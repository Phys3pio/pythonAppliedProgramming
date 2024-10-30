class Human:
    # Статические поля
    default_name = 'NoName'
    default_age = 18

    def __init__(self, name=default_name, age=default_age):
        # Публичные свойства
        self.name = name
        self.age = age

        # Приватные свойства
        self.__money = 10000
        self.__house = None

    def info(self):
        print('Имя:', self.name)
        print('Возраст:', self.age)
        print('Дом:', self.__house)
        print('Деньги:', self.__money)

    @staticmethod
    def default_info():
        print('Статическое имя:', Human.default_name)
        print('Статический возраст:', Human.default_age)

    def make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, amount):
        self.__money += amount
        print(f'{self.name} заработал {amount} денег.')

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.make_deal(house, price)
            print(f'{self.name} купил дом за {price}.')
        else:
            print(f'У {self.name} недостаточно средств для покупки дома.')
class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount / 100)
class SmallHouse(House):
    def __init__(self):
        super().__init__(40, 500000)



Human.default_info()
human = Human(name='Иван', age=25)
human.info()
small_house = SmallHouse()
human.buy_house(small_house, 10)
human.earn_money(400000)
human.buy_house(small_house, 15)
human.info()