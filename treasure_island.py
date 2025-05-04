print("Welcome to treasure island game.")
print("Your mission is to find the treasure.")
direction=input("You want to go left or right ==> ").lower()
if direction =="left":
    print("Nice! You have decided to go left.")
    decide=input("You want to swim or wait ==> ").lower()
    if decide=="wait":
        print("Nice! you have decided to wait.")
        color=input("Choose between Red, blue, yellow ==> ").lower()
        if color=="yellow":
            print("You Win")
        else:
            print("Gave OVer")
    else:
        print("Sorry! You Swimed, so Game Over")
else:
    print("Sorry! you fallen in a hole. Gave Over")