import random

hands = {"r":"Rock", "p": "Paper", "s": "Scissors","e": "exit"}
ai_hands = {"r": "Rock", "p": "Paper", "s":"Scissors" }

print( "Welcome to Rock, Paper, Scissors" )
print( "This is a game of wits, human vs machine." )
print( "You may also concede defeat by pressing e")

game_on = True
while game_on:

    x = input("Choose your hand, of rock, paper, or scissors by typing r,p or s:")
    ai_hand = random.choice(list(ai_hands))

    if x == "r":
        print ("You play Rock")
    elif x == "p":
        print ("You play Paper")
    elif x == "s":
        print ("You play Scissors")
    elif x == "e":
        print ("GG")
        game_on = False
        break
    else:
        print("Admit defeat and press e, or give it your best shot and enter r, p, or s:")

    if ai_hand == "r":
        print("I play Rock")
    elif ai_hand == "p":
        print("I play Paper")
    elif ai_hand == "s":
        print("I play Scissors")

    if x == ai_hand:
        print ("Draw")
    elif x == "r" and ai_hand == "p":
        print("Paper covers Rock: You lose")
    elif x== "p" and ai_hand == "r":
        print("Paper covers Rock: You Win!")
    elif x == "s" and ai_hand == "r":
        print("Rock smahes Scissors: you lose")
    elif x == "r" and ai_hand == "s":
        print("Rock smashes Scissors: You Win!")
    elif x == "p" and ai_hand == "s":
        print("Scissors cuts Paper: You lose")
    elif x == "s" and ai_hand == "p":
        print("Scissors cuts Paper: You Win!")



    #if x != list.item:player_hand

    #   def game(human_player,ai_player):
    #      if human_player.player_hand

    #human players turn

    #ai_players turn


    #ai_player =
    #input ("press enter to continue")