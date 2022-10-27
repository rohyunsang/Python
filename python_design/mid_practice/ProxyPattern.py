import time
from abc import *

# Subject
class Image(metaclass = ABCMeta):
    def __init__(self):
        self.filename = None

    @abstractmethod
    def display(self):
        pass

# Real Subject
class RealImage(Image):
    def __init__(self,filename):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print('loading',self.filename)
        time.sleep(3)

    def display(self):
        print('display',self.filename)

# Proxy
class ProxyImage(Image):
    def __init__(self,filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

proxy_image = ProxyImage('hello.png')

proxy_image.display()
