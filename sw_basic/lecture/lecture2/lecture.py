

t = tuple('dankook')
t2 = tuple([1,2,3,4,5])

t = tuple(range(10)) #iterator object 

print(t)

# t[0] = 100 tuple object does not support item assignment 

a = (1,2,[3,4,5]) # can fix list in tuple 
a[2][0] = 10
print (a)
a[2].append(1000)
print (a)

b = (1,2,[])
print(b)

# a2 = tuple('roh')
# print(globals())
# del a2
# print(globals())

x,y,z = 1,2,3
print(x,y,z)

p = 10
q = 20
print(p,q)
p,q = q,p
print(p,q)

a = (1,2,3)
b = (*a,5,6,7) # *a is unpacking a 
print(b)

my = tuple('apple')
print(my)
print(my.index('p',2))

# pass cmp in tuple 

# python return 은 하나의 객체만 리턴된다. tuple 로 packing 되어서 return 

# f - string 
# 문자열 맨 앞에 f를 붙이고, 출력할 변수, 값을 중괄호 안에 넣습니다.
s = 'coffee'
n = 5
result1 = f'저는 {s}를 좋아합니다. 하루 {n}잔 마셔요.'
print(result1)
print(f'{s}는 {n}00원')

a = (1,2,3,9)
*x,y,z = a # *x : x is list 
print (x,y,z)

# set : 집합 set은 임의대로 정렬, 자동정렬은 아니다.

s = {53,5151,515,153,53,6}
s.add(10)
print(s)
print(sorted(s))
print(s)

A = {1,2,3}
B = {3,4,5}
# | , & , - , ^ , <= 5 methods 

# dictionary    

d = {'a':'1' ,'b':'2'}
print(d)

f = dict(a=1,b=2,c=3)
print(f)