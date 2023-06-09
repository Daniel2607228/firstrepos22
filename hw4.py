class Model:
    def __init__(self):
        super().__init__()
        self.model = "BMW i8"

class Engine:
    def __init__(self):
        super().__init__()
        self.engine = "Turbo V2 350"

class Max_Speed:
    def __init__(self):
        super().__init__()
        self.max = 275

class Color_Pallete:
    def __init__(self):
        super().__init__()
        colist = ["Black", "Gray", "Blue", "White", "Copper", "Chrome"]
        print (colist)
        inp = input("Choose a color: ")
        if inp not in colist:
            print("Invalid Color!")
        self.color = inp

class Car(Model, Engine, Max_Speed, Color_Pallete):
    def info(self):
        print("Vehicle Data: ")
        print(self.model)
        print(self.engine)
        print(self.max)
        print(self.color)

car = Car()
car.info()