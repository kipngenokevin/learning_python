#program that writes prime numbers between 0 and 10
#initialize a variable n and assign it the value 0
n = 0
p = 0
#loop from 2 to 1000
for n in range(2, 1000):
#function to check whether it is a prime number
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=", ")
        p += n
print()
print("Sum of all prime numbers: ", p)
#if it is a prime number, print it out
