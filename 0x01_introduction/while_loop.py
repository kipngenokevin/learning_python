#!/usr/bin/python3
y = 1
while y < 10:
    print("Value of y:", y)
    if y == 5:
        print("The Loop is at 5 and will continue")
        y += 1
        continue
    if y == 8:
        print("Loop is about to break here")
        break
    y += 1
