#password algorithm gui app (main.py + gui.py)
# 11/22/2023
# Total spend time for this project: 5.5 hours
# Mehmet Kahya

# Github repo: PasswordAlgorithms
''' 
    TODO: 
    [] Integrate OpenAI AI's into this project !! 
    [] Create Class
    [X] Create a better UI
    [X] Create a better UX
    [X] Create a better password generator algorithm
    [X] Create a better password checker algorithm
'''

import time
from datetime import datetime
import random
import math
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import font
from tkinter.ttk import Style
from passpwnedcheck.pass_checker import PassChecker

root = Tk()
root.title("Password Algorithms")
root.geometry("500x500")
root.resizable(False, False)
p1 = PhotoImage(file = 'key.png') 
background = "#155b82"
# Setting icon of master window 
root.iconphoto(False, p1) 
root.config(bg=background)

style = Style(root)
style.theme_use("clam")

#get date and time from time lib
date = time.strftime("%d/%m/%Y")
time = time.strftime("%H:%M:%S")

def update_time():
    global time_var
    time_var = datetime.now()
    #print(time_var)  # Print the time to the console for demonstration purposes
    root.after(1000, update_time)  # Schedule the next update

time_var = datetime.now()


def credits():
    print(f"log {time_var} + pressed credits button")
    messagebox.showinfo("Credits", '''
    PASSWORD ALGORITHMS
    ALL RIGHTS RESERVED © 2023

    This program was created by Mehmet Kahya(Team Lead) and Hackathon[crq1243] team members. 

    It is licensed under the MIT License. 

    Special thanks to: @ayseguldemireel for better UI experience. 

    11/22/2023
    ''')

def back_to_black():
    print(f"log {time_var} ------->  pressed back to black button")
    
    for widget in root.winfo_children():
        widget.destroy()
    mainScreen()

def password_generator():
    print(f"log {time_var} ------->  opened password generator section...")
    
    back_button = Button(root, text="<", font=("Helvetica", 15), bg=background, fg="red", command=back_to_black)
    back_button.place(x=10, y=27)

    Mainheader.destroy()
    password_generator_button.destroy()
    password_checker_button.destroy()
    ascii_art.destroy()

    header = Label(root, text="Password Generator", font=("Helvetica", 30, "bold"), bg=background, fg="white", cursor="heart")
    header.place(x=90, y=20)
    
    length = Label(root, text="Set the length of the password: ", font=("Helvetica", 15), bg=background, fg="white")
    length.place(x=10, y=100)

    length_entry = Entry(root, width=25, borderwidth=2)
    length_entry.place(x=235, y=100)

    alternative = Label(root, text="How many passwords to generate: ", font=("Helvetica", 13), bg=background, fg="white")
    alternative.place(x=10, y=150)

    alternative_entry = Entry(root, width=25, borderwidth=2)
    alternative_entry.place(x=235, y=150)

    specialCharacters = Label(root, text="Do you want special characters in your password?", font=("Helvetica", 13), bg=background, fg="white")
    specialCharacters.place(x=10, y=200)

    specialCharacters_check = IntVar()
    checkbutton = ttk.Checkbutton(root, variable=specialCharacters_check, onvalue=1, offvalue=0)
    checkbutton.place(x=330, y=200)

    password_label = Label(root, text="", font=("Helvetica", 13), bg=background, fg="white")
    password_label.place(x=30, y=300)

    def generate():
        print(f"log {time_var} ------->  Generating password...")
        if specialCharacters_check.get() == 1:
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-+*/=!&/()>£#$½§{[]}ğüşiöçĞÜŞİÖÇ@∑€®₺¥üiöπ¨~`æ´¬¨∆^ğƒ∂ßæ≈∫~µ≤≥÷|><|"
        else:
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"



        alternative_entry_value = int(alternative_entry.get())
        length_entry_value = int(length_entry.get())

        password_listbox = Listbox(root, width=50, height=10, font=("Helvetica", 10))
        password_listbox.place(x=100, y=300)  # Adjust the position as needed

        passwordList = []

        # Open the file in write mode
        file = open('passwords.txt', 'a')

        def add_password():
            if passwordList:
                password = passwordList.pop(0)
                password_listbox.insert(END, password)
                file.write(password + '\n')  # Write the password to the file
                root.after(500, add_password)  # Schedule the next call
            else:
                file.close()  # Close the file when all passwords have been written

        for _ in range(alternative_entry_value):
            password = ""
            for _ in range(length_entry_value):
                password += random.choice(characters)
            passwordList.append(password)

        add_password()  # Start adding passwords

    generate_button = Button(root, text="Generate", font=("Helvetica", 15, "bold"), bg=background, fg="red", command=generate)
    generate_button.place(x=10, y=250)

def password_checker():
    print(f"log {time_var} ------->  opened password checker section...")
    back_button = Button(root, text="<", font=("Helvetica", 15), bg=background, fg="red", command=back_to_black, width=2)
    back_button.place(x=10, y=27)

    password_generator_button.destroy()
    password_checker_button.destroy()

    ascii_art.destroy()
    Mainheader.destroy()

    header = Label(root, text="Password Checker", font=("Helvetica", 30, "bold"), bg=background, fg="white")
    header.place(x=90, y=20)

    password_label = Label(root, text="Enter your password: ", font=("Helvetica", 20), bg=background, fg="white")
    password_label.place(x=10, y=100)

    password_entry = Entry(root, width=30, borderwidth=2)
    password_entry.place(x=215, y=100)

    result_label = Label(root, text="", font=("Helvetica", 13), bg=background, fg="white")
    result_label.place(x=10, y=300)

    def check_password():
        print(f"log {time_var} ------->  Checking password...")
        password = password_entry.get()

        uppercaseInPassword = sum(1 for harf in password if harf.isupper())
        lowercaseInPassword = sum(1 for harf in password if harf.islower())

        #calculate number of digits in password
        digits = sum(1 for harf in password if harf.isdigit())

        safetyPoint = 0
        if len(password) >= 8:
            safetyPoint +=1

        if any(harf.isupper() for harf in password):
            safetyPoint +=1

        if any(harf.islower() for harf in password):
            safetyPoint +=1            

        if any(harf.isdigit() for harf in password):
            safetyPoint +=1

        if any(not harf.isalnum() for harf in password):
            safetyPoint +=1
        

        safetyPoint = {
            0: "0 - Very Weak",
            1: "1 - Weak",
            2: "2 - Medium",
            3: "3 - Strong",
            4: "4 - Very Strong",
            5: "5 - Extremely Strong"
        }.get(safetyPoint, "Invalid")

        try_speed_per_second = 100000000
        lenOfCharacters = 62

        possible_password = lenOfCharacters ** len(password)
        cracking_time_sec = possible_password / try_speed_per_second
        cracking_time_day = cracking_time_sec / (60 * 60 * 24)

        result_listbox = Listbox(root, width=100, height=10, font=("Helvetica", 17))
        result_listbox.place(x=0, y=250)

        def update_listbox(text):
            result_listbox.insert(END, text)

        pass_checker = PassChecker()
        is_leaked, count = pass_checker.is_password_compromised(password)

        root.after(0, lambda: update_listbox(f'Password: {password}'))
        root.after(1000, lambda: update_listbox(f'length of password: {len(password)}'))
        root.after(2000, lambda: update_listbox(f'number of Uppercase letters: {uppercaseInPassword}'))
        root.after(3000, lambda: update_listbox(f'number of Lowercase letters: {lowercaseInPassword}'))
        root.after(4000, lambda: update_listbox(f'number of digits: {digits}'))
        root.after(5000, lambda: update_listbox(f'Cracking time: {cracking_time_day} sec'))

        if is_leaked:
            (f'Your password has been leaked {count} times')
            root.after(0, lambda: update_listbox(f'Has this password been leaked before? : {count} times pwned!!!'))
            safetyPoint = "0 - Very Weak"
        else:
            print('Your password has not been leaked (yet)')
            root.after(0, lambda: update_listbox(f'Has this password been leaked before? : No it is not pwned! '))

        root.after(6000, lambda: update_listbox(f'Safety point (0-5): {safetyPoint}\n\n'))
    
    check_button = Button(root, text="Check", font=("Helvetica", 15, "bold"), bg=background, fg="black", command=check_password, width=30)
    check_button.place(x=100, y=150)

def mainScreen():
    print(f"log {time_var} ------->  Welcome to Password Algorithms")
    global password_generator_button, password_checker_button, ascii_art, Mainheader
    Mainheader = Label(root, text="Password Algorithms", font=("Comfortaa", 30, "bold"), bg=background, fg="white")
    Mainheader.place(x=90, y=20)

    password_generator_button = Button(root, text="Password Generator", font=("Helvetica", 15, "bold"), bg=background, fg="black", command=password_generator, width=20, height=10)
    password_generator_button.place(x=20, y=100)

    password_checker_button = Button(root, text="Password Checker", font=("Helvetica", 15, "bold"),  bg=background,fg='black',command=password_checker, width=20, height=10)
    password_checker_button.place(x=260, y=100)

    ascii_art = Label(root, text=
    '''
    ██████╗  █████╗ ███████╗███████╗
    ██╔══██╗██╔══██╗██╔════╝██╔════╝
    ██████╔╝███████║███████╗███████╗
    ██╔═══╝ ██╔══██║╚════██║╚════██║ 
    ██║     ██║  ██║███████║███████║    
    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝''', font=("Helvatica", 10), bg=background, fg="white", cursor="heart red", justify="center", anchor="w")
    ascii_art.place(x=75, y=300)

    acopyright = Label(root, text="© 2023 - Password Algorithms - Mehmet Kahya", font=("Helvetica", 12, "bold"), bg=background, fg="white")
    acopyright.place(x=110, y=480)

    credit = Button(root, text="Credits", font=("Helvetica", 10, "bold"), bg=background, fg="black", command=credits, bd=0)
    credit.place(x=430, y=478)
mainScreen()



update_time()  # Start updating the time
root.mainloop()
