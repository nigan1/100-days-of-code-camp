import os
import random

card=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def game():
    user=[]

    dealer=[]

    def deal_card():
        return random.choice(card)

    def calculate_score(list):

        if len(list)==2 and sum(list)==21:
            return 0
        if sum(list)>21 and 11 in list:
            a=list.index(11)
            list[a]=1

        return sum(list)

    def compare(score1,score2):
        if score1==score2:
            return "DRAW"
        elif score1==0:
            return "BLACKJACK HOUSE WIN!"
        elif score2==0:
            return "BLACKJACK PLAYER WIN!"
        elif score2>21:
            return "USER LOSE!"
        elif score1>21:
            return "HOUSE LOSE!"
        else:
            if score1>score2:
                return "HOUSE WIN!"
            else:
                return "PLAYER WIN!"


    for i in range(2):
        user.append(deal_card())
        dealer.append(deal_card())

    while True:
        user_score=calculate_score(user)
        dealer_score=calculate_score(dealer)

        print(f"user cards: {user},user score: {user_score}")
        print(f"dealer cards: {dealer[0]}")


        if user_score==0 or dealer_score==0 or user_score>21:
            break
        else:
            more=input("do you want another card? 'Y' or 'N':\n").lower()
            if more=="y":
                user.append(deal_card())
            else:
                break

    while dealer_score<17 and dealer_score!=0:
        dealer.append(deal_card())
        dealer_score=calculate_score(dealer)


    print(f"user card: {user}, points: {user_score}")
    print(f"dealer card: {dealer}, points: {dealer_score}")

    print(compare(dealer_score,user_score))

while input("do you want play the game?: Y or N\n").lower()=="y":
    os.system('cls')

    game()
