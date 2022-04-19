studens_heigts=input("input a list of student heighs \n").split()

for n in range(0,len(studens_heigts)):
    studens_heigts[n]=int(studens_heigts[n])

sum=0
count=0


for element in studens_heigts:
    sum+=element
    count+=1

avg=round(sum/count)
print(f"average is {avg}, sum is {sum} and {count} elements in list")

#------------------------------------------------------------------------

students_scores=input("input a list of scores\n").split()

for n in range(0,len(students_scores)):
    students_scores[n]=int(students_scores[n])

hight_score=0

for element in students_scores:
    if element>hight_score:
        hight_score=element

print(f"hight score is {hight_score}")
#---------------------------------------------------------------------------
total=0
for number in range(0,101,2):
    total+=number
print(total)
#----------------------------------------------------------------------

for number in range(1,101):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%5==0:
        print("Buzz")
    elif number%3==0:
        print("Fizz")
    else:
        print(number)
#---------------------------------------------------------------------------
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pass_select=[]

for i in range(1,nr_letters+1):
    letter=random.choice(letters)
    pass_select.append(letter)
    
for i in range(1,nr_symbols+1):
    symbol=random.choice(symbols)
    pass_select.append(symbol)

for i in range(1,nr_numbers+1):
    number=random.choice(numbers)
    pass_select.append(number)


random.shuffle(pass_select)


str="".join(pass_select)

print(f"your password is:  {str}")