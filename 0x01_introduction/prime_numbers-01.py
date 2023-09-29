#write a program that prints prime numbers for whatever range the user sets
#take user input
print("Hello. I am here to help you with prime numbers")
print("Kindly input a range of numbers you would like me to calculate your prime numbers")
i = input("First number in the range: ")
j = input("Second number in the range: ")
#convert user input into integers
i = int(i)
j = int(j)
p = 0
#function to print out prime numbers
if i > j:
    for n in range(j, i):
        is_prime = True
        for m in range(2, int(n ** 0.5) + 1):
            if n % m == 0:
                is_prime = False
                break
        if is_prime:
            print(n, end=" ")
        p += n
else:
    for n in range(i, j):
        is_prime = True
        for m in range(2, int(n ** 0.5) + 1):
            if n % m == 0:
                is_prime = False
                break
        if is_prime:
            print(n, end=" ")
        p += n
print()
print(f"Sum of all prime numbers in the range {i} and {j} is {p}")
