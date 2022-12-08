python Call-by-object

가변 길이 인수 
일부 매개변수를 위치 전용으로 지정 : 슬래시(/) 왼쪽의 모든 매개변수는 위치 인자로 지정되어야 함
-> 키워드 인수로 지정할 수 없음을 의미
* 오른쪽의 모든 매개변수는 키워드 인자로 지정 

def f(x,y /z): # x, y는 위치 전용, z는 둘다 허용
    print(f'x: {x}, y: {y},z:{z}')

f(1,2,3)
f(1,2,z=3)
f(x=1,y=2,z=3) #error

def f2(x,/,y,*,z): # x: 위치전용, y: 둘다 허용, z : 키워드 전용 
    print(f'x: {x}, y: {y}, z: {z}')


그러니까  /  * 이거 2개 있으면
def(x, y, z, /, a, b, c, *, p, q, r):
    x y z 는 위치 전용 a b c 는 둘다 허용 p q r 은 키워드 전용


def add(a, b):
    return a + b
x = add(10,20)

x = (lambda a, b : a + b)(10,20)

list_a = list(filter(lambda a: a % 2 == 1, range(11)))
print(list_a) # [1,3,5,7,9]

list_b = filter(lambda a : a > 5, x)

class student:

    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.id = "32181395"

    def __str__(self):
        return 'name {0} number {1} id {2}'.format(self.name,self.number,self.id)


a = student("노윤상",'01039489077')
print(a)

infile = open("test.txt","r")
for line in infile :
    line = line.rstrip() #오른쪽 공백 문자를 제거
    print(line)
infile.close()

infile = open("test.txt","r")
line = infile.readline()
while line != "":
    print(line)
    line = infile.readline()
infile.close()

outfile = open("phones.txt","a") # type a

outfile.write("노윤상 010-3948-9077")
outfile.close()

my_list = [12,65,54,39,102,339,221]
result = list(filter(lambda x : (x%13 == 0),my_list))
print(result)

term = 10 
result = list(map(lambda x: 2**x,range(term))
print("the total terms are",term)
for i in range(term):
    print("2 raised to power ",i,"is",result[i])

repr()에 의해 호출 된 인스턴스를 재 생성하는 데
사용할 수 있는 공식 문자열(formal string)을 리턴
__str__() : For str(), print(), format() built-in function 객체를 문자열화
class DKU:
    def __repr__(self):
        return 'DKU()'

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

#gene
def MultipleOfN(n,stop):
    num = n 
    while num <= stop:
        yield num 
        num += n

g = MutipleOfN(4,30)
for i in g:
    print( i ,end='')
print()
for i in MutipleOfN(3,40):
    print(i,end='')