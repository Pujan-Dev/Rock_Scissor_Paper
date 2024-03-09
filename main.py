import random

def RPS(p1,p2):
    p1= p1.upper()
    p2 =p2.upper()
    if((p1== "R" and p2== "R" )or (p1== "S" and p2== "S" ) or (p1== "P" and p2== "P" )):
        print("TIE")
    # win wala condition
    elif((p1 == "R" and p2 == "S") or (p1== "P" and p2== "R" ) or (p1== "S" and p2== "P" )):
        print("Player1 wins")
        
    elif((p2 == "R" and p1 == "S") or (p2== "P" and p1== "R" ) or (p2== "S" and p1== "P" )):
        print("Player2 wins")
    elif (p1 == "Q"):
        quit()
    else:
        print("Invalid input")
            

# MAIN GAME 
game = True #for game on state
moves = ["R","S","P"] #for ai moves

# User instruction 
print("Welcome to Rock, Scissor,Paper Game\n")
print("Our task is to play as a player and try to win this game against an AI \nType R for Rock\nP for Paper\nS for Scissor\nQ to Exit the game.\n")
# to get player1 name 
Player1 = input("Enter player1 name:")

while(game):
    AI= random.randint(0,2)
    p2 = moves[AI]
    print(AI,p2)
    p1 = input(f"Now its, {Player1}'s time to Enter your choice:")
    RPS(p1,p2)
        



