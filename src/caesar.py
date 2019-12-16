
#!/usr/bin/python3
'''
Assignment: Caesar Cipher Assn#0
Class: CS 1440
Professor: Falor, Erik
Student Name: Foos, Brandon
A-Number: A02267662
Date: Aug 30, 2019
Date-Completed: Sep 10, 2019

Assignment Description:
Subsititution cipher in which each letter in plain text is "shifted"
a certin number of places to decode cipher text.
 
@author Brandon Foos
@author https://BrandonFoos.com
@version 1.0

'''

import os

filename = None
# Shift a charactor a certin number of times and loop the next char after Z to A and leave special charaters alone.
def rotate(c, n):
    if c.islower():
        if ord(c) + n > ord("z"):
            return chr(ord(c) + n - 26)
        else:
            return chr(ord(c) + n)
    elif c.isupper():
        if ord(c) + n > ord('Z'):
            return chr(ord(c) + n - 26)
        else:
            return chr(ord(c) + n)
    else:
        return c

# Start with a line then break the line into a char then use rotate class to shift the correct amount of spaces
def unscramble(dist):
    print("\n\033[93mRotatation key: " + str(dist) + "\033[00m")
    with open(filename) as secret:
        for line in secret:
            for c in line:
                print(rotate(c, dist), end='')

# Stylized Divider to look nice
def divider():
    print("\033[96m+----------------------------------------------------+\033[00m")

# Asks user how they would like the tool kit program to decode the provided file
def attemptDecode():
    options = formInput('How would you like us to decode your file?\n - Type a number between 0-25 for a certin key \n - Type "All" for any any possiblitys\n - Type "exit" to close program',True).lower()
    if options == "all":
        for i in range(0, 26):
            unscramble(i)
            i = i - 1
    else:
        try:
            # Form validation
            if (int(options) > 25 or int(options) < 0):
                header("You have chosen a number out of bounds please choose a number between 0-25.")
                attemptDecode()
            unscramble(int(options))
        except:
            header("You have not submitted a vaild command\nplease refer to the instuctions below.")
            attemptDecode()
    print("\n")
    choices()

# Ask the user if they would like to contiue using the program
def choices():
    choiceOne = formInput("Would you like another decode attempt? Yes or No or Exit",True).lower()
    if choiceOne == "yes":
        choiceTwo = formInput("Would you like to load another file? Yes or No or Exit",True).lower()
        if choiceTwo == "yes":
            divider()
            main()
        elif choiceTwo == "no":
            attemptDecode()
        else:
            header("You have not submitted a propper response please answer in yes, no, or exit commands")
            choices()
    elif choiceOne == "no":
        leave()
    else:
        header("You have not submitted a propper response please answer in yes, no, or exit commands")
        choices()
        

# a way of having a uniformlly formated input box that support using "exit" to close the program at any time
def formInput(text,leaveOnEmpty):
    divider()
    userInput = input('\033[91m' + text + '\033[00m\n').lower()
    divider()
    if userInput == "exit" or userInput == "" and leaveOnEmpty:
        leave()
    return userInput

# Creates the program title
def header(text):
    divider()
    print("\033[92m" + text + "\033[00m")
    divider()

# asks the user if they are sure they would like to leave
def leave():
    userInput = formInput("You are about to leave hit enter to exit or type \"abort\" to stay \n",False)
    if userInput == "":
        exit()
    else:
        choices()


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    header("  Welcome to the the Caesar Cipher Decoding Tool-Kit\n      You may leave at any time by typing 'exit'")
    print("Your Current Directory: " + os.getcwd())

    # Prompts user to enter file name
    flag = True
    while(flag):
        global filename
        filename = formInput('Please Type A Secret Message File Location: ',False)
        if os.path.isdir(filename):
            header("Path: " + filename + "\t is a directory no filename was specifyed")
        elif os.path.exists(filename):
            flag = False
        else:
            header("File: " + filename + "\t was not found.")

    attemptDecode()
    choices()
print(filename)

main()
