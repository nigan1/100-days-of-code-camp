number=int(input("insert the number:\n"))

if number%2==0:
    print("this is an even number.")
else:
    print("this is an odd number")

#------------------------------------------------------

height=input("input your height in m:\n")
weight=input("input your weight in kg:\n")

bmi=float(weight)/(float(height)**2)
print(bmi)

if bmi <18.5:
    print("underweight")
elif bmi<25:
    print("normal weight")
elif bmi<30:
    print("overweight")
elif bmi<35:
    print("obese")
else:
    ("clinical obese")
#-------------------------------------------------------------

year=int(input("insert year:\n"))

if year%4==0:
    print("leap!")
    if year%100==0:
        print("leap!")
        if year%400==0:
            print("leap!")
        else:
            print("no leap!")
    else:
        print("no leap!")
else:
    print("no leap!")

#---------------------------------------------
print("pizza delivery")

size=input("whay size pizza do you want? S, M, or L\n")
add_pepperoni=input("do you want pepperoni? Y or N\n")
extra_cheese=input("do you want extra cheese? Y or N\n")

bill=0

if size=="S":
    bill+=15
    if add_pepperoni=="Y":
        bill+=2
elif size=="M":
    bill+=20
    if add_pepperoni=="Y":
        bill+=3
else:
    bill+=25
    if add_pepperoni=="Y":
        bill+=3


if extra_cheese=="Y":
    bill+=1

print(bill)
#---------------------------------------------
print("love calculator")

name1=input("What is your name?\n")
name2=input("what is their name?\n")

name_together=name1+name2.lower()


true="true"
love="love"

score_true=0
score_love=0

for character in true:
    score_true=score_true+name_together.count(character)

for character in love:
    score_love=score_love+name_together.count(character)

score=str(score_true)+str(score_love)

if int(score)<=10 or int(score)>=90:
    print(f"your score is {score},you go together like coke and mentos.")
elif int(score)>=40 or int(score)<=50:
    print(f"your score is {score},you are alright together.")
else:
    print(f"your score is {score}")

print(score)
#-----------------------------------------------------------------------


print("welcome to treasure island.Your mission is to find the treasure.")

side=input("left or right?\n").lower()

if side=="left":
    cross=input("swim or wait?\n").lower()

    if cross=="wait":
        door=input("which door? RED, BLUE or YELLOW\n").lower()

        if door=="yellow":
            print("YOU WIN!")

        else:
            print("game over")
    else:
        print("game over")
else:
    print("game over")

