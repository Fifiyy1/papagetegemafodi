#Створення класу
# class Student:
#    print("Hi")

#Створемо екземпляр класу
# class Student:
#    print("Hi")
#
# first_student = Student()


#конструктор класу автоматично викликається під час створення екземпляра.
# class Student:
#    print("Hi")
#    def __init__(self):
#        self.height = 160
#        print("I am alive!")
#
# first_student = Student()

#self - посилання на самого себе
# class Student:
#    def __init__(self):
#        self.height = 160
#        print(self)
#
# first_student = Student()


#аналогічний виклик, але з використанням класу
# class Student:
#    def __init__(self):
#        self.height = 160
#        print(self)
#
# first_student = Student()
# Student.__init__(self=first_student)


#Отримаємо доступ до параметра
# class Student:
#    def __init__(self):
#        self.height = 160
#
# nick = Student()
# print(nick.height)

#в конструктор класу потрапляють початкові параметри,
# які передаються під час створення екземпляра
# class Student:
#    def __init__(self, height=160):
#        self.height = height
#
# nick = Student()
# kate = Student(height=170)
# print(nick.height)
# print(kate.height)

#створення атрибуту класу, який змінюватиметься
# відповідно до кількості оголошених екземплярів
# class Student:
#    amount_of_students = 0
#    def __init__(self, height=160):
#        self.height = height
#        Student.amount_of_students += 1
#
# nick = Student ()
# kate = Student(height=170)
# ann = Student()
# print(ann.amount_of_students)
# print(Student.amount_of_students)

#Оскільки об’єкт та екземпляр взаємопов’язані,
# то атрибут класу можна дістати з допомогою self
# class Student:
#    height = 160
#    def __init__(self):
#        print(self.height)
#
# nick = Student()

#зробимо так, щоби кожен наступний студент ставав вищим
# class Student:
#    height = 160
#    def __init__(self):
#        print(self.height)
#        self.height+=10
#
# nick = Student()
# kate = Student()
#Щось пішло не так :)
#якщо потрібно змінювати атрибут класу,
# звертатися до нього треба через сам клас


#Атрибути об’єкта перекривають собою атрибути класу
# class Student:
#    height = 160
#    def __init__(self):
#        self.height = 170
#
#    def printer(self):
#        print(self.height)
#
# nick = Student()
# nick.printer()


#Області видимості класів аналогічні таким у функціях.
# x = 10
# class Looker:
#    x = 15
#    print(x)
#    def func1(self):
#        x = 20
#        print(x)
#        def func2():
#            x = 30
#            print(x)
#        func2()
# some_object = Looker()
# some_object.func1()



#Методи класів

#додамо метод grow(), що збільшуватиме зріст студента та викличемо його
# class Student:
#    amount_of_students = 0
#    def __init__(self, height=160):
#        self.height = height
#        Student.amount_of_students+=1
#    def grow(self, height=1):
#        self.height+=height
#
# nick = Student()
# kate = Student(height=170)
# kate.grow()
# nick.grow(height=15)
# print(kate.height)
# print(nick.height)

'''
щоби під час видруковування об’єкту не отриму-
вати рядок із незрозумілим вмістом, можна оголосити
метод __str__(), який має повертати рядок відповід-
ного змісту
'''
# class Student:
#    def __init__(self, name=None):
#        self.name = name
#    def __str__(self):
#        return f"I am a student. My name is {self.name}."
#
# nick = Student(name = "Nick")
# print(nick)


#видалити об’єкт дає змогу метод __del__(),
# який автоматично запускається наприкінці програми
# class Student:
#    def __init__(self, name=None):
#        self.name = name
#    def __del__(self):
#        print("Training is over. I am now an expert!")
#
# nick = Student()


'''
Іноді є завдання перевірити істинність об’єк-
ту або його довжину. Тоді стануть у пригоді методи
__bool__ () та __len__()
'''
# class Student:
#    def __init__(self, name=None, height=160):
#        self.name = name
#        self.height = height
#    def __bool__(self):
#        return self.name != None
#    def __len__(self):
#        return self.height
# 
# nick = Student()
# #nick = Student(name="Nick", height=170)
# print(nick.__len__())
# print(nick.__bool__())
# print(len(nick))
# print(bool(nick))
