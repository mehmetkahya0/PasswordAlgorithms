# Password Generator
# Mehmet Kahya - Start: 11.08.2023 



# TODO: SOLVE LENGHT PROBLEM
import random
from colorama import Fore
import time
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

if EncodeType=="n":
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


lenght = int(input(Fore.RED + "Set the length of the password: "))
alternarive = int(input("How many passwords to generate: " + Fore.WHITE))


for i in range(alternarive):
    password = "".join(random.choice(characters) for _ in range(lenght))
    print(Fore.WHITE + f"generated password ->    " + Fore.BLUE + f"{password}")
    time.sleep(0.5)


