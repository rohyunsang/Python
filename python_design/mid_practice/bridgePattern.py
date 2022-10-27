from abc import *

class Color(metaclass = ABCMeta):
    @abstractmethod
    def fill_color(self):
        pass

class RedColor(Color):
    def fill_color(self):
        print("빨간색으로 채워")

class BlueColor(Color):
    def fill_color(self):
        print("파란색으로 채워")
        

class Shape(metaclass = ABCMeta):
    def __init__(self,color):
        self.color = color

    @abstractmethod
    def color_it(self):
        pass

class Rectangle(Shape):
    def __init__(self,color):
        super().__init__(color)
    
    def color_it(self):
        print('사각형 선택 ')
        self.color.fill_color()

class Circle(Shape):
    def __init__(self,color):
        super().__init__(color)
    
    def color_it(self):
        print('원 선택')
        self.color.fill_color()

###

blue_rectangle = Rectangle(BlueColor()) # 생성자 매개변수가 함수 
blue_rectangle.color_it()

red_circle = Circle(RedColor())
red_circle.color_it()