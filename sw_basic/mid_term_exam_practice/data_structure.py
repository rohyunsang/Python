print('# problem 1')

s = tuple(range(2,102,2))

for i in s:
    print(i,end=' ')
    if i % 10 == 0:
        print() # enter key

print('# problem 2')

my = set()

for i in range(3):
    email = input('이메일 입력: ')
    my.update(email.split('@'))

print(my)

mydict = dict(cat = 12 , dog = 6, elephant = 23)
mydict.update(rabbit=10,monkey=30,bear=3)

for key, value in list(mydict.items()):
    if value < 10:
        del mydict[key]

for key in reversed(mydict):
    print(f'{key}는 {mydict[key]}마리')

team1 = {'Phill': {'age':24,'salary':3500}, 'Young':{'age':30,'salary':5500}} # dictionary
team2 = {'Phak':{'age':40,'salary':7000},'Piter':{'age':28,'salary':4200}} #dictionary
print(type(team1))
A = {**team1,**team2}  # unpacking 

print(A)

rows = 'ABCDEFGHI'
cols = '123456789'

result = [r + c for r in rows for c in cols]
print ('result 리스트의 항목의 개수 : ' ,len(result))
print(result[::5])