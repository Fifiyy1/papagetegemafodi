import random


class Alkash:
    def __init__(self, name="oleg", kind=None, garazh=None, banda=None):
        self.name = name
        self.money = 0
        self.booze = 0
        self.inadequacy = 20
        self.kind = kind
        self.garazh = garazh
        self.banda = banda

    def get_garazh(self):
        self.garazh = Garazh()

    def get_kind(self):
        self.kind = Kind()

    def get_banda(self):
        self.banda = Banda()

    def drink(self):
        if self.banda.booze <=0:
            self.theft("vodka")
        else:
            if self.inadequacy >=100:
                self.inadequacy = 100
                return
            self.inadequacy+=5
            self.banda.drink-=5

    def chill(self):
        self.inadequacy+=10
        self.banda+=5

    def zapoi(self):
        self.banda.inadequacy = bandas_type[self.banda.inadequacy]["strength"]
        self.booze += random.randint(40, 80)

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}")
        print(f"Money – {self.money}")
        print(f"Booze – {self.booze}")
        print(f"Inadequacy – {self.inadequacy}")
        garazh_indexes = "banda indexes"
        print(f"{garazh_indexes:^50}")
        print(f"drink – {self.drink}")
        banda_type = f"{self.banda.type} car indexes"
        print(f"{banda_type:^50}")
        print(f"Inadequacy – {self.banda.inadequacy}")
        print(f"Strength – {self.banda.strength}")

    def is_alive(self):
        if self.booze<=10:
            print("Depression…")
            return False
        if self.inadequacy>1000:
            print("Dead…")
            return False
        if self.money<-500:
            print("No vodka…")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.garazh is None:
            print("Settled in the garazh")
            self.get_garazh()
        if self.banda is None:
            self.get_banda()
            print(f"I created my banda {banda.type}")
        if self.kind is None:
            self.get_kind()
            print(f"I don't have a kind, going to get a kind alkahnya")
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.booze < 20:
            print("I'll go to drink")
            self.drink()
        elif self.banda.strength < 15:
            print("I need to kachat` my banda")
            self.to_repair()
        elif dice == 1:
            print("Let`s drink!")
            self.chill()



oleg = Alkash(name="Oleg")


bandas_type = {
    "Alkashnya 1": {"inadequacy": 100, "strength": 100},
    "Zabivnie": {"inadequacy": 50, "strength": 40},
    "3 klas children": {"inadequacy": 1000, "strength": 10},
    "Narkomani": {"inadequacy": 80, "strength": 120},
        }
for day in range(1, 1001):
    if oleg.live(day) == False:
        break