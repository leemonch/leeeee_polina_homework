class Potion:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def drink(self) -> str:
        return f"Вы выпили {self.name}! Сила: {self.power}"
hp = Potion("Зелье здоровья", 50)
print(hp.drink())