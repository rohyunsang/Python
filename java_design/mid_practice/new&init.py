class NewExam:
    def __init__(self, x = 0, y = 0):
        print('__init__Method')
        self.x = x 
        self.y = y

    def __new__(cls,*args):
        print("__new__Method")
        print(cls)
        print(args)
        obj = super().__new__(cls)
        return obj 

a = NewExam(3,4)

# first we check init Vs new 
# if we such like instanciate object by __init__  
# object name = class name(initialize value list)
# compiler show little magic he auto call __new__ Method 
# so we checking Console : 

# __new__Method
# <class '__main__.NewExam'>
# (3,4)
# __init__Method