def hello():
    print("Hello from check_module.py")
print("__name__ in check_module.py:", __name__)
if __name__ == '__main__':
    print("This script is being run as the main program")
else:
    print("This script is being imported as a module")
