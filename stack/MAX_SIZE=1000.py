MAX_SIZE=1000
stack=[0 for i in range(MAX_SIZE)]
top=0
def push():
    global stack,top
    x=int(input("Enter an element to push into the stack: "))
    if top>=MAX_SIZE:
        print("Cannot push into the stack , stack is full")
    else:
        stack[top]=x
        top+=1
def pop():
    global stack,top
    if top==0:
        print("Cannot pop from the stack , stack is empty")
    else:
        top-=1
        print("Popped element is:",stack[:top+1])
#____main______#
while True:
    print("1. Push an element into the stack")
    print("2. Pop an element from the stack")
    print("3. Print the stack")
    print("4. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        print("Stack elements are:",stack[:top])
    elif choice==4:
        break
    else:
        print("Invalid choice , please try again")