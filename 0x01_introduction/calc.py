#!/usr/bin/python3
# let the user enter a calculation
num1, ch, num2 = input("Kindly enter a calculation: ").split(" ", 2)
# store the input strings
num1 = int(num1)
num2 = int(num2)
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
else:
    print("unknown operand {}".format(ch))
    result = 0
# print out the result
print(f"{num1} {ch} {num2} = {result}")
