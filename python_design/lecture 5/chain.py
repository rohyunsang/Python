from abc import *

class Handler(metaclass = ABCMeta):
    @abstractmethod
    def set_next(self,next):
        pass

    @abstractmethod
    def handle(self):
        pass

class AbstractHandler(Handler):

    _next_handler = None

    def set_next(self,handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handler(self,request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class MonkeyHandler(AbstractHandler):
    def handle(self,request):
        if request == "Banana":
            return "Monkey {}".format(request)
        else:
            return super().handle(request)