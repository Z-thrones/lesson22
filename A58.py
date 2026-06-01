try:
    num1, num2 = eval(input("Enter two numbers , seperated with a comma like this: NUM1, NUM2:   "))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Divisio by Zero error!!!!")
except SyntaxError:
    print("The correct format is num1, num2. I TOLD YOU BEFORE!!!!!!!!! ")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what!")