print("==========================atm ==================================")
total_100=total_50=total_20=total_10=total_5=0
customer_served=0
total_dispered=0

serving=True
while serving:
    name=input("whats your name")
    amount=input(f"hi {name} what is your money needed")
    if amount <=0:
     print ("positive amount needed")
     continue
    print(f"f/n diserpering amout{amount} for {name}")
    remaining=amount
    idx=1
    while idx<=6
        if idx==1:value=100
        elif idx==2:value=50
        elif idx==3:value=20
        elif idx==4:value=10
        elif idx==5: value=5
        else:value=1
        count=remaining // value
        if count>0:
           print(f"{count}x {value} -unit notes(s)= {count* value}")
           remaining=count* value
           

