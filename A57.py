try:
    age = int(input("Enter your age: "))
    if(age<18):
        raise ValueError
    else:
        print("Your age is valid")
except ValueError:
    print("Your age is not valid")