# 생성자를 통해서 어떠한 값도 생성하지 않고 내부 클래스를 통해 생성하도록 하는 패턴 

class Student():
    def __init__(self, name, age, height = 184, weight = 87):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

s1 = Student (name = 'hel',age = 26) # KeyWord 인자
print(s1.age)