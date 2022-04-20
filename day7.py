import random
import os

word_list=["ardvark","baboon","camel"]

word=random.choice(word_list)

lives=6

character=[]

for i in range(0,len(word)):
    character.append("_")


while True:
    os.system('cls')

    print(character)
    print(f"lives: {lives}")
    guess=input("guess a letter :\n").lower()

    if guess not in word:
        lives-=1

    if lives==0:
        print("GAME OVER")
        break
        

    for element in range(0,len(word)):
        if word[element]==guess:
            character[element]=guess

    if "_" not in character:
        print("YOU WIN")
        
        break
