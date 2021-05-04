import random
your_wins = 0
computer_wins = 0
max_rounds = 9
moves_arr = ["Rock", "Paper", "Scissors"]

while (your_wins <= 3) or (computer_wins <= 3):
    computer_move = moves_arr[random.randint(0,2)]
    your_input = input('Rock, Paper or Scissors?')
    if your_input == "Rock":
        if computer_move == "Rock":
            print(f"You tied! Computer: {computer_wins} Your Wins: {your_wins}")
        if computer_move =="Scissors":
            your_wins += 1
            print(f"You won! Computer: {computer_wins} Your Wins: {your_wins}")
        if computer_move == "Paper":
            computer_wins +=1
            print(f"You lost! Computer: {computer_wins} Your Wins: {your_wins}")
    if your_input == "Paper":
        if computer_move == "Paper":
            print(f"You tied! Computer: {computer_wins} Your Wins: {your_wins}")
        if computer_move == "Rock":
            your_wins += 1
            print(f"You won! Computer: {computer_wins} Your Wins: {your_wins}")
        if computer_move == "Scissors":
            computer_wins +=1
            print(f"You lost! Computer: {computer_wins} Your Wins: {your_wins}")
    if your_input == "Scissors":
        if computer_move == "Scissors":
            print(f"You tied! Computer: {computer_wins} Your Wins: {your_wins}")
        if computer_move =="Paper":
            your_wins += 1
            print(f"You won! Computer: {computer_wins} Your Wins: {your_wins}")
        if computer_move == "Rock":
            computer_wins +=1
            print(f"You lost! Computer: {computer_wins} Your Wins: {your_wins}")
    if (your_wins == 3):
        print("YOU WIN!!!!!!!!!!!!!!!!!")
        break
    elif (computer_wins == 3):
        print("YOU LOSEEEEEEEEEEEEEEEE!!")
        break