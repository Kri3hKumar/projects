import random
def print_heading():
    print("="*40)
    print("     SNAKE  •  WATER  •  GUN")
    print("="*40)
    print()

print_heading()
def print_score(your_score, computer_score):
    width = 80  # match this to your heading width
    score_text = f"You: {your_score}  |  Computer: {computer_score}"
    print(score_text.rjust(width))
    print()
computer_score = 0
your_score = 0
while(1):
    
    
    computer = random.choice([-1, 0, 1])
    choice = input("Enter your choice: ")
    print("You: ",choice.lower())
    dictionary = {
        1: "snake",
        -1: "water",
        0: "gun"
    }
    revdictionary = {
        "snake": 1,
        "water": -1,
        "gun": 0
    }
    you = revdictionary[choice.lower()]
    print("Computer: ",dictionary[computer])
    if(computer == you):
        print("Its a draw")
    else:
        if((computer - you) == -1 or  (computer - you) == 2 ):
                print("You lose!")
                computer_score = computer_score + 1
        else:
            print("You win!")
            your_score = your_score + 1 
    print_score(your_score, computer_score)
    print("Do you want to continue?\n1. Yes\n2. No")
    exit_this_game = int(input())
    if (exit_this_game == 1):
         continue
    else:
        if (computer_score > your_score):
             print("Computer won this game")
        elif (your_score > computer_score):
             print("You won!")
        else:
             print("It's a tie")
        print("Thanks for playing")
        break
