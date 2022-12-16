def func(arg1 : str, arg2 : int, arg3: 'this is annotation') -> bool:
    print('arg1 = {}'.format(arg1))
    print('arg2 = {}'.format(arg2))
    print('arg3 = {}'.format(arg3))

    return 'True'

result = func('test',3,0.56)
print(type(result))
print('result = {}'.format(result))
