scores = [32,56,64,72,12,37,58,77,59,69]

for i in range(10):
    scores.append(int(input("성적을 입력하시오")))
print(scores)

STUDENT = 5
scores = []
scoreSum = 0

for i in range(STUDENT):
    value = int(input("성적을 입력하시오 : "))
    scores.append(value)
    scoreSum += value


highScoreStudent = 0
for i in  range(len(scores)):
    if scores[i] >= 80:
        highScoreStudent += 1

flist = ["apple","banana","tomato"]
print(len(flist))

# len() // + // * // in // not in // [] // min() // max() // for loop

# whats mean indexing => 리스트에서 하나의 요소를 인덱스 연산자를 통하여 참조 하는것을 의미한다 
# 인덱스는 정수이며 항상0에서부터 시작한다는 것을 잊으면 안된다 

#index out of range in python => list index out of range 

squares = [0,1,4,9,16,25,36,49]
squares[3:6] # slicing은 새로운 복사본을 반환한다. 

a = ["hello","hi"]
b = ["노윤상","이소은"]
c = a + b
print (c)

# erase elements => pop(), remove() 
c.remove("hello")

# list sort, sorted
# sort() 메소드는 리스트를 제자리에서 정렬한다. 따라서 sort()가 호출되면 원본 리스트가 변경된다. 아래의 코드에서 리스트a는 정렬된 상태로 변경된다.

# sorted() : 원본을 유지하고 새로이 정렬된 리스트를 원한다면 내장 함수인 sorted()를 사용하는 것이 좋다. 
# list.sort(), sorted()는 모두 부울형의 reverse 매개 변수를 가진다. 


a = [3,2,1,5,4]
a.sort() #console  1 2 3 4 5 