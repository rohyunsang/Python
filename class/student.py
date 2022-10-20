class Student:
    def __init__(self,name=None,age = 0):
        self.name = names
        self.age = age

obj = Student("Hong",20)
obj.age = 21
print(obj.age)

#information hiding 

class StudentTwo:
    def __init__(self,name=None,age = 0):
        self.__name = name
        self.__age = age

obj2 = Student()
print(obj2.__age)