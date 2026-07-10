import random
from getpass import getpass
def print_heading():
    print("="*40)
    print("     SNAKE  •  WATER  •  GUN")
    print("="*40)
    print()


def print_score(your_score, computer_score):
    width = 80  # match this to your heading width
    score_text = f"You: {your_score}  |  Computer: {computer_score}"
    print(score_text.rjust(width))
    print()


# Against computer
def against_computer(name):

    print_heading()
    computer_score = 0
    your_score = 0
    while(1):
        
        
        computer = random.choice([-1, 0, 1])
        choice = input("Enter your choice: ")
        print(name,": ",choice.lower())
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
            confirm_exit = int(input("Do you really want to exit?\n1. Yes\n2. No\n"))
            if (confirm_exit == 1):
                if (computer_score > your_score):
                    print("Computer won this game")
                elif (your_score > computer_score):
                    print("You won!")
                else:
                    print("It's a tie")
                print("Thanks for playing")
                print("\n\n\n")
                break
            else:
                continue



def with_friend():
    print_heading()
    p1 = input("Enter player 1 name: ")
    p2 = input("Enter player 2 name: ")
    p1_score = 0
    p2_score = 0
    dictionary = {"snake": 1, "water": -1, "gun": 0}

    while 1:
        c1 = getpass(prompt=p1 + "'s turn: ")
        c2 = getpass(prompt=p2 + "'s turn: ")

        p1_choice = dictionary[c1.lower()]
        p2_choice = dictionary[c2.lower()]

        if p1_choice == p2_choice:
            print("It's a draw")
        elif (p1_choice - p2_choice) in (-1, 2):
            p1_score += 1
            print(p1, "wins!")
        else:
            p2_score += 1
            print(p2, "wins!")

        width = 80
        score_text = f"{p1}: {p1_score}  |  {p2}: {p2_score}\n"
        print(score_text.rjust(width))
        # print(f"{p1}: {p1_score}  |  {p2}: {p2_score}\n")
        print("Do you want to continue?\n1. Yes\n2. No")
        if int(input()) != 1:
            confirm_exit = int(input("Do you really want to exit?\n1. Yes\n2. No\n"))
            if (confirm_exit == 1):
                if p1_score > p2_score:
                    print(p1, "won this game")
                elif p2_score > p1_score:
                    print(p2, "won this game")
                else:
                    print("It's a tie")
                print("Thanks for playing\n\n\n")
                break
            else:
                continue

'''Home page'''

def home_page():
    print("=== MAIN MENU ===")
    print("1. Play with Friend")
    print("2. Play with Computer")
    print("3. Exit")
    

# This is my main code:
while(1):
    home_page()
    menu = int(input("Enter your choice: "))
    if (menu == 3):
        confirm_exit = int(input("Do you really want to exit?\n1. Yes\n2. No\n"))
        if (confirm_exit == 1):
            print("Thanks for using this app!")
            break
        else:
            print("\n\n\n")
            continue
    elif (menu == 1):
        with_friend()
    elif (menu == 2):
        name = input("Enter your name: ")
        against_computer(name)
