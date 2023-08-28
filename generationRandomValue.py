import random

print(random.random())
for i in range(3):
    print(random.randint(10, 20))

members = ['ahmad', 'hadi', 'ali', 'mohammad']
print(random.choice(members))


class Dise:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dise()
print(dice.roll())
