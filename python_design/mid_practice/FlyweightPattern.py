# 플라이웨이트 패턴
# 동일하거나 유사한 객체들 사이에 가능한 많은 데이터를 서로 공유하며
# 메모리 사용량을 최소화하는 패턴

# 공유되는 많은 객체의 수를 줄여서 메모리 사용량을 줄여주는 패턴
# 특정 클래스의 인스턴스 한 개만 가지고 여러 개의 가상 인스턴스를 제공

import random
from abc import * 

class Shape(metaclass = ABCMeta):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self,x,y,radius,bg_image):
        self.x = x
        self.y = y
        self.radius = radius
        self.bg_image = bg_image

    def draw(self):
        print(self.x, ' ' ,self.y, ' ', self.radius, ' ',self.bg_image.filename)


class Image:
    def __init__(self,filename):
        self.filename = filename
        print('이미지 로드 ',filename)

class ShapeFactory:
    bg_images = {}

    @classmethod
    def get_circle(cls,x,y,radius,bg_image_filename):
        bg_image = cls.bg_images.get(bg_image_filename,None)
        if bg_image is None:
            bg_image = Image(bg_image_filename)
            cls.bg_images[bg_image_filename] = bg_image

        return Circle(x,y,radius,bg_image)

bg_image_filenames = ['flower.png','butterfly.png']

circles = []
for i in range(10):
    x = random.randint(0,100)
    y = random.randint(0,100)
    radius = random.randint(1,100)
    bg_image_filename = bg_image_filenames[radius % len(bg_image_filenames)] #random

    circle = ShapeFactory.get_circle(x,y,radius,bg_image_filename)
    circles.append(circle)

for circle in circles:
    circle.draw()