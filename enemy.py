import random

class Enemy:
    def __init__(self, name, max_hp, attack, defense, min_gold, max_gold):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.defense = defense
        self.min_gold = min_gold
        self.max_gold = max_gold

    def take_damage(self, amount):
        # Метод для уменьшения здоровья врага
        damage = amount - self.defense
        damage = max(damage, 1)
        self.hp -= damage
        print("Вы нанесли врагу {} единиц урона.".format(damage))
        if self.hp <= 0:
            print("Вы победили врага {}.".format(self.name))
            return True
        else:
            return False

    def attack_player(self, player):
        # Метод для атаки игрока
        damage = self.attack
        print("Враг {} атакует вас.".format(self.name))
        if random.random() < 0.5:
            print("Вы избежали атаки.")
        else:
            if player.take_damage(damage):
                return False
        return True

    def drop_gold(self):
        # Метод для получения случайного количества золота при победе над врагом
        return random.randint(self.min_gold, self.max_gold)