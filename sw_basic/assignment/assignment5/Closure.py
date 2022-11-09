def has_permission(page):

    def inner(username):
        if(username == 'Admin'):
            print(username,' does have access to Admin Area')
        else:
            print('TestUser does NOT have access to Admin Area')
        return username
    return inner

func = has_permission('Admin Area')
print(func('Admin'))

func2 = has_permission('32181395 Area')
print(func('32181395'))