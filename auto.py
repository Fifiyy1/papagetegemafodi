class Auto:
        def __init__(self, brand_list):
            self.brand = random.choice(list(brand_list))
            self.fuel = brand_list[self.brand]["fuel"]
            self.strength = brand_list[self.brand]["strength"]
            self.consumption = brand_list[self.brand]["consumption"]

        def drive(self):
            if self.brand == "bike":
                if self.strength > 0:
                    self.strength -= 1
                    return True
                else:
                   print("The car cannot move")
                   return False
            else:
                if self.strength > 0 and self.fuel >= self.consumption:
                    self.fuel -= self.consumption
                    self.strength -= 1
                    return True
                else:
                    print("The car cannot move")
                    return False

brands_of_car = {
    "BMW":{"fuel":100, "strength":100, "consumption": 6},
    "Lada":{"fuel":50, "strength":40, "consumption": 10},
    "Volvo":{"fuel":70, "strength":150, "consumption": 8},
    "Ferrari":{"fuel":80, "strength":120, "consumption": 14},
    "Mitsubishi":{"fuel":60, "strength":90, "consumption": 5}
        }
