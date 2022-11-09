phrase = input('문자열을 입력하시오 : ')


print(phrase.upper())
acronym = ""
for word in phrase.upper().split():
    acronym +=word[0]

print(acronym)

# 예제가 잘못됨 input값을 Nato Atlantic이 아니라
#                       noto atlantic이어야함


