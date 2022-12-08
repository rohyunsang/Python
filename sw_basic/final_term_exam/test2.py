def MultipleOfN(n,stop):
    num = n 
    while num <= stop:
        yield num 
        num += n

g = MultipleOfN(2,30)
for i in g:
    print( i ,end=' ')
print()
for i in MultipleOfN(2,40):
    print(i,end=' ')