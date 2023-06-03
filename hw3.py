import random
class Dog:
    def __init__(self, name):
        self.petname = name
        self.energy = 2.5
        self.bond = 1
        self.happinest = 3
        self.alive = True
    def game(self):
        print("Time to play!")
        self.happinest += 0.25
        self.energy -= 1
    def to_sleep(self):
        print("Sleep time!")
        self.energy += 3
    def owner(self):
        print("Rest time")
        self.energy -= 1.5
        self.happinest += 3
        self.bond += 3
    def is_alive(self):
        if self.energy < -0.5:
            print("Past Out. The dog dropped dead on the ground...")
            self.alive = False
        elif self.happinest <= -3:
            print("Depression… The dog ran away...")
            self.alive = False
        elif self.bond > 10:
            print(f"Passed externally… R.I.P {self.petname}")
            self.alive = False

        def end_of_day(self):
            print(f"Energy = {self.energy}")
            print(f"Happiness ={round(self.happinest)}")

        def live(self, day):
            day = "Day" + str(day) + "of" + self.name + "life"
            print(f"{day:=^50}")
            live_cube = random.randint(1, 3)
            if live_cube == 1:
                self.game()
            elif live_cube == 2:
                self.to_sleep()
            elif live_cube == 3:
                self.ownerl()
            self.end_of_day()
            self.is_alive()

ruffus = Dog(name="Ruffus")
for day in range(365):
    if ruffus.alive == False:
            break
            ruffus.live(day)