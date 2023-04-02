class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, player):
        # Метод для использования предмета
        pass

class Weapon(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage

    def use(self, player):
        # Метод для использования оружия
        player.weapon = self
        print("Вы взяли оружие {}.".format(self.name))

class Potion(Item):
    def __init__(self, name, description, healing):
        super().__init__(name, description)
        self.healing = healing

    def use(self, player):
        # Метод для использования зелья лечения
        player.heal(self.healing)
        print("Вы использовали зелье лечения {} и восстановили {} единиц здоровья.".format(self.name, self.healing))