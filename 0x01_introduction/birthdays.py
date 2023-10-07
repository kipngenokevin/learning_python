#!/usr/bin/python3
age = eval(input("Kindly enter your age: "))
if (age >= 1) and (age <= 18):
    print("Your birthday is important")
elif (age == 21) or (age == 50):
    print("Your birthday is important")
elif not(age < 65):
    print("Your birthday is important")
else:
    print("Your birthday is not that important")
