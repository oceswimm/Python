print("first attempt of using method")

def add(x,y):
    z=x+y
    return z

while (1):

    s=int(input("please enter an integer between 1 and 3\n"))
    
    
    if ((s==1) or (s==2) or(s==3)):
        print(s,"+", t," =",add(s,t))
    elif (s<1)or(s>3):
        print("sorry you entered a wrong integer")
        break
    t=int(input("pick a number to add to your integer\n"))
    contin=input("do you want to do another addition? (yes/no)\n")

    if contin=="no":
        print("Bye!")
        break    
    
