double = lambda x: x * 2

def double(x):

Animal

age
weight


Cat

breed 
name

method: feed (increases weight)

class Animal():
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight
class Cat(Animal):
    def __init__(self, age, weight, breed, name):
        super().__init__(age, weight)
    def feed(self):
        self.weight += 1
