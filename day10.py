""" def format_name(name,last):
    f_name=name.capitalize()
    l_name=last.capitalize()

    return f"{f_name} {l_name}"

a=format_name("yusniel","abreu")

print(a)
#--------------------------------------
def is_leap(year):
    if year%4==0:
        if year%100:
            if year%400:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year,month):
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]

    if is_leap(year):
        month_days[1]=29

    day=month_days[month-1]

    return f"the month of the year {year} has {day} days"


year=int(input("enter a year:\n"))
month=int(input("enter a month:\n"))

days=days_in_month(year,month)
print(days) """
#--------------------------------------------------------
def add(num1,num2):
    return num1+num2

def rest(num1,num2):
    return num1-num2

def multi(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

operations={"+":add,"-":rest,"*":multi,"/":div}



def calculator():
    num1=float(input("what is the first number?:\n"))
    continu=True

    for oper in operations:
        print(oper)

    while continu:

        operation_symbol=input("pick an operation:\n")
        num2=float(input("what is the next number?:\n"))
        answer=operations[operation_symbol](num1,num2)
        print(f"{num1}{operation_symbol}{num2}={answer}")


        again=input("more operations? Y or N\n").lower()
        if again=="y":
            num1=answer
        else:
            continu=False
            calculator()

calculator()