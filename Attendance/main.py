# Modules to be used in the project
import calendar
from datetime import datetime
from tkinter import *

# Getting current month
month = datetime.now()
month_no = int(month.strftime("%m"))
month_name = calendar.month_name[month_no]

# Main window
root = Tk()
root.title("Attendance Management")
root.geometry("800x600")
root.configure(bg="#F5F6FA")

# Heading
heading = Label(
    root,
    text="Attendance",
    font=("Arial", 28, "bold"),
    fg="#2C3E50",
    bg="#F5F6FA"
)
heading.place(relx=0.5, y=25, anchor="n")


# Date and time
def get_date_day_time():
    now = datetime.now()
    
    today_date = now.strftime("%d-%m-%Y")      # e.g. 2026-07-21
    today_day = now.strftime("%A")              # e.g. Tuesday
    current_time = now.strftime("%I:%M %p")     # e.g. 03:45 PM
    
    return today_date, today_day, current_time


# Getting username and password
def getvals():
    date, day, time = get_date_day_time()
    with open("attendance.txt", "a") as f:
        f.write(f"{date:<12}|{day:<12}|{time:<12}|{uservalue.get():<15} | {passvalue.get():<12}|\n")
        f.write("-" * 70 + "\n")

# Username
user = Label(root, text="Username", bg="#F5F6FA")
user.grid(row=1, column=0, padx=10, pady=(180, 10))

uservalue = StringVar()
userentry = Entry(root, textvariable=uservalue)
userentry.grid(row=1, column=1, padx=10, pady=(180, 10))

# User ID
password = Label(root, text="User ID", bg="#F5F6FA")
password.grid(row=2, column=0, padx=10, pady=10)

passvalue = StringVar()
passentry = Entry(root, textvariable=passvalue)
passentry.grid(row=2, column=1, padx=10, pady=10)

# Submit button
Button(root, text="Submit", command=getvals).grid(
    row=3, column=0, columnspan=2, pady=15
)

root.mainloop()
