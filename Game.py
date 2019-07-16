import json
import random
import Depot
from Depot import cword
from Depot import Bannounce
from Depot import sword
from Depot import bonuses
from Depot import RouletteCases
from Depot import colorlist


#GUESS&OR&BET
#SELECT&A&BORING&LANGUAGE&GAME
#OR&PLAY&AT&LE&CASINO

class Game:
    bet = 0
    minbetx = mbx = 0.0
    roundx = rx = 0
    winoperator = ' '
    pxnumber = ' '
    pxcolor = ' '
    pxbetcolor = " "

    def __init__(self):
        pass

#Winning Number Generator

    def usround(self):
        self.winoperator = random.choice(RouletteCases)
        print("The winning number is :" + str(self.winoperator))
        if int(self.winoperator) == int(self.pxnumber):
            print("Congrats ! Here's your money")
        else:
            print("Better luck next time !")

#Round Counter v1

    def newRound(self):
        #Round addr
        #Minbet increasing
        rx = 0
        rx += 1
        if rx == 1:
            self.mbx += 1.0
        elif 2 <= rx <= 4:
            self.mbx += 0.25
        elif 4 < rx <= 8:
            self.mbx += 0.5
        else:
            self.mbx += 1     
        Gameinfo = "Current Game Stats: Round[ {} ] | Min.Bet[ {} ] | Player[ {} ] | Credits[ {} ]"
        print(Gameinfo.format(rx, self.mbx, px, self.bet))

#Current Game Amount to Bet

    def currentRound(self):
        print("How many tokens are you gonna Bet this time ?")
        pxbet = input()
        pxbet = float(pxbet)
        while float(pxbet) >= 0.0 :
            if float(pxbet) < self.mbx:
                print(" In order to play, Please respect the minimum bet rule ")
                pxbet = input()
            elif float(pxbet) > float(self.bet):
                print(" Thats way too much for your wallet sir ")
                pxbet = input()
            else:
                self.bet = float(self.bet) - float(pxbet)
                print("You gambled " + str(pxbet) + " tokens this round")
                break

        print("Which number do you want to gamble on ?")
        self.pxnumber = input()
        while int(self.pxnumber) >= 0:
            if 0 <= int(self.pxnumber) < 37:
                print("You gambled on the number " + str(self.pxnumber))
            else:
                print(" You must chose a number between 0 and 36 ")
                self.pxnumber = input()
            break

#Gambling Mode Picker v1

        print("Do you want to gamble on a color ? [Red|Black|No] ")
        self.pxcolor = input()
        for self.pxcolor in colorlist:
            if (self.pxcolor == "red, Red"):
                print("How many tokens do you want to gamble on Red ?")
                self.pxbetcolor = input()
            elif (self.pxcolor == "black, Black"):
                print("How many tokens do you want to gamble on Black ?")
                self.pxbetcolor = input()
            else:
                self.pxcolor = "no, No"
                print("Alright no color-gambling this time")
            break

#Game Function

    def guess_or_bet(self):
        print("Guess or Bet ?")
        pick = input()

        #Player selected Guess---------------------------------------------------------------------------------------------------

        if pick == "Guess":
            for x in cword:
                if x == "cannabise":
                    print("thats illegal")
                    continue
                else:
                    print(x)
            print("What's Illegal ?")
            x = input()
            while x != sword:
                print("Not Correct. Try Again:")
                x = input()
            if x == sword:
                print("Correct ! The full list was :")
                print(cword)

        #Player selected Guess---------------------------------------------------------------------------------------------------

        #Player selected Bet-----------------------------------------------------------------------------------------------------

        elif pick == "Bet":
            print("Please type your starting bet [Up to 100 Tokens]")
            bet = input()
            bet = float(bet)
            if bet <= 10:
                self.bet = float(bet) * bonuses[0]
                print(Bannounce)
                print(self.bet)
            elif 10 < bet <= 25:
                self.bet = float(bet) * bonuses[1]
                print(Bannounce)
                print(self.bet)
            elif 25 < bet <= 50:
                self.bet = float(bet) * bonuses[2]
                print(Bannounce)
                print(self.bet)
            elif 50 < bet <= 75:
                self.bet = float(bet) * bonuses[3]
                print(Bannounce)
                print(self.bet)
            elif 75 < bet <= 100:
                self.bet = float(bet) * bonuses[4]
                print(Bannounce)
                print(self.bet)
            else:
                print("Messing with the ksino ? Try beating us bigboy")
                self.bet = 1

            self.newRound()   
            self.currentRound()
            self.usround()

        #Invalid Selection
        
        else:
            print("Enter a valid pick")

        #Load Function

     #Player selected Bet-----------------------------------------------------------------------------------------------------

#Setup

print("Hey Player, what is your name ?")
px = "    "
px = input()
if px.strip():
    game = Game()
    game.guess_or_bet()
else:
   print("Invalid Player Name")