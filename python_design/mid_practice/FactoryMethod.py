# product의 세부 종류인 concreteProduct 객체의 생성을 
# Creator의 자식 클래스인 concreteCreator에서 담당

from abc import *
from dataclasses import make_dataclass

#Product

class Mouse(metaclass = ABCMeta):
    @abstractmethod
    def click_left(self):
        pass

    @abstractmethod
    def click_right(self):
        pass

# concreteProduct 

class G102(Mouse):
    def click_left(self):
        print('click right g102')

    def click_right(self):
        print('click left g102')

class MagicMouse(Mouse):
    def click_left(self):
        print('click left MagicMouse')
   
    def click_right(self):
        print('click right MagicMouse')

# Factory
class MouseFactory(metaclass = ABCMeta):
    @abstractmethod
    def createMouse(self):
        pass

class LogiMouseFactory(MouseFactory):
    def createMouse(self):
        return G102()

class AppleMouseFactory(MouseFactory):
    def createMouse(self):
        return MagicMouse()

# client

class Client():
    def use(self,company):
        if company == 'logi':
            factory = LogiMouseFactory()
        elif company =='apple':
            factory = AppleMouseFactory()
        else :
            return

        myMouse = factory.createMouse()
        myMouse.click_left()

client_a = Client()
client_a.use('logi')
client_a.use('apple')


        