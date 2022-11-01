my_list = [12,65,54,39,102,309,221]

my_list = list(filter(lambda x : x % 13 == 0 ,my_list))


print('Multiple of 13 are',my_list)