class Player:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def hit(self, monster):
        print(f"{self.name} атакує {monster.name}!")
        monster.health -= self.attack

    def is_alive(self):
        return self.health > 0


class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def hit(self, player):
        print(f"{self.name} атакує {player.name}!")
        player.health -= self.attack

    def is_alive(self):
        return self.health > 0


# --- СИМУЛЯЦІЯ ---
player = Player("Герой", 100, 20)
monster = Monster("Монстр", 80, 15)

print("⚔️ Бій почався!\n")

while player.is_alive() and monster.is_alive():
    player.hit(monster)
    print(f"Здоров'я монстра: {monster.health}")

    if monster.is_alive():
        monster.hit(player)
        print(f"Здоров'я гравця: {player.health}")

    print("-----")

if player.is_alive():
    print(" Гравець переміг!")
else:
    print(" Монстр переміг!")