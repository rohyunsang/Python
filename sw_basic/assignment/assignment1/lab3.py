email = set()

for i in range(3):
    tmp = input().split('@')
    email.add(tmp[0])
    email.add(tmp[1]) 

print(email)