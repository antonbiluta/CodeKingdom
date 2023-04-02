class Location:
    def __init__(self, name, description, neighbors=None, enemies=None, items=None):
        self.name = name
        self.description = description
        self.neighbors = neighbors or {}
        self.enemies = enemies or []
        self.items = items or []

    def add_neighbor(self, direction, location):
        # Метод для добавления соседней локации
        self.neighbors[direction] = location

    def get_neighbor(self, direction):
        # Метод для получения соседней локации
        return self.neighbors.get(direction)

    def add_enemy(self, enemy):
        # Метод для добавления врага в локацию
        self.enemies.append(enemy)

    def remove_enemy(self, enemy):
        # Метод для удаления врага из локации
        if enemy in self.enemies:
            self.enemies.remove(enemy)

    def add_item(self, item):
        # Метод для добавления предмета в локацию
        self.items.append(item)

    def remove_item(self, item):
        # Метод для удаления предмета из локации
        if item in self.items:
            self.items.remove(item)

    def show_enemies(self):
        # Метод для вывода врагов в локации
        print("В локации {} находятся следующие враги:".format(self.name))
        for enemy in self.enemies:
            print("- {}".format(enemy.name))

    def show_items(self):
        # Метод для вывода предметов в локации
        print("В локации {} находятся следующие предметы:".format(self.name))
        for item in self.items:
            print("- {}".format(item.name))

    def __str__(self):
        return "{}: {}".format(self.name, self.description)