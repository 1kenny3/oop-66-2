class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает...")
        self.health += 1


hero1 = Hero(name="Арагорн", level=10, health=100, strength=20)
hero2 = Hero(name="Леголас", level=12, health=80, strength=15)


hero1.greet()
print(f"Статы до: Сила={hero1.strength}, Здоровье={hero1.health}")
hero1.attack()
hero1.rest()
print(f"Статы после: Сила={hero1.strength}, Здоровье={hero1.health}")




hero2.greet()
print(f"Статы до: Сила={hero2.strength}, Здоровье={hero2.health}")
hero2.attack()
hero2.rest()
print(f"Статы после: Сила={hero2.strength}, Здоровье={hero2.health}")