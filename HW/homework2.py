import random

# 📌 Родительский класс
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

# 📌 Дочерние классы с уникальными атрибутами и переопределенным attack()
class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina
    
    def attack(self):
        print("Воин атакует мечом!")

class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana
    
    def attack(self):
        print("Маг кастует заклинание!")

class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth
    
    def attack(self):
        print("Ассасин атакует из-под тишка!")

# 📌 Создание объектов
warrior_obj = Warrior('Артур', 10, 100, 20, 50)
mage_obj = Mage('Гэндальф', 12, 70, 10, 100)
assassin_obj = Assassin('Эцио', 11, 80, 25, 40)

# Словарь для логики игры
heroes = {
    "warrior": warrior_obj,
    "mage": mage_obj,
    "assassin": assassin_obj
}

# 🎮 Мини-игра "Камень, Ножницы, Бумага"
user_input = input("Выберите героя (Warrior / Mage / Assassin): ").lower()

if user_input in heroes:
    user_hero = heroes[user_input]
    
    # Программа случайно выбирает противника
    enemy_key = random.choice(list(heroes.keys()))
    enemy_hero = heroes[enemy_key]

    print(f"Вы выбрали: {user_hero.__class__.__name__}")
    print(f"Противник: {enemy_hero.__class__.__name__}")

    # Логика определения победителя
    if user_input == enemy_key:
        print("Ничья!")
    elif (user_input == "warrior" and enemy_key == "assassin") or \
         (user_input == "assassin" and enemy_key == "mage") or \
         (user_input == "mage" and enemy_key == "warrior"):
        user_hero.attack()
        print(f"{user_hero.__class__.__name__} победил!")
    else:
        enemy_hero.attack()
        print(f"{enemy_hero.__class__.__name__} победил!")
else:
    print("Неверный ввод. Пожалуйста, выберите Warrior, Mage или Assassin.")