def decorator1(func):
    def wrap():
        print(func.__name__,'decorator1')
        func()
    return wrap 

def decorator2(func):
    def wrap():
        print(func.__name__,'decorator2')
        func()
    return wrap

@decorator1
@decorator2
def hello():
    print ('hello')

hello()


