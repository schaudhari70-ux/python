def factorial(x):
    '''this is use to find the factoial of a integer'''
    if x==0 or x==1:
      return 1
    else:
       return x * factorial(x-1)
print(factorial.__doc__)
print("this for 0",factorial(0))
print("this is for 1",factorial(1))
print("this is for 2",factorial(2))
print("this is for 5",factorial(5))
print("this is for 10",factorial(10))