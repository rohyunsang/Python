def reduce(combiner,*vals,start = 0):
    accum = start
    for item in vals:
        accum = combiner(accum,item)
    return accum

print(reduce(lambda x,y:x*y,1,2,3,4,start=1))
print(reduce(lambda sos,n:sos + n**2,1,2,3,4))
print(reduce(lambda total, s: total + len(s),'hello','beautiful','world'))
print(reduce(lambda s,l:s &set(l),range(0,10),range(5,20),range(8,12),start = set(range(0,100))))