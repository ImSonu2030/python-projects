
import time
import random
from os import name, system


# Welcome
name=input("Enter Your Name : ")
print(f"Hello {name}, Welcome To Dice Rolling Game")
print("Please wait, Loading.",end="")
time.sleep(2)
print("..",end="")
time.sleep(1)
print("...")
system('cls')
print("Let's Play\n**********Dice Rolling**********")


def terminateGame():
    print("Whould you Like to Play it again?\nYes -> y\nNo -> n : ")
    userAct=input()
    if userAct.lower()=="y":
        system('cls')
        Game()
    elif userAct.lower()=="n":
        system('cls')
        print("Hope You Enjoyed Playing Our Game :)\nTHANKS for Playing,\nFrom Team COder")
        exit()
    else:
        print("Wrong Input.Please Try Again")
        terminateGame()

def inputVal():
    global Dicelist
    face1='''
     ______
    |      |
    |  O   |
    |______|'''
    face2='''
     ______
    |      |
    |  O O |
    |______|'''
    face3='''
     ______
    |    O |
    |  O   |
    |O_____|'''
    face4='''
     ______
    | O O  |
    | O O  |
    |______|'''
    face5='''
     ______
    | O  O |
    |  O   |
    |_O__O_|'''
    face6='''
     ______
    | O O O|
    | O O O|
    |______|'''
    Dicelist=[face1,face2,face3,face4,face5,face6]


#Return Input value:
def Input():
    Val=random.randint(1,6)
    return Val


#Working Process game:
def Game():
    global Dicelist

    #Computer Turn
    print("Computer's Tern -> ")
    compTake1=Input()
    compTake2=Input()
    time.sleep(1)
    print(Dicelist[compTake1-1],Dicelist[compTake2-1])
    
    #User Turn
    print(name+"'s Turn ->")
    startG=input("Throw your Dice\nPress Enter : ")
    if startG=="":
        userTake1=Input()
        userTake2=Input()
    else:
        print("Wrong Input,Press Enter Button.\nTry Agian")
        time.sleep(1)
    time.sleep(1)
    print(Dicelist[userTake1-1],Dicelist[userTake2-1])

    compInpSum=compTake1+compTake2
    userInpSum=userTake1+userTake2

    if userInpSum==compInpSum:
        print("Tie!\n Play Agian")
        time.sleep(2)
        system('cls')
        Game()
    elif userInpSum>compInpSum:
        print("Yuhuu!! You Won :)")
        terminateGame()
    else:
        print("You Loss ; (")
        terminateGame()


inputVal()
Game()