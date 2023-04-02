class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start(self):
        # Метод для начала боя
        print(f"Вы сражаетесь с {self.enemy.name} ({self.enemy.health} HP)!")
        while self.player.health > 0 and self.enemy.health > 0:
            self.player.attack(self.enemy)
            if self.enemy.health <= 0:
                break
            self.enemy.attack(self.player)
        if self.player.health > 0:
            print("Вы победили!")
            self.player.items["золото"] += self.enemy.gold
            print(f"Вы получили {self.enemy.gold} золота.")
            return True
        else:
            print("Вы проиграли!")
            return False