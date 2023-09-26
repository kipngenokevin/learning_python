#first python program
print("Hello there")
#ask user for their name
name = input("What is your name? ")
#greet them nicely
print("Nice to meet you", name)
#ask user for age
age = input(f"{name} how old are you? ")
age = int(age)
if age >= 18:
    #verify is they have an id
    response = input("Do you have an ID number? ")
    #enter ID number
    if response.lower() == "yes":
        #process ID number
        id_number = input(f"{name} enter your ID number: ")
        print(f"Your qualify to apply {name}")
    else:
        print("Try another way")
        #confirm application is successful upon having an id
else:
    #ask user to try another way if they don't have an id
    print("Do you have a birth certificate or passport?")
    #provide option for birth cert or passport
    option = input("Enter 1 to choose birth certificate or 2 for passport: ")
    option = int(option)
    #confirm correct input from user
    while option != 1 and option != 2:
        option = input("Kindly confirm 1 for birth certificate of 2 for passport: ")
        option = int(option)
        #complete application upon having one of these
    if option == 1:
        birthc = input("Enter your birth certificate number: ")
    if option == 2:
        passport = input("Enter your passport number: ")
    #if they have neither, tell the user they have not met all the requirements
    #confirm that the application is successful
    print(f"You qualify to apply {name}")
