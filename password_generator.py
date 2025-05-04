import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
          'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
          'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols = ['+', '-', '*', '/', '%', '=', '==', '!=', '<', '>', '<=', '>=',
    '(', ')', '{', '}', '[', ']', ';', ':', ',', '.', '!', '&', '|',
    '^', '~', '?', '#', '@', '\\', '"', "'", '`']
hold=[]
l=int(input("How many letters you want in your password ==> "))
n=int(input("How many numbers you want in your password ==> "))
s=int(input("How many symbols you want in your password ==> "))
for i in range(0,l):
    hold.append(random.choice(letters))
for j in range(0,n):
    hold.append(random.choice(numbers))
for k in range(0,s):
    hold.append(random.choice(symbols))
random.shuffle(hold)
password=""
for i in range(0,len(hold)):
    password+=hold[i]
print(f"Your password is ==> {password}")


