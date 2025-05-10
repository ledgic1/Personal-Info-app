class Character:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 100

    def level_up(self):
        self.level += 1
        self.health += 20
        print(f"{self.name} leveled up to {self.level}! Health is now {self.health}.")

# Try it
hero = Character("Archer")
hero.level_up()
hero.level_up()