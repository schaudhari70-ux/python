print("this is a calculaterfor the owner ")
price=float(input("type the price"))
supplies=int(input("type of the number of the supplies"))
def calulate_total(price,supplies):
    total=price*supplies
    return total
total1=calulate_total(price,supplies)
total3=round(total1)
paid=float(input("the price paid by the customer"))
def calculate_change(total3,paid):
    change=total3-paid
    return change
change1=calculate_change( total3,paid)
change2=round(change1)
print("artsupplies result")
print(price,"this is the price")
print(supplies,"supplies number")
print(total3,"total")
print(paid,"paid information")
print(change2,"change")
print("========================")