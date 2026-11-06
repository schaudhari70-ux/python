def greeting_user():
    print("lemonde stand for you")
    print("fresh for you")
    greeting_user()
price_percup=float(input("give the price per cupto owner"))
cupssold=int(input("give the cups sold"))
def calculating_total(price_percup,cupssold):
    total=price_percup*cupssold
    return total
totalwithoutround=calculating_total(price_percup,cupssold)
total=round(totalwithoutround)
print("total",total)
paid=float(input("the price paid from the user"))
def calculate_change(total,paid):
    change=total-paid
    return change
change1=calculate_change(total,paid)
changereal=round(change1)
print("the change is here",changereal)
if cupssold >=5:
    print("big oder")
else:
    print("thankyou")
print("")
print("lemonde reipt")
print ("total",total)
print ("change",changereal)
print ("paid",paid)
print("price",price_percup)
print("number of cups",cupssold)