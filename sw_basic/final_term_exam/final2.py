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
