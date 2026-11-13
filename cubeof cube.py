def cube(number):
    return number*number*number
def of_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False
print(of_three(9))
print(of_three(4))