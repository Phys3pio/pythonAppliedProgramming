class Human:
    default_name="Илья"
    default_age=20
    def __init__(self,money,house):
        self.name=self.default_name
        self.age=self.default_age
        self.__money=money
        self.__house=house
    def info(self):
        print(self.name,self.age,self.__money,self.__house)
    def default_info(self):
        print(self.default_age,self.default_name)
    def make_deal(self,house,money):
        self.__money-=money
        self.__house=house
    def earn_money(self,money):
        self.__money+=money
    def buy_house(self,money,house):
        try:
            if self.__money>=money:
                print('Дом можно купить')
                self.make_deal(house,money)
        except:
            raise 'Дом нельзя купить'
class House:
    def __init__(self,area,price):
        self._price=price
        self._area=area
    def final_price(self,discounts):
        self._price-=discounts
SmallHouse=House(40,400000)
Human1=Human(300000,"House")
Human1.info()
SmallHouse1=House(40,400000)
Human1.buy_house(400000,SmallHouse)
Human1.earn_money(100000)
Human1.info()







