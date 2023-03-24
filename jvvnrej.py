class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []
    def add_passengers(self, *args):
        for passengers in args:
            self.passengers.append(human)
    def del_passengers(self, human):
        self.passengers.remove(human)
        print(f"Remove {human.name} from {self.brand}")
    def print_passengers_names(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(F"There are no passenger in {self.brand}")


nick = Human("Nick")
kate = Human("Kate")
car = Auto("BMW")
car.add
