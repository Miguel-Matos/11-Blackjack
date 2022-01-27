import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(): #randomly gives cards to either the user or computer
    chosen_card = random.randint(0,12)
    return cards[chosen_card]

user_cards = []
computer_cards = []

i = 0

while i < 2: #generates both player and computer starting hand
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    i += 1

print(f" Your hand: {user_cards} \n Computer hand: {computer_cards}")

no_more_cards = False
while no_more_cards == False:
    more_cards = input("Do you want another card? Y or N: ").lower()
    if more_cards == "y":
        user_cards.append(deal_card())
    else:
        no_more_cards = True
    print(f" Your hand: {user_cards} \n Computer hand: {computer_cards}")


def calculate_score(player_hand): #calculates score
    score = sum(player_hand)
    lets_count = 0
    for i in player_hand:
        if player_hand[lets_count] == 11: #checks and changes 11 to 1 if player hand is higher than 21
            if score > 21:
                player_hand.remove(11)
                player_hand.append(1)
                score = sum(player_hand)
        lets_count += 1

    if score == 21:
        return 0
    else:
        return score

player_points = calculate_score(user_cards)
comp_points = calculate_score(computer_cards)

def judgement(pp,cp): #winning conditions
    if cp == 0 or pp > 21 or cp > pp:
        print("The computer wins")
    elif cp == pp:
        print("It's a tie!")
    elif pp > cp:
        print("You win!")

judgement(player_points, comp_points)



#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.