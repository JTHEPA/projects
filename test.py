def life():
    user = int(input("how old are you? "))
    if user < 18:
        return print("you are too young")
    else:
        return print("you are young")
    return user
life()