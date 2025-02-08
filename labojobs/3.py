class Shape:
    def __init__(self, area = 0, h = 0):
        self.area = area
        self.h = h

class Triangle(Shape):
    def __init__(self, height):
        super().__init__()
        self.height = height
    
    def calculate(self):
        self.area = self.height * self
