two_digit_number=input("input 2 digit number\n")

print(int(two_digit_number[0])+int(two_digit_number[1]))

#-------------------------------------------------------------

print(3 * (3 + 3) / 3 - 3)

#-----------------------------------------------------------

height=input("input your height in m:\n")
weight=input("input your weight in kg:\n")

bmi=float(weight)/(float(height)**2)

print(int(bmi))

#---------------------------------------------------------------

age=input("input your age:\n")

year_total=90

day=(90-int(age))*365
months=(90-int(age))*12
weeks=(90-int(age))*52

print(f"you have {day}, {weeks}  weeks and {months} months left")

#------------------------------------------------------------------

print("welcome to the tip calculator")

bill=input("total bill?\n")
porcentage=input("porcentage tip to give?\n")
people=input("many people to split bill?\n")

give=round((float(bill)*(float(porcentage)/100))/int(people),2)

print(f"each person should pay: {give}")