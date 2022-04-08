import random
from os import system


#Class for taking system generated input
class computer:
    def __init__(self,value):
        self.compvalue=value
    def action(self):
        comp_take=random.choice(self.compvalue)
        return comp_take

#user input and game console
class user:
    def userAction(self):
        user_take=input("Choose Rock, Paper or Scissor\nEnter : ")
        user_take=user_take.lower()
        return user_take
    def game(val1,val2):
        if val1==val2:
            print("*****Tie, Please try again.")
        elif val1=="rock" and val2=="paper":
            print("You Won!!")
            print(f"Computer chosed : {val1}")
        elif val1=="rock" and val2=="scissor":
            print("You Loss!!")
            print(f"Computer chosed : {val1}")
        elif val1=="scissor" and val2=="paper":
            print("You Loss!!")
            print(f"Computer chosed : {val1}")
        elif val1=="scissor" and val2=="rock":
            print("You Won!!")
            print(f"Computer chosed : {val1}")
        elif val1=="paper" and val2=="scissor":
            print("You Won!!")
            print(f"Computer chosed : {val1}")
        elif val1=="paper" and val2=="rock":
            print("You Loss!!")
            print(f"Computer chosed : {val1}")
        else:
            print("Invalid Input. Please try again.")


#main function
if __name__=="__main__":
    while(1):
        comp_value=computer(["rock","paper","scissor"]) #intializing computer() class
        user_val=user()                                 #Intializing user() class
        comp_turn=comp_value.action()
        user_turn=user_val.userAction()
        #passing aruguments to game() method of user() class
        user_val=user.game(comp_turn,user_turn)   #TypeError: action() missing 1 required positional argument: 'self' 
                                                  # -> solution that i got for this error, when we pass an method and 
                                                  #    we have more than 1 argument we can remove self and just use required arguments
                                                  # In line 45 i passed 2 arguments but for game() method 3 arguments required self, 
                                                  # val1 and val2 i.e why it shows missing 1 arguments. 
                                                  # 
                                                  # 
                                                  #  
        userResp=input("Play again? \nYes -> y\nNo -> n :")
        #Game Termination
        if userResp=="y":
            system('cls')
            continue
        else:
            print("Thanks for Playing!!")
            exit()