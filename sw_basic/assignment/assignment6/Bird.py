class Bird:
    def __init__(self,name,age):
        self.name = name
        self.age = age 

    def __repr__(self):
        return 'Bird {0}, {1}'.format(self.name,self.age)

    def fly(self):
        print('새는 날수 있다.')

class Parrot(Bird):
    def __init__(self,words):
        super().__init__('루루',3)
        self.words = words

    def __repr__(self):
        return 'Parrot({0}, {1}, {2})'.format(self.name,self.age,self.words)
    
    def fly(self):
        print('앵무새는 말도하고 날 수 있어.')

class Penguin(Bird):
    def __init__(self,divingTime):
        super().__init__('치치',1)
        self.divingTime = divingTime

    def __repr__(self):
        return 'Penguin({0}, {1}, {2})'.format(self.name,self.age,self.divingTime)
    
    def fly(self):
        print('펭귄은 수영 잘해 근데 날 수 없어')

