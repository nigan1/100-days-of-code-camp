import random


c=random.randint(100,200)
print(c)

d=random.uniform(1,10)
print(d)
#-------------------------------------------
test_seed=int(input("create a seed number:\n"))
random.seed(test_seed)

random_numb=random.randint(0,1)


if random_numb==1:
    print("Heads")
else:
    print("Tails")

#--------------------------------------------

test_seed=int(input("create a seed number:\n"))
random.seed(test_seed)

nameCsv=input("give me all the names:\n")
names=nameCsv.split(", ")

person=random.randint(0,len(names)-1)

print(f"{names[person]} is going to buy the meal today!")
#-------------------------------------------------------

row1=["0","0","0"]
row2=["0","0","0"]
row3=["0","0","0"]

map=[row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}\n")

position=input("where do you want to put the treasury?\n")

position1=int(position[0])-1
position2=int(position[1])-1

map[position2][position1]="X"

print(f"{row1}\n{row2}\n{row3}\n")
#-------------------------------------------------------

user=int(input("what do you choose? type 0 for rock, 1 for paper and 2 for scissors.\n"))


bot=random.randint(0,2)

if user==bot:
    print("draw")

elif user==0 and bot==1:
    print("you lose")

elif user==0 and bot==2:
    print("you win")

elif user==1 and bot==0:
    print("you win")

elif user==1 and bot==2:
    print("you lose")

elif user==2 and bot==0:
    print("you lose")

elif user==2 and bot==1:
    print("you win")

else:
    print("ha introducido numero invalido")