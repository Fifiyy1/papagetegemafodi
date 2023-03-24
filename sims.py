import random

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()


    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <=0:
            self.shopping("food")
        else:
            if self.satiety >=100:
                self.satiety = 100
                return
            self.satiety+=5
            self.home.food-=5


    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety-=4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Hooray! Delicious!")
            self.gladness+=10
            self.satiety+=2
            self.money-=15

    def chill(self):
        self.gladness+=10
        self.home.mess+=5

    def cat_time(self):
        self.gladness+=breeds[self.breeds]
        self.home.mess+=2
        self.gladness += 20

    def clean_deliver(self):
        self.money -=5
        self.home.mess = 0

    def clean_home(self):
        self.gladness-=5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength = brands_of_car[self.car.brand]["strength"]
        self.money -= random.randint(40, 80)

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}")
        print(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")

    def is_alive(self):
        if self.gladness<=10:
            print("Depression…")
            return False
        if self.satiety<0:
            print("Dead…")
            return False
        if self.money<-500:
            print("Bankrupt…")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, going to get a job {self.job.job} with salary {self.job.salary}")
        self.days_indexes(day)
        dice = random.randint(1,4)
        if self.satiety<20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess>15:
                print("I want to chill, but there is so much mess…\nSo I will clean the house")
                self.clean_deliver()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.money<0:
            print("Start working")
            self.work()
        elif self.gladness < 20:
            print("I`m so mad..\nSo I will play with my cat!")

        elif self.car.strength<15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 3:
            print("Time for treats!")
            self.shopping(manage="delicacies")
        elif dice == 4:
            print("Start working")
            self.work()


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
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14},
    "Mitsubishi": {"fuel": 60, "strength": 90, "consumption": 5},
    "Koshara": {"fuel": 100, "strength": 150, "consumption": 2},
    "Bomzh": {"fuel": 120, "strength": 50, "consumption": 8},
    "Roblox car 2014": {"fuel": 40, "strength": 10, "consumption": 10},
    "sled": {"fuel": 1000, "strength": 10, "consumption": 1},
        }
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

job_list = {
    "Java developer":
    {"salary":50, "gladness_less": 10 },
    "Python developer":
    {"salary":40, "gladness_less": 3 },
    "C++ developer":
    {"salary":45, "gladness_less": 25 },
    "Rust developer":
    {"salary":70, "gladness_less": 1 },
    "Bomzh":
    {"salary":1, "gladness_less": 20 },
    "cashier":
    {"salary":10, "gladness_less": 30 },
    "Holy father":
    {"salary": 100, "gladness_less": 45},
    "Alkash":
    {"salary": 0, "gladness_less": 50},
    "Thief":
    {"salary": 100, "gladness_less": 100},
        }

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

nick = Human(name="Nick")




class Cat:
    def __init__(self, breeds):
        self.hunger = 20
        self.breed = random.choice(list(breeds))
        self.catgladness = breeds[self.gladness]["gladness"]



breeds = {
    "Yasha": {"gladness": 100},
    "Lily": {"gladness": 45},
    "Pumba": {"gladness": 70},
    "Kitty": {"gladness": 80},
    "Max": {"gladness": 20},
         }

for day in range(1, 1000000000000000):
    if nick.live(day) == False:
        break