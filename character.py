from constants import *

class Player:
    def __init__(self):
        self.name = self.get_name()
        self.health = MAX_HEALTH
        self.attack = MAX_ATTACK
        self.defense = MAX_DEFENSE
        self.items = []
        self.level = 1
        self.experience = 0

    def get_name(self):
        name = input("Введите имя своего персонажа: ")
        return name

    def level_up(self):
        self.level += 1
        self.attack += 2
        print(f"{self.name} достиг нового уровня {self.level}!")

    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= 100:
            self.level_up
            self.experience = 0
        print(f"{self.name} получил {amount} ед. опыта.")

    def attack_enemy(self, enemy):
        # Метод для атаки врага
        damage = self.attack - enemy.defense
        enemy.health -= damage
        print(f"{self.name} атаковал {enemy.name} и нанес {damage} урона.")
    
    def use_item(self, item):
        # Метод для использования предмета
        if item in self.items:
            item.apply_effect(self)
            self.items.remove(item)
            print(f"{self.name} использовал {item.name}.")
        else:
            print(f"{self.name} не имеет предмета {item.name}.")
    
    def is_alive(self):
        # Метод для проверки, жив ли персонаж
        return self.health > MIN_HEALTH