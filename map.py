class Location:
    def __init__(self, name, description, enemy=None, task=None):
        self.name = name
        self.description = description
        self.enemy = enemy  # Враг в локации (если есть)
        self.task = task  # Задание в локации (если есть)
        self.next_location = None  # Следующая локация на карте

    def __str__(self):
        return self.name
    

class Map:
    def __init__(self):
        self.start_location = None
        self.final_location = None

    def add_location(self, location):
        # Метод для добавления локации на карту
        if not self.start_location:
            self.start_location = location
        elif not self.final_location:
            self.final_location = location
        else:
            current_location = self.start_location
            while current_location.next_location:
                current_location = current_location.next_location
            current_location.next_location = location



location_1 = Location(
    name="Castle Entrance",
    description="Вы стоите перед входом в замок, где живет коварный враг Syntax Error.",
    enemy=Enemy(name=ENEMY_1, health=50, attack=8, defense=2)
)
location_2 = Location(
    name="The Forest",
    description="Вы находитесь в густом лесу, где живет враг Runtime Error.",
    enemy=Enemy(name=ENEMY_2, health=60, attack=10, defense=3),
    task=Task(
        name="Сбор ягод",
        description="Соберите 10 ягод и принесите их к старику в лесу."
    )
)
location_3 = Location(
    name="The Mountains",
    description="Вы поднимаетесь по крутым горам, чтобы победить врага Memory Leak.",
    enemy=Enemy(name=ENEMY_3, health=80, attack=12, defense=4)
)

game_map = Map()
game_map.add_location(location_1)
game_map.add_location(location_2)
game_map.add_location(location_3)