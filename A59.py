value = False
while not value:
    try:
        n = int(input("Enter a number: "))
        while n % 2 == 0:
            print("Bye")
        value = True
        raise ValueError
    except ValueError:
        print("Invalid")