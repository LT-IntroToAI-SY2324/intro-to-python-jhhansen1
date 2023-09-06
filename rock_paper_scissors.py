# We will write a rock paper scissors game in class - Complete it in this file
import random 
userChoice=input("rock, paper, or scissors?")
gameOptions=["rock", "paper", "scissors"]
gameChoice=random.choice(gameOptions)
if (userChoice==gameChoice):
    print("you tied")
if (userChoice=="rock"):
    if(gameChoice=="paper"):
        print ("you lose")
    if(gameChoice=="scissors"):
        print ("you win")
if (userChoice=="paper"):
    if(gameChoice=="rock"):
        print ("you win")
    if(gameChoice=="scissors"):
        print ("you lose")
if (userChoice=="scissors"):
    if(gameChoice=="paper"):
        print ("you win")
    if(gameChoice=="rock"):
        print ("you lose")
 
