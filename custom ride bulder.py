print("==================================")
print("=            rider picker        =")
print("==================================")
print("which option do you whant 1or 2"
     "1=bike 2=car" )
vehical=int(input("what is your chocie"))
if vehical ==  1:
    print("your choices are " \
    "1 =scooter" \
    "or 2=mountain bike")
    bike=int(input( 1 or 2)) 
    if bike==1:
     print("you selected a scooter")
     print(" speed=40km/h")
     print("best for city road")
    else:
       print("you selected a mountain bike")
       print("speed=40km")
       print("best for of road trails")
else:
    print("the chocis are " \
    "1= suv" \
    "2=sedan")
    car=int(input("which 1 or 2"))
    if car==1:
       print("you selected a suv")
       print("seats=7 passanger")
       print("best for of road trip")
    else:
       print("you selected a sedan")
       print("seat =5" \
       "best for family trips")
print("==============end===============")
      
