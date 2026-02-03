class Coffee:
    def __init__(self, size):
        self.size=size
    def prepare(self):
        return "Готовим кофе размера "+self.size
    def price(self):
        if self.size=='S':
            return 100
        elif self.size=='M':
            return 150
        elif self.size=='L':
            return 200
class Latte(Coffee):
    def prepare(self):
        return super().prepare()+' с молоком'
class Espresso(Coffee):
    def price(self):
        return super().price()+50
    
c=Coffee('M')
print(c.prepare())
print(c.price())

l=Latte('L')
print(l.prepare())
print(l.price())

e=Espresso('S')
print(e.prepare())
print(e.price())