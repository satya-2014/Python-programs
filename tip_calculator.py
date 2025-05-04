print("* Welcome to the tip calculator *")
bill=float(input("What was the total bill => "))
tip=int(input("How much tip you would like to give 10%, 12%, 15% => "))
split=int(input("How many people do you want to split the bill => "))
percent=tip/100
tot_bill=bill+ percent*bill
bill_per_person=tot_bill/split
print(f"Each person has to pay => ${round(bill_per_person,2)}")