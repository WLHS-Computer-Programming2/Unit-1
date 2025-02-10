import random

"""
Name: Mr. Smith
File: rps_minus_one.py
Description: Implements the Rock Paper Scissor Minus One
game from Squid Game
"""

"""
Pseudocode
Have computer pick two random "hands" of rps
SET comp_score, player_score to 0
STORE values in comp_hand somehow (you choose)
ASK user for their hands
STORE values in player_hand
ASK user which hand to keep
computer randomly chooses hand
EVALUATE who wins
UPDATE score
ASK if they want to continue or quit
IF quit, PRINT scores and END game
    ELSE play again
"""

def comp_hands(options:list)->list:
    comp_choice1 = random.randint(0,2)
    comp_choice2 = random.randint(0,2)
    while comp_choice1 == comp_choice2:
        comp_choice2 = random.randint(0,2)
    comp_hands = [options[comp_choice1],options[comp_choice2]]
    return comp_hands

def player_hands(options:list)->list:
    player_hand1 = int(input("Left hand: Please choose rock(1), paper(2), or scissors(3) "))
    player_hand2 = int(input("Right hand: Please rock(1), paper(2), or scissors(3) "))
    player_hands = [options[player_hand1-1],options[player_hand2-1]]
    return player_hands

def minus_one(player_hand:list,computer_hand:list)->list:
    #print(f"Player hands: {player_hand[0]} and {player_hand[1]}")
    print("Which hand do you want to keep left(1) or right(2)?")
    player_choice = int(input("> "))
    computer_choice = random.randint(0,1)
    player_hand_final = player_hand[player_choice-1]
    computer_hand_final = computer_hand[computer_choice]
    #print(f"Player:{player_hand_final}\nComputer{computer_hand_final}")
    return [player_hand_final,computer_hand_final]
    

def determine_winner(final_hands:list,scores:list)->list:
    player = final_hands[0]
    computer = final_hands[1]
    if player == computer:
        print("The result is a tie")
        return scores
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        scores[0] += 1
        print("The player wins this round")
        return scores
    else:
        scores[1] += 1
        print("The computer wins this round")
        return scores
    
def print_score(scores):
    print(f"The player has a score of {scores[0]} and the computer has a score of {scores[1]}")
    print()
    
def print_hands(hand_one:list,hand_two:list=None)->None:
    if hand_two is None:
        print(f"Computer | {hand_one[1]:8}")
        print(f"Player   | {hand_one[0]:8}")
    else:
        print(f"{"":<11}{"Left Hand":<11}| {"Right Hand"}")
        print(f"Computer   {hand_two[0]:<11}{"| "}{hand_two[1]}")
        print(f"{"Player   ":<11}{hand_one[0]:<11}{"| "}{hand_one[1]}")
        print()
    



def main():
    # first is always player, second is always computer
    scores = [0,0] 
    while True:
        options = ["rock","paper","scissors"]
        comp = []
        player = []
        comp = comp_hands(options)
        player = player_hands(options)
        
        #print(f"The computer has chosen: {comp[0]} and {comp[1]}")
        #print(f"You have chosen: {player[0]} and {player[1]}.")
        print_hands(player,comp)
        final_choices = minus_one(player,comp)
        print(f"Final Choices: {final_choices}")
        print_hands(final_choices)
        scores = determine_winner(final_choices,scores)
        print_score(scores)
        try:
            print("Would you like to play again? (yes or no)")
            continue_game = input(">")
        except ValueError:
            print("Invalid choice. The game will continue")
        if(continue_game.lower() == 'yes'):
            print("Prepare for the next round")
            print()
            continue
        elif(continue_game.lower()=='no'):
            if(scores[0]>scores[1]):
                print(f"Final Score")
                print(f"Computer: {scores[1]:<5}Player:{scores[0]}")
                print("You win! Thanks for playing.")
            elif(scores[0]<scores[1]):
                print(f"Final Score")
                print(f"Computer: {scores[1]:<5}Player:{scores[0]}")
                print("You didn't win, better luck next time.")
            else:
                print(f"Final Score")
                print(f"Computer: {scores[1]:<5}Player:{scores[0]}")
                print("The game ended in a tie.")
            break
        else:
            print("Invalid option. The game will continue")
    
if __name__ == '__main__':
    main()