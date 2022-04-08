import random
import time
from os import system
from typing import get_origin

#Intro of Game/ Greeting User
print("****************Hangman****************")
name=input("Enter Your Name : ")
print(f"Hello {name}, Wecome to Hangman")

print("Loading Please Wait.",end="")
time.sleep(2)
print(".",end="")
time.sleep(2)
print("..",end="")
time.sleep(1)
print("...",end="")
system('cls')
print("Let's Play")

#All variable defintion need in game, define globally for required one
def hangmanTool():
    global word
    global originalWord
    global guessWord
    global length
    global user_Guessed
    global count
    wordList=["book","january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants","anime","laptop","program"]
    word=random.choice(wordList)
    originalWord=word
    length=len(word)
    guessWord="_"*length
    user_Guessed=[]
    count=0
    if length<=5:
        hint=random.sample(word,2)
    elif length>5:
        hint=random.sample(word,3)
    print("Hint : "+str(hint))

#Function to Terminate/exit the game
def hangmanTerminate():
    print("\nPlay Again? : \nYes -> y\nNo -> n :")
    userAct=input()
    if userAct=="y":
        hangmanTool()
        Hangman()
    elif userAct=="n":
        print("Hope You Like It.THANKS for Playing")
        exit()
        
    else:
        print("Wrong Input.Please try agian...")
        hangmanTerminate()


#Game Working tool 
def Hangman():
    global word
    global originalWord
    global guessWord
    global length
    global user_Guessed
    global count
    print(f"You have to choose : {guessWord}")

    userGuess=input("Enter your guess : ")
    userGuess=userGuess.strip()
    if len(userGuess)>=2 or len(userGuess)==0:
        print("***you can guess only 1 latter at a time***")
        Hangman()
    elif userGuess in word:
        user_Guessed.extend(userGuess)
        index=word.find(userGuess)
        word=word[:index]+"_"+word[index+1:]
        guessWord=guessWord[:index]+userGuess+guessWord[index+1:]
    elif userGuess in user_Guessed:
        print("!!!You have already selected this character.Try another character")
    else:
        count+=1
        if count==1:
            time.sleep(1)
            print('''
             ____
            |    |
            |
            |
            |
            |
            |
          __|__
            ''')

        elif count==2:
            time.sleep(1)
            print('''
             ____
            |    |
            |    |
            |
            |
            |
            |
          __|__
            ''')
        elif count==3:
            time.sleep(1)
            print('''
             ____
            |    |
            |    |
            |    |
            |
            |
            |
          __|__
            ''')
        elif count==4:
            time.sleep(1)
            print('''
             ____
            |    |
            |    |
            |    |
            |    |
            |
            |
          __|__
            ''')
        elif count==5:
            print('''
             ____
            |    |
            |    |
            |    |
            |    |
            |    O
            |   / \  \n
            |   /|\ \n
          __|__
            ''')
            time.sleep(3)
            system('cls')
            print("You Loss!! \nYou are Hanged!! (x_x) \nThe Hangman Word : "+originalWord)
            hangmanTerminate()
        if count<5:
            print("You have "+str(5-count)+" moves left")
    if word=="_"*length:
        system('cls')
        print("Wow!! Congratulations You Won")
        hangmanTerminate()
    Hangman()

hangmanTool()
Hangman()