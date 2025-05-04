import random
x=random.randint(30,50)
print("The random number is => ",x)

#It will produce between zero and one, inclusize 0 but not 1 
y=random.random()
print("Another random float number is => ",y)

#It will produce between 30 and 50, between that excluding 30 & 50 
z=random.uniform(30,50)
print(f"Another random float value => {z}")