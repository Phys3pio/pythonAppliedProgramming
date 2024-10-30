class Nikola:
    __slots__ = ['name','age']
    def __init__(self,name,age):
        self.age=age
        if name!='Николай':
            self.name="Я не "+name+",а Николай"
        else:
            self.name=name
person1 = Nikola('Иван', 31)
person2 = Nikola('Николай', 14)
print(person1.name)
print(person2.name)
person2.surname = 'Петров'
