class Mammal:
    def walking(self):
        print(" walking")


class Dog(Mammal):
    def barking(self):
        print("barking")
    
class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walking()
dog1.barking()




