global_var = 10 #This is a global variable
def my_function():
    print("Global variable", global_var)
def modify_glob():
    global global_var
    global_var += 5
print("Outside the module:", global_var)
