num=0
while num!=100:
    try:
        num1=int(input("Enter the 1'st number:"))
        num2=int(input("Enter the 2'nd number:"))
        divide=num1/num2
        print("The result of the division is:",divide)
        break
    except ZeroDivisionError:
        print("You cannot divide a number by zero")
    except ValueError:
        print("Please enter a valid number")    
    finally:
        print("This is the end of the program")