# Expense Tracker 

## Overview
This is a beginner-friendly Python project built to help users track their daily personal expenses through a command-line terminal interface. It records item details, categories, and exact timestamps into a text file, allowing users to analyze their spending against a set monthly budget.

## Project Features
- Add Expenses: Record expense name, amount, and choose from 8 predefined categories.
- Automatic Timestamping: Uses Python's datetime module to automatically record the Date, Day, and Time of each entry.
- File Storage: Automatically creates and updates a text file to keep spending records formatted cleanly as a table.
- View Expense History: Read and display all past transactions directly in the terminal.
- Budget Tracking: Calculates total money spent against a default budget of Rs 5000, displaying remaining balance and budget health.
- Category Breakdown: Sums up expenses by category and displays a text-based bar chart to visualize spending patterns.

## Code Explanation

The project uses a simple function-based structure to handle different tasks:

1. `show_menu()`: Prints the main menu options for navigation.
2. `add_expense()`: Takes input for expense name, amount, and lets the user choose a category from a list.
3. `get_date_day_time()`: Uses the `datetime` library to fetch the current date, day of the week, and exact time.
4. `save_expense()`: Checks if the destination file exists, creates table headers if needed, and appends the new entry.
5. `view_all_expense()`: Opens the stored file and reads its content to show all records.
6. `view_totals_by_category()`: Reads the file, splits each line into separate data fields, sums expenses per category, and calculates overall totals.
7. `budget_mood()` and `budget_bar()`: Calculate the percentage of the budget used and generate a visual progress bar.

## Categories Included
- Stationary
- Transport
- Food
- Daily needs
- Entertainment
- Health
- Financial
- Others

## Requirements
- Python 3.x
- `colorama` library (for terminal text styling)

## How to Run

1. Open your terminal or command prompt.
2. Install the required dependency:
   pip install colorama

3. Run the main Python script:
   python main.py

## Sample Output File Structure

Saved text files store records formatted as a structured table:

Date        |Day         |Time        |Item            | Category     |    Price|
---------------------------------------------------------------------------------
28-07-2026  |Tuesday     |03:45 PM    |Notebook        | Stationary   |     80.0|
---------------------------------------------------------------------------------
