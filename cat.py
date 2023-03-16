class cat:
   print("Hi")
   def __init__(self, color=None):
        self.weight = 160
        print("I am alive!")
        self.breed = input("Какой породы ваш кошак? :  ")
        self.color = color
   def drive(self):
        print("sleep /_/")

   def __str__(self):
        return f"Наш кошак - {self.breed}\n {self.color} color"
