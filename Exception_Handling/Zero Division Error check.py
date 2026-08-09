try:
    o=int(input("enter a number: "))
    p=int(input("Enter your second number: "))
    c=o/p
    print("the answer is :",c)
except ZeroDivisionError:
    print("you cannot divide a number by zero")
finally:
    print("this is the end of the program") 