import random
user=int(input("Choose one - For Rock(0), Paper(1), Scissor(2) => "))
data=["rock","paper","scissor"]
computer=random.randint(0,2)
print(f"You choose ==> {data[user]}")
print(f"Computer choose ==> {data[computer]}")

if data[user]==data[computer]:
    print("You Won")
else:
    print("You Lost")


