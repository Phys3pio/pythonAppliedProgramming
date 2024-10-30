class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def roll_over(self):
        print(self.name,"перекатился")
    def sit(self):
        print(self.name,"сел")
my_dog=Dog("Willie",6)
my_dog.roll_over()
my_dog.sit()


