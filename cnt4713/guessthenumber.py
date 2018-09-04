import random

def generate():
    for x in range(1):
        return(random.randint(1,20))
def compare(x,y):
    if x == y:
        print("Good job!\nYou guessed it right!\n")
        return 1
    elif x>y:
        output= int(input("Too high! Try again:"))
        return output
    elif x<y:
        output = int(input("Too low! Try again:"))
        return output

   
answer = input("Welcome to the guessTheNumber game, do you want to play?(yes/no)\n")

while(1):
    if answer == "yes":
        x=generate()
        print(x)
        y=int (input("OK, guess a number between 1 and 20 included\n"))
        result= compare(y,x)
        while(1):
            if result == 1:
                break
            else:
                result = compare(result,x)
            
                
        answer = input ("Do you want to play again?(yes/no)\n")
    elif answer == "no":
               print("Ok, see you next time!")
               break
