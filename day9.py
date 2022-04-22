student_scores={"harry":81,"Ron":78,"Hermione":99,"Draco":74,"Neville":62}

student_grades={}

for key in student_scores:
    
    if student_scores[key]<71:
        student_grades[key]="Fail"
    elif student_scores[key]<81:
        student_grades[key]="Acceptable"
    elif student_scores[key]<91:
        student_grades[key]="Exceeds  Expectations"
    else:
        student_grades[key]="Outstanding"
    
print(student_grades)

#------------------------------------------------------------------------------------------
travel_log=[{"country":"France","visits":12,"cities":["Paris","Lille","Dijon"]},{"country":"Germany","visits":5,"cities":["Berlin","Hamburg","Stuttugart"]}]

add={"country":"Russia","visits":2,"cities":["moscow"]}

travel_log.append(add)

print(travel_log)
#---------------------------------------------------------------------------------------
import os

bids={}

whil=True

while whil:

    name=input("input your name:\n")
    bid=int(input("input your bid:\n"))

    bids[name]=bid

    continu=input("continue? Y or N\n").lower()

    if continu=="n":
        whil=False

    os.system("cls")

mayor=max(bids.values())

for key in bids:
    if bids[key]==mayor:
        print(f"max bid is {key} with {bids[key]}")
