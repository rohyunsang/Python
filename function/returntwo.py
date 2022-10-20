from termios import CR0


def cal(a,b):
    result1 = a + b
    result2 = a * b
    return result1, result2


c, d = cal(3,4)

print(c) #console 7
print(d) #console 12


