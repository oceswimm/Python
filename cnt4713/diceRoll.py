import random
def roll():
    for x in range(1):
        return (random.randint(1,6))
        
print("Welcome to the dice roller:")

answer =input("Would you like to roll a dice?\n")
while(1):
    if answer == "yes":
        print("It's a ",roll(),"!")
        answer = input("Do you want to do it again?\n")
    
    elif answer == "no":
        print("Sounds good, sad to see you leave!")
        break
