def http_error(status):
    match status:
        case 400: 
            print("Bad Request")
        case 404:
            print("Not Found")
        case 418:
            print("I am a teapot")
        case _:
            print("Something is wrong with the internet")
