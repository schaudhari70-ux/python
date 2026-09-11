totalchorce=4
origanlchorce=totalchorce
print(f"today you have to compete{origanlchorce}today ")
competecountdown=0
chorcenumber=1
while chorcenumber <=1:
    if chorcenumber==1: chorcenext="make your bed"
    elif chorcenumber==2:chorcenext="feed the pet"
    elif chorcenumber==3:chorcenext="put the trash out"
    else: chorcenext="wash your dish"
    answer=input(f"have you competed the {chorcenext} yes or no")
    if answer=="yes":
       competecountdown +=1
       chorcenumber +=1
       print("great work move on ")
    else :
        print("finsh it cheack again")
        print("remmaning chorce=",competecountdown-totalchorce)
print("great now compete your cheaklist")
print("now letssaferylook at infinate loop")
test_value=0
safety_counter=0
while test_value <=0:

    print("this condintio never ends")
    safety_counter +=1
    if safety_counter==3:
     print("stoping here a infinate loop never stops")
     break
print("summary ")
print("chorce assgined", totalchorce)
print("chorce completed", competecountdown)
print("left",totalchorce-competecountdown)