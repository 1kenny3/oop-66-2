from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health 
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1 

    @abstractmethod
    def attack(self):
        pass


class Warrior(Hero):
    def attack(self):
        print("Воин атакует мечом")

class Mage(Hero):
    def attack(self):
        print("Маг использует магию")

class Assassin(Hero):
    def attack(self):
        print("Ассасин атакует из-под тишка")

warrior = Warrior(name="Артур", level=10, health=150, strength=50)
mage = Mage(name="Мерлин", level=15, health=80, strength=20)
assassin = Assassin(name="Эцио", level=12, health=100, strength=40)


warrior.greet()
warrior.attack()
warrior.rest()

mage.greet()
mage.attack()
mage.rest()

assassin.greet()
assassin.attack()
assassin.rest()