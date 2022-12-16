# 옵저버 패턴 (Observer Pattern)

# 한 객체의 상태가 변하면 그 상태에 의존하는 여러 객체들에게 상태의 변화를 알려주는 패턴
# Subject 와 Observer 가 존재 
from abc import *
import random
class Subject():
    _state = None
    _observers = []

    def attach(self, observer):
        print("Subject: Attached an observer")
        self._observers.append(observer)

    def detach(self,observer):
        self._observers.remove(observer)

    def  notify(self):
        print("Subject : Notifying observers...")
        for observer in self._observers:
            observer.update(self)
    
    def some_logic(self):
        print("Subject: do something important")
        self._state = random.randrange(0,10)

        print(f"Subject: My state has {self._state}")
        self.notify()

class Observer(ABC):
    @abstractmethod
    def update(self,subject):
        pass

class ConcreteObserverA(Observer):
    def update(self,subject):
        if subject._state < 5:
            print(" ObserverA : Reacted to the event")

class ConcreteObserverB(Observer):
    def update(self,subject):
        if subject._state >= 5:
            print(" Observer : Reacted to the evnet")


subject = Subject()

observer_a = ConcreteObserverA()
subject.attach(observer_a)

observer_b = ConcreteObserverB()
subject.attach(observer_b)

subject.some_logic()
subject.some_logic()

subject.detach(observer_a)
subject.some_logic()

# 옵저버 패턴
# -특징 subject 입장에서 옵저버에 대해서 잘 모름 (느슨한 결합)
# subject 는 Observer 추상클래스 (인스턴스)를 구현한 객체는 옵저버로 등록 가능
# S - O 사이 느슨한 결합으로 인해 서로 독립적으로 사용 가능하고 변경되어도 서로 영향을 미치지 않음
# 이벤트 핸들러, 구독 시스템 .. 등등 예제 




