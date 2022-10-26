def trace(func):
    def wrapper(a,b):
        r = func(a,b)
        print('{0} {1} {2} {3}'.format(func.__name__,a,b,r))
        return r
    return wrapper


@trace
def add(a,b):
    return a + b

print(add(10,20))


