from tkinter import N


obj = ['even' if i % 2 == 0 else 'odd' for i in range(10)]
# even odd even odd even odd even odd even odd
print(obj)

obj = ['even' if i % 3 == 0 else 'odd' for i in range(10)]

print(obj)

#Python supports a conditional expression 

#if n >= 0 :
  #  param = n  
#else :
    #param = -n 

#param = n if n >= 0 else -n 

# two statement is equal 

int_data = [1,1,2,3,4,5]
square_data_set = {num * num for num in int_data}
print(square_data_set ) # this make templete by set data structure 

square_data_set = {num * num for num in int_data if num > 3}
print(square_data_set)
