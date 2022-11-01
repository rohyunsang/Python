print(sorted([-3,5,-1,0])) 
#[-3, -1, 0, 5]
print(sorted([-3,5,-1,0],key=abs))
#[0, -1, -3, 5]
print(sorted(['ingesting','cakes','is','fun']))
#['cakes', 'fun', 'ingesting', 'is']
print(sorted(['ingesting','cakes','is','fun'],key=lambda s : len(s)))
#['is', 'fun', 'cakes', 'ingesting']
print(sorted(['ingesting','cakes','is','fun'],key= len))
#['is', 'fun', 'cakes', 'ingesting']
print(sorted(['ingesting','cakes','is','fun'],key=lambda s : s.count('i'),reverse=True))
#['ingesting', 'is', 'cakes', 'fun']