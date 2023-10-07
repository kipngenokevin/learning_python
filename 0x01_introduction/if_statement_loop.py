#!/usr/bin/python3
while True:
    try:
        x = int(input("Please enter an integer: "))
        print("Integer successfully captured, you entered", x)
        y = input("Is this correct? Press enter to confirm, otherwise enter the new value: ")
        if y != "":
            while True:
                try:
                    int(y)
                    x = y
                    break
                except ValueError:
                    print("Whelp, that didn't work, let's try this again")
                    y = input("Enter your new integer: ")
        break
    except ValueError:
        print("Whelp, that didn't work, let's try this again")
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('The value you entered is Zero')
elif x > 0:
    print("The value you entered is more than Zero")    
