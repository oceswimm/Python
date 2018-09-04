input("just press Enter to read this mini game intro :)")
input("Hello, this is my first attempt to create some kind of a game...")
input("I know right, how weird is it for a game to directly talk to you?")
input("But let's not waste our time here.")
input("Your are currently in the hallway of a house, your goal?")
input("Get the hell out of here !! \nWhy? Because a serial killer is after you")
input("You have 4 options to move : forward ; backward ; left ; right")
input("Evertime you will tell me which direction to go i'll give \nyou a description of where you are")
input("Sounds good? Ok let's begin!")

def whichRoom(theList):
    if theList ==["forward","left"]:
        print("How can you be hungry when a serial killer wants to take away your life?! run ! You're in the Kitchen right now!")
        return 1
    elif theList == ["forward","forward"]:
        print("That was the easiest way to make it halfway! I'm proud :)")
        return 12
    elif theList ==["forward","left","forward"]:
        print("Woa woa woa, how can so many clothes be in a such restricted area?\nThis looks like a closet.. not an EXIT!")
        return 2
    elif theList ==["forward","left","forward","forward"]:
        print("Sorry but you can't go that way, you must try another direction!")
        return 0
    elif theList ==["forward","left","forward","right"]:
        print("You got out of the closet and you are now back in the hallway; you are right in the middle of this hallway\nThe point you started from is behind you")
        return 12    
    elif theList ==["forward","left","forward","left"]:
        print("Sorry but you can't go that way, you must try another direction!")
        return 0    
    elif theList == ["forward","right"]:
        print("I don't think it is time to watch TV... You're in the living room!")
        return 4
    elif theList == ["forward"]:
        print("I see you've listened to me ! Good job, you're still in the hallway but one step closer from the EXIT!")
        return 11
    elif theList ==["forward","right","forward"]:
        print("The bedroom is probably the most cliche place you could go to to hide from a serial killer, leave !")
        return 5
    elif theList==["forward","right","forward","left"]:
        print("There you go, you got out of the bedroom and you are now in the middle of the hallway, getting closer from the exit! Pick wisely your directions!")
        return 12
    elif theList==["forward","right","forward","forward"]:
        print("Sorry but you can't go that way, you must try another direction!")
        return 0
    elif theList==["forward","right","forward","right"]:
        print("Sorry but you can't go that way, you must try another direction!")
        return 0
    elif theList == ["forward","forward","forward"]:
        print("Good job! You're still in the hallway and even more closer to exit this mess!")
        return 13
    elif theList ==["forward","left","forward","right","forward"]:
        print("Hey! Nice, you're still in the hallway but the exit is getting closer...")
        return 13
    elif theList ==["forward","right","forward","left","forward"]:
        print("Hey! Nice, you're still in the hallway but the exit is getting closer...")
        return 13
    elif theList ==["forward","forward","right"]:
        print("Come on you're not making progress right now, you're in the bedroom get out of there")
        return 5
    elif theList ==["forward","forward","left"]:
        print("Come on you're not making progress right now, you're in the closet get out of there")
        return 2
    elif theList == ["forward","forward","forward","forward"]:
        print("Ok. Now it looks like you're cheating! have you already been in this house before ?? You can be out in 1 move!!")
        return 14
    elif theList ==["forward","left","forward","right","forward","left"]:
        print("Hey! Who ever told you that the restrooms where the most commong exit in a house?? ")
        return 3
    elif theList ==["forward","left","forward","right","forward","forward"]:
        print("Hey! Still in the hallway but You can be out in 1 move!!")
        return 14
    elif theList ==["forward","right","forward","left","forward","left"]:
        print("Hey! Who ever told you that the restrooms where the most commong exit in a house?? ")
        return 3
    elif theList ==["forward","right","forward","left","forward","forward"]:
        print("Hey! Still in the hallway but you can be out in 1 move!!")
        return 14
    elif theList == ["forward","forward","forward","forward","forward"]:
        print("YES YOU MADE IT")
        return 15
    elif theList == ["forward","forward","forward","forward","right"]:
        print("If you never wanna be done with this game that was the best move to do...You're in the office")
        return 6
    elif theList ==["forward","left","forward","right","forward","forward","forward"]:
        print("YES YOU MADE IT")
        return 15
    elif theList ==["forward","left","forward","right","forward","forward","right"]:
        print("If you never wanna be done with this game that was the best move to do...You're in the office")
        return 6
    elif theList ==["forward","right","forward","left","forward","forward","forward"]:
        print("YES YOU MADE IT")
        return 15
    elif theList ==["forward","right","forward","left","forward","forward","right"]:
        print("If you never wanna be done with this game that was the best move to do...You're in the office")
        return 6
    else:
        print("Sorry but this is not an exit...")
        return 0
#should be a checkpoint at middle of hallway and give hint to move forward if whichRoom =12 
print("\n\nI'm going to be nice and tell you that you must start by moving forward!")
theList = []
while (1):
    direction = input("Which direction do you want to choose?(type exit to stop the game)\n")
    if direction =="backward":
        theList.pop()
        whichRoom(theList)
        continue
    elif direction=="exit":
        print("Thanks for playing!")
        break
    theList.append(direction)
    print(theList)
    s=whichRoom(theList)
    if s == 12:
        print("\nOk you've made it halfway, so i'm giving you a hint, you should move forward.\n")
    elif s == 15:
        break
    
