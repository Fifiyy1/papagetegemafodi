#конструктор класу автоматично викликається під час створення екземпляра.
class Student:
    print("Hi")
    def __init__(self):
        self.height = 180
        print("I am alive!")
    money = 0
def __init__(self, height=180):
    self.height = height
    Student.money += 1
    print(self.money)
    print(Student.money)


first_student = Student()


def __init__(self, height=180):
    self.height = height
    Student.amount_of_students += 1
    print(Student.amount_of_students)

#self - посилання на самого себе
class Student:
    def __init__(self):
        self.height = 180
        print(self)

first_student = Student()


#аналогічний виклик, але з використанням класу
class Student:
    def __init__(self):
        self.height = 180
        print(self)

first_student = Student()
Student.__init__(self=first_student)


#Отримаємо доступ до параметра
class Student:
    def __init__(self):
        self.height = 180
nick = Student()
print(nick.height)

#в конструктор класу потрапляють початкові параметри,які передаються під час створення екземпляра
class Student:
    def __init__(self, height=180):
        self.height = height

nick = Student()


#створення атрибуту класу, який змінюватиметься відповідно до кількості оголошених екземплярів








#Оскільки об’єкт та екземпляр взаємопов’язані, то атрибут класу можна дістати з допомогою self
class Student:
    height = 180
    def __init__(self):
        print(self.height)

nick = Student()

#зробимо так, щоби кожен наступний студент ставав вищим
class Student:
    height = 180
    def __init__(self):
        print(self.height)
        self.height+=10

nick = Student()
kate = Student()






#Атрибути об’єкта перекривають собою атрибути класу
class Student:
   height = 160
   def __init__(self):
       self.height = 170
   def printer(self):
       print(self.height)
nick = Student()
nick.printer()


class Student:
   amount_of_students = 0
   def __init__(self, height=160):
       self.height = height
       Student.amount_of_students+=1
   def grow(self, height=1):
       self.height+=height
nick = Student()
kate = Student(height=172)
kate.grow()
nick.grow(height=15)
print(kate.height)
print(nick.height)

