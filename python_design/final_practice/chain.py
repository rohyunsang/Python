# 책임 연쇄 패턴 (Chain Of Responsibility)

# 요청을 처리하는 동일 인터페이스 객체들을 체인 형태로 연결해놓은 패턴
# 앞의 객체의 요청을 처리하지 못할 경우, 같은 인터페이스의 다른 객체에게 해당 요청을 전달
# 다양한 처리 방식을 서로 연결하여 체인으로 형성

from abc import *
class Handler(metaclass = ABCMeta):
    @abstractmethod
    def set_next(self,handler):
        pass

    @abstractmethod
    def handle(self,request):
        pass

class AbstractHandler(Handler):

    _next_handler = None 

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self,request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None 

class MonkeyHandler(AbstractHandler):
    def handle(self, request):
        if request == "Banana":
            return "Monkey: I'll eat the {}".format(request)
        else:
            return super().handle(request)

class SquirrelHandler(AbstractHandler):
    def handle(self,request):
        if request =="Nut":
            return "squirrel {} ".format(request)
        else:
            return super().handle(request)

class DogHandler(AbstractHandler):
    def handle(self, request):
        if request =="MeatBall":
            return f"Dog: i {request}"
        else:
            return super().handle(request)


monkey = MonkeyHandler()
squ = SquirrelHandler()
dog = DogHandler()

monkey.set_next(squ)._next_handler(dog)
monkey.handle('Nut')
monkey.handle('MeatBall')
print(squ.handle('banana'))
