
rows ='ABCDEFGHI'
cols ='123456789'
result = ["".join([x,y]) for x in rows for y in cols]

print(len(result))

for x in result:
    print(x)
