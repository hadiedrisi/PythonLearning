class Point:
    def __init__(self, x, y): #contractor 
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


p = Point(10, 23)
p.draw()


#constarctor  


class Person:
    def __init__(self , name):
        self.name = name
    
    def talk(self):
        print(f"my name is {self.name}")



person = Person("hadi")
person.talk()