import math

test_h=int(input("height of wall:\n"))
test_w=int(input("width of wall:\n"))
coverage=5

def paint_calc(test_h,test_w,coverage):
    num_cans=math.ceil((test_h*test_w)/coverage)

    print(f"you need {num_cans} cans")

paint_calc(test_h,test_w,coverage)
#------------------------------------------

n=int(input("insert number:\n"))

def prime_checker(num):
    prime=0

    for dig in range(2,num-1):
        if num%dig==0:
            prime+=1

    if prime>0:
        print("not prime")
    else:
        print("is prime")

prime_checker(n)
#--------------------------------------------
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


while True:
    direction=input("type 'encode' to encrypt or 'decode' to decrypt:\n" )

    text=input("type your message:\n")
    shift=int(input("type the shift number:\n"))

    def caesar(direction,text,shift):
        new_text=""

        if shift>25:
            shift=shift%25

        for element in text:
            if element in alphabet:
            
                position=alphabet.index(element)
                if direction=="encode":
                    new_position=position+shift
                else:
                    new_position=position-shift

                new=alphabet[new_position]
                new_text+=new
            else:
                new_text+=element
        
        print(f"{direction}d text : {new_text}")

    caesar(direction,text,shift)

    again=input("run again? Y o N\n").lower()

    if again=="n":
        break




