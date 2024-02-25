import random
from enum import Enum

game_count = 0

def RPS():
    class rps(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3
        
    player_move = input("Enter\n1 for ROCK\n2 for PAPER\n3 for SCISSORS:\n\n")
    if player_move not in ["1", "2", "3"]:
        print("Player Choice Invalid")
        return RPS()
    player = int(player_move)
    
    computer_choice = random.choice("123")
    computer = int(computer_choice)
    
    print("You Chose: " + str(rps(player)).replace('rps.', ''))
    print("Computer Chose: " + str(rps(computer)).replace('rps.', ''))
    
    def winner(player, computer):
        if player == computer:
           return "Tie Game!"
        elif player == 1 and computer == 3:
           return "You Win!"
        elif player == 2 and computer == 1:
           return "You Win!"
        elif player == 3 and computer == 2:
           return "You Win!"
        else:
           return "Computer Wins!"

    result = winner(player, computer)
    print(result)
    
    global game_count
    game_count += 1
    print("\nGames played:", game_count)
    
    while True:
        play_again = input("\nWould you like to play again?: Yes or No\n")
        if play_again not in ["Yes", "yes", "No", "no"]:
            continue
        else:
            break
    
    if play_again == "Yes":
        return RPS()
    elif play_again == "yes":
        return RPS()
    else:
        print("Thank you for playing!")
        
    
RPS()
    
  