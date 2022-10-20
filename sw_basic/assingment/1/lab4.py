mydict = dict({'cat':12,'dog':6,'elephant':23})
#print(mydict)

def update():
    key_tmp = input()
    value_tmp = input()
    mydict[key_tmp] = value_tmp

for i in range(3):
    update()

for key, value in list(mydict.items()): 
    if int(value) < 10:
        del mydict[key]

mydict = dict(sorted(mydict.items(), reverse = True))
for key,value in list(mydict.items()):
    print(str(key),'는',mydict[key],'마리') 




