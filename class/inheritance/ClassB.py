import ClassA

class ClassB(ClassA):

    name = " "


    def __init__(self,name):
        self.name = name

b = ClassB("hello")
b.show_info()