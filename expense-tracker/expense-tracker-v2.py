import calendar
import datetime
budget = 5000
from datetime import datetime
import colorama
from colorama import Fore
import os
month = datetime.now()
month_no = month.strftime("%m")
# print(month_no)
month_no = (int)(month_no)
# print(type(month_no))

month_name = calendar.month_name[month_no]

# if month_no == 1:

# Now naming month name
# if month_no == 
current_month_file = datetime.now().strftime(month_name+"_%Y.txt")
# This is only for if file is new


expenses = []  # this list will hold all expenses

categories = ["Stationary", "Transport", "Food", "Daily needs", "Entertainment", "Health", "Financial", "Others"]
# Show months
def month():
    for i in range(1, 13):
        print(f"{i}. {calendar.month_name[i]}")


def show_menu():
    print("===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. View Expense by category")
    print("5. Exit")
    print("============================")

def expense_category():
    print("\nChoose the expense category: ")
    print("1. Stationary")
    print("2. Transport")
    print("3. Food")
    print("4. Daily needs")
    print("5. Entertainment")
    print("6. Health")
    print("7. Financial")
    print("8. Others")

# Add expense
def add_expense(file):
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))

    expense_category()  # just prints the menu
    choice = int(input("Enter category number: "))
    print("\n")
    category = categories[choice - 1] #If user enters 3 he means index 2: so this will point toward index 2 which is Food. So this will acress food form the list declared above.
    save_expense(expense_name, expense_amount, category, file)

# Date and time (Help from AI and google)
def get_date_day_time():
    now = datetime.now()
    
    today_date = now.strftime("%d-%m-%Y")      # e.g. 2026-07-21
    today_day = now.strftime("%A")              # e.g. Tuesday
    current_time = now.strftime("%I:%M %p")     # e.g. 03:45 PM
    
    return today_date, today_day, current_time

# Saving expense
def save_expense(expense_name, expense_amount, category, file):

    date, day, time = get_date_day_time()
    
    file_is_new = not os.path.exists(file) or os.path.getsize(file) == 0
    with open(file, "a") as f:
        if file_is_new:
            f.write(f"{'Date':<12}|{'Day':<12}|{'Time':<12}|{'Item':<15} | {'Category':<12} | {'Price':>8}|\n")
            f.write("-" * 81 + "\n")
        f.write(f"{date:<12}|{day:<12}|{time:<12}|{expense_name:<15} | {category:<12} | {expense_amount:>8}|\n")
        f.write("-" * 81 + "\n")
        
# View all expense:
def view_all_expense(file):
    print(" "*20 + "Expense Table")
    print()
    with open(file, "r") as f:
        content = f.read()
        print(content)


def budget_mood(total, budget):
    percent_used = (total / budget) * 100
    if percent_used < 50:
        return Fore.GREEN + "You're doing great!" + Fore.RESET
    elif percent_used < 80:
        return Fore.YELLOW + "Keep an eye on it" + Fore.RESET
    elif percent_used <= 100:
        return Fore.RED + "Cutting it close!" + Fore.RESET
    else:
        return Fore.RED + "You've gone over budget!" + Fore.RESET
# Sum of total amount by category:
def view_totals_by_category(menu, file):
    totals = {}  # will hold category -> total sum
    # file = input("Enter file name: ")
    with open(file, "r") as f:
        lines = f.readlines()

    for line in lines[2:]:  # skip header row and the dashed separator line
        if line.strip() == "" or line.startswith("-"):
            continue  # skip empty lines or separator lines

        parts = line.split("|")
        category = parts[4].strip()   # "Category" column
        price = float(parts[5].strip())

        if category in totals:
            totals[category] += price
        else:
            totals[category] = price
    if menu == 3:
        total = sum(totals.values())
        print("Total money spent: Rs",total)
        print(budget_mood(total, budget))
        print()
        if (budget - total >= 0):
            print(Fore.GREEN + f"Money left: Rs {budget - total}")
            print('\033[39m')
            
        else:
            print(Fore.RED + f"Money overspent: Rs {total - budget}")
            print('\033[39m')
        budget_bar(total, budget, 20)

        
    elif menu == 4:
        print(Fore.GREEN + "\n===== Category-wise Totals =====")
        print('\033[39m')
        for cat, total in totals.items():
            print(f"{cat}: ₹{total}")
        print("\n\n")


    
        # Bar chart
        category_colors = {
        "Stationary": Fore.YELLOW,
        "Transport": Fore.BLUE,
        "Food": Fore.GREEN,
        "Daily needs": Fore.CYAN,
        "Entertainment": Fore.MAGENTA,
        "Health": Fore.RED,
        "Financial": Fore.WHITE,
        "Others": Fore.LIGHTBLACK_EX
        }
        print(Fore.GREEN + "===== Spending Bar Chart =====")
        print('\033[39m')
        sorted_totals = sorted(totals.items(), key=lambda x: x[1], reverse=True)
        for cat, total in sorted_totals:
            bar = "█" * int(total / 50)
            color = category_colors.get(cat, Fore.WHITE)
            print(f"{cat:<12} | " + color + bar + Fore.RESET + f" ₹{total}")
            print()

    # money_spent = total


def budget_bar(total, budget, length=20):
    percent = min(total / budget, 1)
    filled = int(length * percent)
    bar = "█" * filled + "░" * (length - filled)
    if total <= budget:
        label = f"{percent * 100:.0f}%"
    else:
        label = "100%+"
    print(f"Budget used: {bar} {label}")



# This is my main code:
while True:
    show_menu()
    menu = int(input("Select your option: "))
    if menu == 5:
        print("Exiting... Goodbye!")
        break
    select_year = int(input("Enter the year: "))
    month()
    select_month = int(input("Select the month: "))
    selected_month_name = calendar.month_name[select_month]

    file = datetime.now().strftime(selected_month_name+"_"+ (str)(select_year) + ".txt")
    if menu == 1:
        add_expense(file)
    elif menu == 2:
        view_all_expense(file)
    elif menu == 3:
        view_totals_by_category(menu, file)
    elif menu == 4:
        view_totals_by_category(menu, file)
    else:
        print("Invalid choice, please try again.\n")
