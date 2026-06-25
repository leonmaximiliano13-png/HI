secret = 14

while True:

    number = int(input("guess the number: "))

    if number == secret:
        print("correct")
        break
    
    else:
        print("wrong")