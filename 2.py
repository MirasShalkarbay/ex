# lambda exersices

# x = lambda a : a + 10
# print(x(5))

# def lgfdnlfe(a):
#     print(a + 10)

# # x = lambda a, b : a * b
# # print(x(10, 5))
    
# def my_function(n):
#     return lambda a : n * a

# mydoubler = my_function(2)
# mytripler = my_function(3)

# print(mydoubler(11))
# print(mytripler(11))

# class MyClass:
#     x = 5

# p1 = MyClass()
# print(p1.x)

# class Person:
#     def __init__(self, name, lname):
#         self.name = name
#         self.lname = lname
#         self.age = 20
    
#     def info(self):
#         print(self.name+ " " + self.lname + " " + str(self.age) + " years old" )

# P1 = Person("John", "Wilber")
# P2 = Person("Jesica", "Huston")

# print(P1.age, P2.name, P2.lname)
# P1.info()

# #Ex 1
# class Stringinput:
#     def __init__(self):
#         self.input = None

#     def get_string(self):
#         self.input = input("")

#     def printString(self):
#         print(self.input.upper())

# string_input = Stringinput()

# string_input.get_string()
# string_input.printString()

# class Shape:
#     def __init__(self, area = 0):
#         self.area = area

#     def defolt(self):
#         print("defolt area of the shape {}".format(self.area))

# class Square(Shape):
#     def __init__(self, length):
#         super().__init__()
#         self.length = length

#     def calculate_area(self):
#         self.area = self.length ** 2
#         print("Calculated area : " + str(self.area))

# length_input = float(input())

# square = Square(length_input)

# square.defolt()
# square.calculate_area()

class Shape:
    def __init__(self):
        self.area = 0

    def defolt(self):
        print("defolt area of the shape {}".format(self.area))

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = self.length * self.width

    def area_of_rectangle(self):
        print(self.area)

l = int(input())
w = int(input())

rectangle = Rectangle(l, w)
rectangle.area_of_rectangle()
