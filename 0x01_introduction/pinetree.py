#!/usr/bin/python3
height = int(input("How tall is the pine tree: "))
i = 0
m = height
while i < height:
    for j in range(m):
        print(" ", end = "")
    for h in range(i + 1):
        print("#", end = "")
    for k in range(i):
        print("#", end="")
    print()
    m -= 1
    i += 1
print((" " * (i - 1)), "#")
