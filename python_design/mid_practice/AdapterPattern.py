from abc import *

class Fighter(metaclass=ABCMeta):
    @abstractmethod
    def attack(self): pass

    @abstractmethod
    def defend(self): pass

    @abstractmethod
    def escape(self): pass

class Warrior(Fighter):
    def attack(self):
        print('칼을 휘두르다')

    def defend(self):
        print('방패를 들어올리다.')

    def escape(self):
        print('뒤로 물러난다.')


class WizardAdapter(Fighter):
    def __init__(self,wizard):
        self.wizard = wizard
    
    def attack(self):
        self.wizard.shot_fire_ball()

    def defend(self):
        self.wizard.shield()

    def escape(self):
        self.wizard.portal()


class Wizard:
    def shot_fire_ball(self):
        print("빠이어뽈 발싸!!")

    def shield(self):
        print('주변에 보호막 씌우기')

    def portal(self):
        print('포탈 열고 이동')

wizard = WizardAdapter(Wizard())
wizard.attack()
wizard.defend()
wizard.escape()
