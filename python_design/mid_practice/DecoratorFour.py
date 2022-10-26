def trace(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        print('name = {0}, args = {1} , kwargs = {2}, return ={3}'.format(func.__name__,args,kwargs,r))
        return r
    return wrapper

@trace
def get_max(*args):
    return max(args)

@trace
def get_min(**kwargs):
    return min(kwargs.values())

print(get_max(10,20)) # args 
print(get_min(x = 10 , y = 20, z =30)) # kwargs 
# x = 10 y = 20 z = 30 이런 값들 받음 kwargs가 