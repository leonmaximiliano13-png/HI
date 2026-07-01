def say_hello():
    print("Hello welcome to this program!")

def say_goodbye():
    print("Goodbye and thanks for using this program!")

while True:
    
    option = input("Type 1 to say hello, 2 to exit: ")

    if option == "1":
        say_hello()

    elif option == "2":
        say_goodbye()
        break

    else:
        print("Invalid option, please try again.")