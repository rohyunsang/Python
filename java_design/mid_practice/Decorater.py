# Decorater : 이미 만들어져 있는 기존의 코드를 수정하지 않고도, wrapper 함수를 이용해서
# 여러가지 기능을 추가할 수 있음

def trace(func):
    def wrapper():
        print(func.__name__,'함수 시작')
        func()
        print(func.__name__,'함수 끝')
    return wrapper # not wrapper() 파이썬에서 func return 할때 () 붙이지 않는다.

def hello():
    print('hello')

def world():
    print('world')

trace_hello = trace(hello)
trace_world = trace(world)

trace_hello()
trace_world()

