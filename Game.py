import json
import random
import Depot
from Depot import cword
from Depot import Bannounce
from Depot import sword
from Depot import bonuses
from Depot import Case
from Depot import rouletteCases
from Depot import list_of_cases


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
    pxmisebet = 0
    pxbet = ' '
    checked = 1

    def __init__(self):
        pass

    def credits_checker(self):
        if float(self.pxmisebet) > float(self.bet) :
            self.checked = 0
            return self.checked
        else:
            self.checked = 1
            return self.checked

    def colorpicker(self):
        """Gamble on colors"""
        colors = {
            "red": "Red",
            "black": "Black"
        }
        print("What color do you want to gamble on ? [ red | black ]")
        pxcolor = input().lower()
        try:
            print(f"How many tokens do you want to gamble on {colors[pxcolor]} ?")
            self.pxmisebet = float(input())
        except:
            print("Error, that's not a valid color")

        self.credits_checker()
        if self.checked == 1:
             print("You gambled" + str(self.pxmisebet))
             return self.pxmisebet
        else:
             print("You can't bet more than " + str(self.bet) + " tokens")

    def mise(self):
        """Retrieve credits when tokens are gambled"""
        if float(self.pxbet) > 0:
            self.bet = float(self.bet) - float(self.pxbet)
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
#Gambling Mode Picker v1
        print("Which format do you want to gamble on ? ")
        print(" [1] Color (1:2) | [2] Even/Odd (1:2) | [3] Dozen (1:3) | [4] Sixt (1:6) | [5] Square (1:9) | [6] Double (1:18)")
        self.gamepicker = input()
        for self.gamepicker in range(1,7):
            if self.gamepicker == 1:
                self.colorpicker()
                break
            else:
                print("Please chose a valid Gamemode")
                self.gamepicker = input()

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
            #self.usround()

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