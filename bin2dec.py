while True:
    user_input = input("Enter binary up to 8 digits: ")
    if (user_input.count("0")
     + user_input.count("1") != len(user_input)):
        print("Invalid input")
    elif (len(user_input) < 1 or len(user_input) > 8):
        print("Invalid string length")
    else:
        break

