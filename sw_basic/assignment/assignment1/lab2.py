a = tuple(i for i in range(2,102) if i % 2 == 0)

for i in range (0, 10):
    for j in range(0,5):
        tmp = i*5 + j
        print(a[tmp],end=" ")
    print()
    