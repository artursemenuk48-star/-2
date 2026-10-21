class Cat:
    def __init__(self, name):
        self.name = name
        self.energy = 50
        self.hunger = 50
        self.happiness = 50

    def eat(self, food_amount):
        self.hunger = max(0, self.hunger - food_amount)
        self.happiness = min(100, self.happiness + 10)
        print(f"{self.name} поїв. Голод: {self.hunger}, Щастя: {self.happiness}")

    def sleep(self, hours):
        self.energy = min(100, self.energy + hours * 10)
        self.hunger = min(100, self.hunger + 5 * hours)
        print(f"{self.name} поспав {hours} год. Енергія: {self.energy}")

    def play(self):
        can_play = self.energy >= 20
        self.energy -= 20 * can_play
        self.happiness = min(100, self.happiness + 20 * can_play)
        self.hunger = min(100, self.hunger + 10 * can_play)

        messages = {
            True: f"{self.name} погрався! Щастя: {self.happiness}, Енергія: {self.energy}",
            False: f"{self.name} занадто втомився для ігор!"
        }
        print(messages[can_play])

    def __str__(self):
        return f"{self.name}: енергія {self.energy}, голод {self.hunger}, щастя {self.happiness}"

my_cat = Cat("Барсик")
print(my_cat)
my_cat.play()
my_cat.eat(30)
my_cat.sleep(4)
print(my_cat)