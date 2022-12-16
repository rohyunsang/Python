for i in range(3):
    print(i)

class MyIter:
    def __init__(self,end):
        self.current = 0 
        self.end = end

    def __iter__(self):
        return self

    def __next__(self): # python __next__ function must be return value variable
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else :
            raise StopIteration

for i in MyIter(3):
    print(i)

def generator_a():
    yield 2
    yield 3 
    yield 4

for i in generator_a():
    print(i)
# yield 로 지정한 값이 __next__ 함수의 반환값으로 나옴 


def generator_c(end):
    n = 0
    while n < end:
        yield n 
        n += 1

for i in generator_c(3):
    print(i)


def generator_d():
    x = [1,2,3]
    for i in x :
        yield i

for i in generator_d():
    print(i)

def generator_e():
    x = [1,2,3]
    yield from x

for i in generator_e():
    print(i)
ee = generator_e()
next(ee)

# yield from 반복가능한객체
# yield form 이터레이터
# yield form 제네레이터객체

