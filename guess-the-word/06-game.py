# pip install random-word
from random_word import RandomWords


# For generating colored text
import colorama
from colorama import Fore, Back, Style
colorama.init()



# For generating random word
def generate_random_word(num):
    r = RandomWords()
    random_word = r.get_random_word()
    while len(random_word) != num:
        random_word = r.get_random_word()
    return random_word

def menu():
    print("=== GUESS THE WORD ===")
    print("1. Easy (5 letters)")
    print("2. Medium (6 letters)")
    print("3. Hard (8 letters)")
    print("4. Extreme (8 letters + 8 chances)")
    print("5. Exit")

def easy_mode():
    word = generate_random_word(5)
    user_word = "Hi"
    while user_word != word:
        user_word = input("Enter the word: ")
        user_word2 = user_word.lower()
        if(len(user_word2) != 5):
            print("Please enter a 5 letter word!\n\n\n")
            continue
        else:
            for i in range(len(user_word2)):
                if user_word2[i] == word[i]:
                    print(Fore.GREEN + user_word2[i], end="")
                    print('\033[39m', end="")  # no newline
                elif user_word2[i] != word[i] and user_word2[i] in word:
                    print(Fore.YELLOW + user_word2[i], end="")
                    print('\033[39m', end="")  # no newline
                else:
                    print(Fore.RED + user_word2[i], end="")
                    print('\033[39m', end="")  # no newline

        print()  # one newline after the whole word
    print("Congratulations! you guessed the word...\n\n\n")
def medium_mode():
    word = generate_random_word(6)
    user_word = "Hi"
    while user_word != word:
        user_word = input("Enter the word: ")
        user_word2 = user_word.lower()
        if(len(user_word2) != 6):
            print("Please enter a 6 letter word!\n\n\n")
            continue
        else:
            for i in range(len(user_word2)):
                if user_word2[i] == word[i]:
                    print(Fore.GREEN + user_word2[i], end="")
                    print('\033[39m', end="")  # no newline
                elif user_word2[i] != word[i] and user_word2[i] in word:
                    print(Fore.YELLOW + user_word2[i], end="")
                    print('\033[39m', end="")  # no newline
                else:
                    print(Fore.RED + user_word2[i], end="")
                    print('\033[39m', end="")  # no newline

        print()  # one newline after the whole word
    print("Congratulations! you guessed the word...\n\n\n")
def hard_mode():
    word = generate_random_word(8)
    user_word = "Hi"
    while user_word != word:
        user_word = input("Enter the word: ")
        user_word2 = user_word.lower()
        if(len(user_word2) != 8):
            print("Please enter a 8 letter word!\n\n\n")
            continue
        else:
            for i in range(len(user_word2)):
                if user_word2[i] == word[i]:
                    print(Fore.GREEN + user_word2[i], end="")
                    print('\033[39m', end="")  # no newline
                elif user_word2[i] != word[i] and user_word2[i] in word:
                    print(Fore.YELLOW + user_word2[i], end="")
                    print('\033[39m', end="")  # no newline
                else:
                    print(Fore.RED + user_word2[i], end="")
                    print('\033[39m', end="")  # no newline

        print()  # one newline after the whole word
    print("Congratulations! you guessed the word...\n\n\n")
def extreme_mode():
    word = generate_random_word(8)
    # print(word)
    user_word = "Hi"
    count = 0
    while count < 8:
        count += 1
        user_word = input("Enter the word: ")
        user_word2 = user_word.lower()
        
        if(len(user_word2) != 8):
            print("Please enter a 8 letter word!\n\n\n")
            continue
        else:
            for i in range(len(user_word2)):
                if user_word2[i] == word[i]:
                    print(Fore.GREEN + user_word2[i], end="")
                    print('\033[39m', end="")  # no newline
                elif user_word2[i] != word[i] and user_word2[i] in word:
                    print(Fore.YELLOW + user_word2[i], end="")
                    print('\033[39m', end="")  # no newline
                else:
                    print(Fore.RED + user_word2[i], end="")
                    print('\033[39m', end="")  # no newline
        if(user_word2 == word):
            print("\nCongratulations! you guessed the word in",count,"attempts","\n\n\n")
            break
        print()  # one newline after the whole word
    if(user_word2 != word):
        print("Better luck next time...\nThe word was ",word,"\n\n\n")
 
# This is my main code
while True:
    menu()
    menu_choice = int(input("Enter you choice: "))
    if (menu_choice == 1):
        easy_mode()
    elif (menu_choice == 2):
        medium_mode()
    elif (menu_choice == 3):
        hard_mode()
    elif (menu_choice == 4):
        extreme_mode()
    
    elif(menu_choice == 5):
        confirm_exit = int(input("Do you really want to exit?\n1. Yes\n2. No\n"))
        if (confirm_exit == 1):
            print("Thanks for playing this game...")
            break
        elif (confirm_exit == 2):
            print("\n\n\n")
            continue
        else:
            print("Invalid Input...\n\n\n")
            continue