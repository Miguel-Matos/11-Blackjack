import art
import random

def game():
    print(art.logo)
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

    print(f" Your hand: {user_cards} \n Computer hand: [{computer_cards[0]}]")

    def cont_game():
        no_more_cards = False
        while no_more_cards == False:
            more_cards = input("Do you want another card? Y or N: ").lower()
            if more_cards == "y":
                user_cards.append(deal_card())
                print(f" Your hand: {user_cards} \n Computer hand: {computer_cards[0]}")
            else: #lets computer draw cards as long as they are under 17 and then breaks the loop  
                more_than_seventeen = False
                while more_than_seventeen == False:
                    computer_cards.append(deal_card())
                    current_comp_hand = sum(computer_cards)
                    if current_comp_hand >= 17:
                        more_than_seventeen = True
                    
                no_more_cards = True
        if current_comp_hand > 21:
            PC_card_length = len(computer_cards) - 1
            del computer_cards[PC_card_length]
            print(f" Your hand: {user_cards} \n Computer hand: {computer_cards}")
        else:
            print(f" Your hand: {user_cards} \n Computer hand: {computer_cards}")

    cont_game()


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

    again = input("Play again? Y or N: ").lower()
    if again == "y":
        game()

game()


#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.