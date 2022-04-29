import random

print("bienvenido al juego de adivinar el numero")

vidas=10


numero=random.randint(1,100)

print("el numero esta entre 1 y 100")

dificultad=input("eliga su dificultad 'FACIL' - 'DIFICIL'\n").lower()

if dificultad=="dificil":
    vidas=5

def comparar(num):

    if num>numero:
        return "muy alto"
    elif num<numero:
        return "muy bajo"
    else:
        return "ha adivinado el numero, FELICITACIONES!"

while True:
    print(f"vidas restantes: {vidas}")

    guess=int(input("que numero cree que seleccionamos?\n"))

    print(comparar(guess))

    if vidas==1:  
        print("HAS PERDIDO")
        break
    elif comparar(guess)=="ha adivinado el numero, FELICITACIONES!":
        break
    elif comparar(guess)=="muy bajo":
        vidas-=1
    else:
        vidas-=1