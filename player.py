class Player:
    def __init__(self, name, max_hp, attack, defense, gold, location, weapon=None, items=None):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.defense = defense
        self.gold = gold
        self.location = location
        self.weapon = weapon
        self.items = items or []

    def take_damage(self, amount):
        # Метод для уменьшения здоровья игрока
        damage = amount - self.defense
        damage = max(damage, 1)
        self.hp -= damage
        print("Вы получили {} единиц урона.".format(damage))
        if self.hp <= 0:
            print("Игра окончена. Вы проиграли.")
            return True
        else:
            return False

    def heal(self, amount):
        # Метод для восстановления здоровья игрока
        self.hp = min(self.max_hp, self.hp + amount)

    def add_item(self, item):
        # Метод для добавления предмета в инвентарь игрока
        self.items.append(item)

    def remove_item(self, item):
        # Метод для удаления предмета из инвентаря игрока
        if item in self.items:
            self.items.remove(item)

    def show_inventory(self):
        # Метод для вывода инвентаря игрока
        print("Ваш инвентарь:")
        for item in self.items:
            print("- {}".format(item.name))

    def move(self, direction):
        # Метод для перемещения игрока на другую локацию
        location = self.location.get_neighbor(direction)
        if location is None:
            print("Вы не можете пойти в этом направлении.")
        else:
            self.location = location
            print("Вы переместились в локацию {}.".format(location.name))

    def attack_enemy(self, enemy):
        # Метод для атаки врага
        if self.weapon is None:
            damage = self.attack
        else:
            damage = self.weapon.damage + self.attack
        if enemy.take_damage(damage):
            self.gold += enemy.drop_gold()

    def add_gold(self, amount):
        self.gold += amount
        print(f"Вы получили {amount} золота. Теперь у вас {self.gold} золота.")

    def __str__(self):
        return "{} ({} здоровья, {} золота)".format(self.name, self.hp, self.gold)