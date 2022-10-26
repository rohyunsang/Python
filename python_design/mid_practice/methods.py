class MethodTypes:
    firstname = "Yun Sang"

    def instanceMethod(self):
        self.lastname = "Roh"
        print(self.firstname, end=' ')
        print(self.lastname) # we use value name self.lastname not a lastname

    @classmethod
    def classMethod(cls):
        cls.name = "Lee"
        print(cls.name)

    @staticmethod
    def staticMethod(): # static method dont need self keyword
        print("this is staticMethod")

m = MethodTypes()
m.instanceMethod()
MethodTypes.classMethod()
MethodTypes.staticMethod()