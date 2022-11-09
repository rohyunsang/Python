def MultipleOfNGen(n,stop):
    multiples = []
    for i in range(n,stop+1,n):
            multiples.append(i)
    yield from multiples

for i in MultipleOfNGen(2,10):
    print(i,end=" ")