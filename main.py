from player import Player
from location import Location
from enemy import Enemy
from item import Item

# Создание локаций
start_location = Location("Стартовая локация", "Вы начинаете свое путешествие здесь.")
middle_location = Location("Средняя локация", "Здесь находятся более сильные враги.")
end_location = Location("Финальная локация", "Вас ждет последний бой здесь.")

# Создание игрока
player = Player(input("Введите ваше имя: "), 20, 5, 2, 0, start_location)

# Создание врагов
enemy1 = Enemy("Враг 1", 10, 2, 1, 5, 10)
enemy2 = Enemy("Враг 2", 20, 4, 2, 10, 20)
enemy3 = Enemy("Враг 3", 30, 6, 3, 15, 30)

# Создание предметов
item1 = Item("Предмет 1", "Описание предмета 1.")
item2 = Item("Предмет 2", "Описание предмета 2.")
item3 = Item("Предмет 3", "Описание предмета 3.")

# Добавление врагов и предметов в локации
start_location.add_enemy(enemy1)
start_location.add_item(item1)

middle_location.add_enemy(enemy2)
middle_location.add_item(item2)

end_location.add_enemy(enemy3)
end_location.add_item(item3)

# Добавление соседних локаций
start_location.add_neighbor("восток", middle_location)
middle_location.add_neighbor("запад", start_location)
middle_location.add_neighbor("восток", end_location)
end_location.add_neighbor("запад", middle_location)

# Начало игры
current_location = start_location
print(current_location)

while True:
    # Вывод возможных направлений для перемещения
    print("Доступные направления: ")
    for direction, location in current_location.neighbors.items():
        print("- {} в направлении {}".format(location.name, direction))

    # Вывод врагов и предметов в локации
    current_location.show_enemies()
    current_location.show_items()

    # Обработка команды игрока
    command = input("Введите команду: ")
    if command == "атака":
        current_enemy = None
        for enemy in current_location.enemies:
            if enemy.hp > 0:
                current_enemy = enemy
                break
        if current_enemy:
            while current_enemy.hp > 0 and player.hp > 0:
                # Ход игрока
                player_attack = player.attack
                current_enemy.take_damage(player_attack)
                if current_enemy.hp <= 0:
                    current_location.remove_enemy(current_enemy)
                    player.add_gold(current_enemy.drop_gold())
                    break
                # Ход врага
                enemy_attack = current_enemy.attack
                player.take_damage(current_enemy.attack)
                if player.hp <= 0:
                    print("Вы погибли!")
                    exit()
                else:
                    print("В локации нет врагов.")
    elif command.startswith("идти "):
        direction = command.split(" ")[1]
        if direction in current_location.neighbors:
            current_location = current_location.get_neighbor(direction)
            print(current_location)
        else:
            print("Неверное направление.")
    elif command == "инвентарь":
        player.show_inventory()
    elif command.startswith("использовать "):
        item_name = command.split(" ")[1]
        item = player.get_item(item_name)
        if item:
            item.use(player)
        else:
            print("У вас нет такого предмета.")
    else:
        print("Неверная команда.")