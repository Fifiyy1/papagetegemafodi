



class Avto:
    def __init__(self, color=None):
        self.brand = input("marka????  ")
        self.color = color
        self.engine = input("mator kakoy a   ")
    def drive(self):
        print("DRIVE MRUUUUW")

    def __str__(self):
        return f"moi car - {self.brand}\n {self.color} color"
car = Avto(color = "пинк")


print(car)