import json
import random
import Depot
import Modesfunc
from Depot import cword
from Depot import Bannounce
from Depot import sword
from Depot import bonuses
from Depot import Case
from Depot import rouletteCases
from Depot import list_of_cases
from Modesfunc import pxmisebet
from Modesfunc import colorpicker

#yeezus casino

class Game:
    bet = 0
    minbetx = mbx = 0.0
    roundx = rx = 0
    winoperator = ' '
    pxnumber = ' '
    pxcolor = ' '
    pxbetcolor = " "
    gamepicker = ' '
    gameapprove = " "


    def __init__(self):
        pass

    def mise(self):
        """Retrieve credits when tokens are gambled"""

        if int(pxmisebet) > 0:
            self.bet = float(self.bet) - float(pxmisebet)
        else: 
            return 'error 400'

    def usround(self):
        """Winning Number Generator"""

        self.winoperator = random.choice(rouletteCases)
        print("The winning number is :" + str(self.winoperator))
        if int(self.winoperator) == int(self.pxnumber):
            print("Congrats ! Here's your money")
        else:
            print("Better luck next time !")

    def newRound(self):
        """Round Counter v1"""

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

    def currentRound(self):
        """Current Game Amount to Bet"""

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
                print("You gambled on number " + str(self.pxnumber))
            else:
                print(" You must chose a number between 0 and 36 ")
                self.pxnumber = input()
            break

#Gambling Mode Picker v1

        print("Which format do you want to gamble on ? ")
        print(" [1] Color (1:2) | [2] Even/Odd (1:2) | [3] Dozen (1:3) | [4] Sixt (1:6) | [5] Square (1:9) | [6] Double (1:18)")
        self.gamepicker = input()
        if self.gamepicker == str[1]:
            colorbet()
        elif self.gamepicker == str[2]:
            evenoddbet()
        elif self.gamepicker == str[3]:
            dozenbet()
        elif self.gamepicker == str[4]:
            sixtbet()
        elif self.gamepicker == str[5]:
            squarebet()
        elif self.gamepicker == str[6]:
            doublebet()
        else:
            print("Okay, I'm assuming that you're gambling on a single number then ;) ")

        print("Do you want to gamble on anything else ? [y/n]")
        self.gameapprove = input()

    def guess_or_bet(self):
        """Load Game Function"""

        print("Guess or Bet ?")
        pick = input().lower()

        #Player selected Guess---------------------------------------------------------------------------------------------------

        if pick == "guess":
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

        elif pick == "bet":
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