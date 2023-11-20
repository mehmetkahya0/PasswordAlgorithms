# Password Generator
# Mehmet Kahya - Start: 11.08.2023 

import random
from colorama import Fore
import time


choice = int(input(Fore.BLUE +f'''  
    '''+Fore.RED+"WELCOME TO THE PASSWORD-ALGORITHMS \n   - Mehmet Kahya -"+Fore.BLUE+'''        

    <-- Select category --> 
    Password Generator [1]
    Password Chacker [2]
---> ''' + Fore.WHITE))


if choice == 1: # Password Generator
    print(Fore.GREEN + f'''
                |////////////////////////////////////|      
                |/// PASSWORD GENERATOR VERSION 2 ///|
                |///       MEHMET KAHYA           ///|
                |///                              ///|
                |////////////////////////////////////|
    ''' + Fore.WHITE)

    passwordList = ['']
    EncodeType = str(input(Fore.YELLOW + "Do you want spacial characters of your password? (~æ¨^~≈∂€ƒ),  (y/n)?  " + Fore.WHITE))


    if EncodeType=="y":
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-+*/=!&/()>£#$½§{[]}ğüşiöçĞÜŞİÖÇ@∑€®₺¥üiöπ¨~`æ´¬¨∆^ğƒ∂ßæ≈∫~µ≤≥÷|><|"

    elif EncodeType=="n":
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    else:
        print("try again")
        exit()

    lenght = int(input(Fore.RED + "Set the length of the password: "))
    alternarive = int(input("How many passwords to generate: " + Fore.WHITE))


    for i in range(alternarive):
        password = "".join(random.choice(characters) for _ in range(lenght))
        print(Fore.WHITE + f"generated password ->    " + Fore.BLUE + f"{password}")
        time.sleep(0.5)      

if choice == 2: # Password Checker
        print(Fore.GREEN + f'''
                |////////////////////////////////////|      
                |/// PASSWORD CHECKER VERSION 0.1 ///|
                |///       MEHMET KAHYA           ///|
                |///        20.11.2023            ///|
                |////////////////////////////////////|
    ''' + Fore.WHITE)
        
        password = input(Fore.GREEN + "Enter your password: " + Fore.WHITE)
        print("--------------------------------")
        time.sleep(0.250)

        #lenghtOfPassword = print("lenght of password: " + len(password))
        uppercaseInPassword = sum(1 for harf in password if harf.isupper())
        print(Fore.BLUE + f"number of uppercase letters: {uppercaseInPassword}")
        time.sleep(0.250)

        lowercaseInPassword = sum(1 for harf in password if harf.islower())
        print(f"number of lowercase letters: {lowercaseInPassword}")
        time.sleep(0.250)

        def check_password_safety(password):
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

            print(Fore.RED + f"safety point of your password (0-5): {safetyPoint}" + Fore.WHITE)
        check_password_safety(password)


