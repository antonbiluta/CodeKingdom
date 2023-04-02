def print_location(location):
    # Функция для вывода информации о локации на экран
    print(f"Вы находитесь в {location.name}.")
    print(location.description)
    if location.enemy:
        print(f"Вы видите врага: {location.enemy.name} ({location.enemy.health} HP).")
    if location.task and not location.task.is_completed:
        print(f"У вас есть задание: {location.task}.")
    if location.items:
        print("Вы видите следующие предметы:")
        for item in location.items:
            print(f"- {item}")

def process_command(command, player, game_map):
    # Функция для обработки команды игрока
    parts = command.split()
    verb = parts[0]
    if verb == "идти":
        direction = parts[1]
        player.go(direction, game_map)
    elif verb == "осмотреться":
        print_location(player.location)
    elif verb == "атаковать":
        if player.location.enemy:
            battle = Battle(player, player.location.enemy)
            battle.start()
            if player.location.enemy.health <= 0:
                player.location.enemy = None
    elif verb == "взять":
        item_name = " ".join(parts[1:])
        if item_name in player.location.items:
            player.items.append(item_name)
            player.location.items.remove(item_name)
            print(f"Вы взяли '{item_name}'")
        else:
            print("Этого предмета здесь нет.")
    elif verb == "инвентарь":
        if not player.items:
            print("Ваш инвентарь пуст.")
        else:
            print("Ваш инвентарь содержит следующие предметы:")
            for item in player.items:
                print(f"- {item}")
    else:
        print("Я не понимаю, что вы хотите.")