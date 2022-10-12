import random


def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice (rock, paper, scissors):")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
        return ("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            return ("Rock Smashes Sissors! You Win!")
        else:
            return ("Paper covers Rock! You Lose")

    elif player == "paper":
        if computer == "rock":
            return ("Paper covers Rock!! You Win!")
        else:
            return ("Scissors cuts paper! You Lose")

    elif player == "sicssors":
        if computer == "paper":
            return ("Scissors cuts paper! You Win!")
        else:
            return ("Rock Smashes Sissors! You Lose")


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
