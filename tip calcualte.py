tipper=20
bill=150
def totalcaulater(bill,tipper):
    total=bill*(1+0.1*tipper)
    totalr=round(total,2)
    print("please pay",total)



totalcaulater(150,20)