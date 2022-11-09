def addNumber(fixedNum):
    #This is the outer enclosing function

    def add(number):
        #This is the nested function
        return fixedNum + number
    return add

func = addNumber(10)
print(func(20))

def has_permission(page):

    def inner(username):
        if(username == 'Admin'):
            print(username,' does have access to Admin Area')
        else:
            print('TestUser does NOT have access to Admin Area')
        return page + username
    return inner

func = has_permission('Admin Area')
print(func)