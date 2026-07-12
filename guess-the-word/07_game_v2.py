# pip install random-word
from random_word import RandomWords

# For surprise difficulty
import random

# For generating colored text
import colorama
from colorama import Fore, Back, Style
colorama.init()

# To run my code for x sec
import time

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
    print("5. Surprise me")
    print("6. Timer mode")
    print("7. 2 player (with history)")
    print("8. History")
    print("9. Exit")

def mode(length_of_word):

    word = generate_random_word(length_of_word)
    user_word = "Hi"
    count = 0
    score = 100
    while user_word.lower() != word:
        count += 1
        print("Enter a",length_of_word,"letter word: ",end="")
        user_word = input()
        user_word2 = user_word.lower()
        if(len(user_word2) != length_of_word):
            print("Please enter a",length_of_word,"letter word!\n\n\n")
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
        if(user_word2 != word):
            score -= 2
            hint(count,word)
        print()  # one newline after the whole word
    print("\nCongratulations! you guessed the word in",count,"attempts","\n")
    print("Your final score is: ",score,"\n\n\n")


def extreme_mode():
    print("=" * 40)
    print("           EXTREME MODE  ")
    print("=" * 40)
    score = 100
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
        if(user_word2 != word):
            score -= 10
            hint(count,word)
        if(user_word2 == word):
            print("\nCongratulations! you guessed the word in",count,"attempts","\n")
            print("Your final score is: ",score,"\n\n\n")
            break
        print()  # one newline after the whole word
    if(user_word2 != word):
        print("Better luck next time...\nThe word was ",word,"\n\n\n")

# Hints
def hint(num,word):
    if(num == 5):
        print("\n")
        print(Fore.YELLOW + 'HINT: Word starts with: ' + word[0])
        print('\033[39m')
    elif(num == 10):
        print("\n")
        print(Fore.YELLOW + 'HINT: Word ends with: ' + word[len(word) - 1])
        print('\033[39m')
    elif(num == 15):
        print("\n")
        print(Fore.YELLOW + 'HINT: Second letter of the word is: ' + word[1])
        print('\033[39m')


def menu_for_timer_mode():
    print("\n\n\n")
    print("===== TIMER MODE =====")
    print("1. 60 sec")
    print("2. 90 sec")
    print("3. 120 sec")
    print("4. 150 sec")
    print("5. 180 sec")
    print("=======================")
    print("\n")
def timer_mode(num,length_of_word):
    print("=" * 40)
    print("           TIMER MODE  ")
    print("=" * 40)
    if(num == 1):
        end_in_sec = 60
    elif(num == 2):
        end_in_sec = 90
    elif(num == 3):
        end_in_sec = 120
    elif(num == 4):
        end_in_sec = 150
    elif(num == 5):
        end_in_sec = 180
    start_time = time.time()
    end_time = start_time + end_in_sec
    word = generate_random_word(length_of_word)
    user_word = "Hi"
    count = 0
    score = 100
    while time.time() < end_time:
        count += 1
        print("Enter a",length_of_word,"letter word: ",end="")
        user_word = input()
        user_word2 = user_word.lower()
        if(len(user_word2) != length_of_word):
            print("Please enter a",length_of_word,"letter word!\n\n\n")
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
        if(user_word2 != word):
            score -= 2
            hint(count,word)
            print()  # one newline after the whole word
        if(user_word2 == word):
            print("\nCongratulations! you guessed the word in",count,"attempts","\n")
            print("Your final score is: ",score,"\n\n\n")
            break
    # If we reach here, time is up
    if(time.time() >= end_time):
        print("\nTime's up!")
        print("The word was:", word, "\n\n\n")



# This is for two player version  :)
def two_player(p1_name, p2_name):
    word = generate_random_word(6)
    p1 = ""
    p1_count = 0
    p2 = ""
    p2_count = 0
    print("Enter a 6 letter word\n")
    while (p1.lower() != word or p2.lower() != word):
        p1_count += 1
        p1 = input(f"{p1_name}: ")
        # print("\n")
        p1 = p1.lower()
        if (p1 == word):
            print(f"Congratulations! {p1_name} guesses it in {p1_count} attempts\n")
            victory = p1_name
            break
        if(len(p1) != 6):
            print("Please enter a 6 letter word!\n\n\n")
            continue
        else:
            for i in range(len(p1)):
                if p1[i] == word[i]:
                    print(Fore.GREEN + p1[i], end="")
                    print('\033[39m', end="")  # no newline
                elif  p1[i] != word[i] and  p1[i] in word:
                    print(Fore.YELLOW +  p1[i], end="")
                    print('\033[39m', end="")  # no newline
                else:
                    print(Fore.RED +  p1[i], end="")
                    print('\033[39m', end="")  # no newline
        
        # if(p1 != word):
        #     hint(p1_count,word)
        print("\t"*len(p1_name))
        print()
        p2_count += 1
        p2 = input(f"{p2_name}: ")
        # print("\n")
        p2 = p2.lower()
        if (p2 == word):
            print(f"Congratulations! {p2_name} guesses it in {p2_count} attempts\n")
            victory = p2_name
            break

        if(len(p2) != 6):
            print("Please enter a 6 letter word!\n\n\n")
            continue
        else:
            for i in range(len(p2)):
                if p2[i] == word[i]:
                    print(Fore.GREEN + p2[i], end="")
                    print('\033[39m', end="")  # no newline
                elif  p2[i] != word[i] and  p2[i] in word:
                    print(Fore.YELLOW +  p2[i], end="")
                    print('\033[39m', end="")  # no newline
                else:
                    print(Fore.RED +  p2[i], end="")
                    print('\033[39m', end="")  # no newline
        if(p1 != word):
            hint(p2_count,word)
        print("\t"*len(p2_name))
        print()
    history(p1_name, p2_name, victory)

def history(p1_name, p2_name,victory):
    with open(f"history/history.txt","a") as f:
        f.write(f"{p1_name} VS {p2_name} " +"                                  " + f"{victory} won this game.\n")
    
def read_history():
    with open(f"history/history.txt" , "r") as f:
        read_h = f.read()
    print(read_h)

# This is my main code
while True:
    menu()
    menu_choice = int(input("Enter you choice: "))
    if (menu_choice == 1):
        print("=" * 40)
        print("              EASY MODE  ")
        print("=" * 40)
        mode(5)
    elif (menu_choice == 2):
        print("=" * 40)
        print("           MEDIUM MODE  ")
        print("=" * 40)
        mode(6)
    elif (menu_choice == 3):
        print("=" * 40)
        print("              HARD MODE  ")
        print("=" * 40)
        mode(8)
    elif (menu_choice == 4):
        extreme_mode()
    elif(menu_choice == 5):
        # 1 : extreme 
        # 2 : timer
        surprise = random.choice([5,6,8,1,2])
        if(surprise == 1):
            extreme_mode()
        elif(surprise == 2):
            menu_for_timer_mode()
            choice_for_timer = int(input("Enter any mode: "))
            if(choice_for_timer > 5 or choice_for_timer < 1):
                print("Invalid option...\n\n\n")
                continue
            len_of_word = int(input("Enter the length of word: "))
            timer_mode(choice_for_timer, len_of_word)
        else:
            if(surprise == 5):
                print("=" * 40)
                print("              EASY MODE  ")
                print("=" * 40)
            elif(surprise == 6):
                print("=" * 40)
                print("           MEDIUM MODE  ")
                print("=" * 40)
            elif(surprise == 8):
                print("=" * 40)
                print("              HARD MODE  ")
                print("=" * 40)
            mode(surprise)

    


    elif(menu_choice == 6):
        menu_for_timer_mode()
        choice_for_timer = int(input("Enter any mode: "))
        if(choice_for_timer > 5 or choice_for_timer < 1):
            print("Invalid option...\n\n\n")
            continue
        len_of_word = int(input("Enter the length of word: "))
        timer_mode(choice_for_timer, len_of_word)

    elif(menu_choice == 7):
        print("\n\n\n")
        p1_name = input("Enter first player's name: ")
        p2_name = input("Enter second player's name: ")
        print("=" * 40)
        print("           TWO PLAYER MODE  ")
        print("=" * 40)
        two_player(p1_name, p2_name)
    elif(menu_choice == 8):
        read_history()
        print("\n\n\n")
    elif(menu_choice == 9):
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