#!/usr/bin/env python
import random
from random import randint
num=0
yes=""
no=""
while num<1:
    def score(number):
        if number=="Ace":
            theScore=1
        elif number=="King":
            theScore=13
        elif number =="Queen":
            theScore=12
        elif number == "Jack":
            theScore =11
        else:
            theScore = number
        return theScore

    def theCards():#defines which card is created
        number= random.randint(1,13)
        if number==1:
            theCard="Ace"
        elif number==13:
            theCard="King"
        elif number ==12:
            theCard="Queen"
        elif number == 11:
            theCard ="Jack"
        else:
            theCard = str(number)
        return theCard
    def theRobe():#defines the robe of the created card
        robe=("Clubs","Diamonds","Hearts","Spades")
        num= random.randint(0,3)
        theRobe = robe[num]
        return theRobe

    numbers=[]
    robes=[]

    def initiateHiddenCards():
        s=0

        while s<5:
            number = theCards()
            robe= theRobe()
            numbers.append(number)
            robes.append(robe)
            s+=1


    def get21(player,chosen):
        if player=="Ace":
            num1=1
        elif player=="King":
            num1=13
        elif player=="Queen":
            num1=12
        elif player=="Jack":
            num1=11
        else:
            num1=int(player)

        if chosen=="Ace":
            num2=1
        elif chosen=="King":
            num2=13
        elif chosen=="Queen":
            num2=12
        elif chosen=="Jack":
            num2=11
        else:
            num2 = int(chosen)
        add = num2+num1
        return add

 #will allow to print number associated to the robe
    def printcards(number):

        print('%8s|'% (numbers[number]))
        print('%8s|'% (robes[number]))
    def askUser():
        keepPlaying= input("Do you want to try again? (yes/no):")
        if keepPlaying=="no":
            contin=1
        else:
            contin=0
        return contin
        
    playerCard=theCards()
    playerRobe=theRobe()
    score=score(playerCard)
    l=[1,2,3,4,5]
    length=len(l)
    print("------------->Your card is",playerCard,"of",playerRobe,"<-------------")
    print("Initial score is",score)
    initiateHiddenCards()
   
    print("Now that you know your card, there are 5 cards that \nare available for you to pick:")

    print(l)

    choice =int(input("Which one do you want to choose?"))
    currChoice = choice-1
    chosen =numbers[currChoice]
    print("You picked a:")
    printcards(currChoice)
    #sets value of picked card to used
    l[currChoice]="used"
    numbers[currChoice]="used"
    robes[currChoice]="used"

    result=0
    while num<1:
        result=get21(playerCard,chosen)
        if result <21:
            print("Your result is: ",result)
            if len(l)>0:
                print("You are not at 21 yet, pick another card!:\n",l)

                newChoice=int(input("->"))
                
                theChoice= newChoice-1

                newChosen=numbers[theChoice]
                print("You picked a:")
                printcards(theChoice)
     #sets value of picked card to used
                l[theChoice]="used"
                numbers[theChoice]="used"
                robes[theChoice]="used"

               
        #updates both values to input in get21 function
                playerCard=result
                chosen = newChosen
                continue
            else:#if there are no more cards to chose from
                print("Sorry there are no more cards available...")
                num=askUser()
                if num == 0:
                    break
        #if result is 21 you win
        elif result==21:
            print("Congrats! You won!")
            num=askUser()
            if num ==0:
                break
        #handles the case where player loses
        else:
            print("Sorry you lost, you went over 21!! :(")
            print("The final score was:",result)
            num=askUser()
            if num==0:
                break
            
