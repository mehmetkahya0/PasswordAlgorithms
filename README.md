# Password Generator and Checker (GUI and Terminal version)


[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fmehmetkahya0%2FPasswordAlgorithms%2F&label=VISITORS&countColor=%23263759)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fmehmetkahya0%2FPasswordAlgorithms%2F)

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![LeetCode](https://img.shields.io/badge/LeetCode-000000?style=for-the-badge&logo=LeetCode&logoColor=#d16c06)
![Coursera](https://img.shields.io/badge/Coursera-%230056D2.svg?style=for-the-badge&logo=Coursera&logoColor=white)
![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)
![Github-sponsors](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)

## Terminal Version
https://github.com/mehmetkahya0/PasswordGenerator/assets/84154488/f1b35a7b-3bff-416f-bd0d-63bfee0b1225

## GUI Version
https://github.com/mehmetkahya0/PasswordAlgorithms/assets/84154488/a42fcabc-2ac5-4737-bafb-e4d9d0ce3cc4




> [!IMPORTANT]
> Now, PasswordAlgorithms support Windows, MacOS, and Linux directly!



## Terminal version wiki
This is a password generator that can generate strong and secure passwords. It is written in Python and uses the `random` module to generate random characters. The `colorama` module is used to print text in different colors.

The code is very simple to understand. The first few lines import the necessary modules. Then, a variable called `characters` is created that contains all the characters that can be used in a password.

The next few lines print the title of the program and ask the user to enter the length of the password and the number of passwords to generate.

The `for` loop then iterates over the number of passwords to generate. In each iteration, a new password is generated by joining random characters from the `characters` variable. The password is then printed to the console.

The `time.sleep()` function is used to pause the program for 0.5 seconds between each password generation. This is done to make the program more user-friendly.

Here is a step-by-step explanation of the code:

1. The `random` module is imported.
2. The `colorama` module is imported.
3. A variable called `characters` is created that contains all the characters that can be used in a password.
4. The title of the program is printed.
5. The user is asked to enter the length of the password.
6. The user is asked to enter the number of passwords to generate.
7. A `for` loop iterates over the number of passwords to generate.
8. In each iteration, a new password is generated by joining random characters from the `characters` variable.
9. The password is printed to the console.
10. The `time.sleep()` function is used to pause the program for 0.5 seconds between each password generation.

## Gui version wiki:
This is a simple GUI application built with Python's Tkinter library. The application provides two main functionalities: password generation and password checking.

### Features
- **Password Generation:** The application can generate random passwords based on user preferences. Users can specify the length of the password and the number of alternative passwords to generate. They also have the option to include special characters in the password.

- **Password Checking:** The application can also check the strength of a given password. It provides information about the number of uppercase letters, lowercase letters, and digits in the password. It also estimates the time it would take to crack the password and gives a safety score from 0 to 5.

- **Have i been pwned** This function scans your password for all internet leaks and shows how many times it has been leaked.

> [!NOTE]
> I use **haveibeenpwned.com** api for this function.


> [!IMPORTANT]
> The 'safety_point' rating, where I show the strength of your password, is purely personal, not scientific.

### Usage
To run the application, simply execute the gui.py script with a Python interpreter. The application requires the Tkinter library, which is included in standard Python distributions.

### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### License
This project is under MIT license.



> _special thanks to @ayseguldemireel for better UI experiance._



