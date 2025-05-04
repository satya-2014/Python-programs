print("Welcome to Python Pizza Delivery")
size=input("What size of pizza, do you want S, M or L => ")
peperoni=input("Do you want peperoni on your pizza? Y or N => ")
extra_cheese=input("Do you want extra cheese? Y or N => ")
small=15
medium=20
large=25
bill=0
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25
else:
    print("Invalid choice selected")
if peperoni=="Y":
    if size=="S":
        bill+=2;
    else:
        bill+=3;
if extra_cheese=="Y":
        bill+=1

print(f"Your final bill for pizza is => ${bill}")
    