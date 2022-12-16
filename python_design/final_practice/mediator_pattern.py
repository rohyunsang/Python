# Mediator Pattern
# 중재자 패턴
# 클래스 간의 복잡한 관계들을 캡슐화하여 하나의 
# 클래스에서 관리하도록 처리하는 패턴
# 다수의 객체들 사이에 중재자를 추가 하여 중재자가 모든
# 객체들의 통신을 담당
# 각 객체들은 서로 알 필요가 없고 중재자 객체가 관리

# Mediator : Colleague 객체 간의 상호참조를 위한 인터페이스.
# 클라이언트 등록 , 실행 등의 메소드 정의

# Colleague 다른 Colleague와의 참조를 위한 추상클래스
# ConcreteMediatro : Mediator 구현 클래스.
# Colleague 간의 참조를 조정
# ConcreteColleague : Colleague 구현 클래스 Mediator를 통해 다른 Colleague와의 참조
from abc import *

class Mediator(ABC):
    @abstractmethod
    def add_user(self,user):
        pass

    @abstractmethod
    def delete_user(self,user):
        pass

    @abstractmethod
    def send_message(self,msg,user):
        pass

class ConcreteMediator(Mediator):
    def __init__(self):
        self.users = []
    def add_user(self, *user):
        self.users.extend(users)

    def delete_user(self,user):
        self.users.remove(user)
    
    def send_message(self, msg, user):
        for _user in self.users:
            if _user == user:
                continue
            _user.receive(msg)

class Coleague(ABC):
    def __init__(self,_mediator,name):
        self.mediator = _mediator
        self.name = name

    @abstractmethod
    def send(self,msg):
        pass
    @abstractmethod
    def receive(self,msg):
        pass

class ConcreteColleague(Colleague):
    def __init__(self,mediator,name):
        super().__init__(mediator,name)
    
    def send(self,msg):
        print(f'{self.name} sending message = {msg}')
        self.mediator.send_message(msg,self)

    def receive(self,msg):
        print(f'{self.name} receiving mesaage={msg}')


mediator = ConcreteMediator()
user1 = ConcreteColleague(mediator,'lee')
user2 = ConcreteColleague(mediator,'lee')
user3 = ConcreteColleague(mediator,'lee')
user4 = ConcreteColleague(mediator,'lee')
mediator.add_user(user1,user2,user3,user4)
user1.send("안녕하세요")

mediator.delete_user(user4)
user2.send("Kevin 없지?")