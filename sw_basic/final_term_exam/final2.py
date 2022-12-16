가변 길이 인수
/ 왼쪽은 위치 전용 
/ 오른쪽은 둘다 허용 
* 왼쪽은 둘다 허용
* 오른쪽은 키워드 전용

list_a = list(filter(lambda a:a%2==1,range(11)))
list_b = filter(lambda a : a > 5, x)

infile = open("test.txt","r")
for line in infile:
    line = line.rstrip() #오른쪽 공백 문자를 제거
    print(line)
infile.close()
my_list = [12,3213,321,3,21,312]
result = list(filter(lambda x : (x%13==0),my_list))

result = list(map(lambda x:2**x,range(10)))

repr()에 의해 호출 된 인스턴스를 재 생성하는데 
사용할 수 있는 공식 문자열(formal string)을 리턴

print(a) # repr 호출
print(a[0]) # str 호출

#iter
class MultipleOfN:
    def __init__(self,n,stop):
        self.n = n
        self.stop = stop
        self.current = 0

def __iter__(self):
    return self

def __next__(self):
    num = self.current + self.n
    if num > self.stop:
        raise StopIteration
    else:
        self.current = num 
        return self.current

class PowTwo:
    def __init__(self,max=0):
        self.max = max
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n <=self.max:
            result = 2 ** self.n
            self.n +=1
            return result
        else :
            raise StopIteration

a = PowTwo(4)
i = iter(a)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

for i in PowTwo(4):
    print(i)

#gene 
def MultipleOfN(n,stop):
    num = n 
    while num <= stop:
        yield num
        num += n 

def MultipleOfN2(n,stop):
    num = n
    while n<=stop:
        yield n
        n += n 

for i in MultipleOfN(3,40):
    print(i,end=' ')


gy iinS in5r  lfl