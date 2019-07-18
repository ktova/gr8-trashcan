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
    rx = 0
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
    number = 0
    context = ""
    multipler = 0
    powerbet = 0
    gain = 0
    endround = 1

    def __init__(self, number):
        self.number = number
        pass

    def roundwin(self):
        self.endround = 1
        if self.multipler == 2:
            self.powerbet == 2
            self.gain = float(self.pxmisebet) * float(self.powerbet)
            self.bet = float(self.bet) + float(self.gain)
        elif self.multipler == 3:
            self.powerbet == 3
            self.gain = float(self.pxmisebet) * float(self.powerbet)
            self.bet = float(self.bet) + float(self.gain)
        elif self.multipler == 36:
            self.powerbet == 36
            self.gain = float(self.pxmisebet) * float(self.powerbet)
            self.bet = float(self.bet) + float(self.gain)
        else:
            return 'error invalid win'
        print("Congrats you won this round !")
        print("Your new amount of credits is : " + str(self.bet))

    def roundloss(self):
        self.endround = 1
        self.bet = float(self.bet) - float(self.pxmisebet)
        print("Unlucky, you did bet on the wrong number. Better luck next time !")
        print("Your new amount of credits is : " + str(self.bet))
        print(self.endround)

    def credits_checker(self):
        if float(self.pxmisebet) > float(self.bet) :
            self.checked = 0
            return self.checked
        else:
            self.checked = 1
            return self.checked


    def singlenumpicker(self):
        """Gamble on single numbers"""
        self.context = "singlenumber"
        print("Which number do you want to gamble on ?")
        self.pxnumber = input()
        while int(self.pxnumber) >= 0:
            if 0 <= int(self.pxnumber) < 37:
                print("You gambled on number " + str(self.pxnumber))
            else:
                print(" You must chose a number between 0 and 36 ")
                self.pxnumber = input()
            break
        self.confirmise()

    def colorpicker(self):
        """Gamble on colors"""
        self.context = "color"
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
             print("You gambled " + str(self.pxmisebet) + " tokens")
             return self.pxmisebet
        else:
             print("You can't bet more than " + str(self.bet) + " tokens")
        self.mise()


    def confirmise(self):
    #"""Check if player respects betting rules"""
        print("How many tokens are you gonna bet ?")
        pxmisebet = float(input())
        while float(pxmisebet) >= 0.0 :
            if float(pxmisebet) < self.mbx:
                print(" In order to play, Please respect the minimum bet rule ")
                pxmisebet = input()
            elif float(pxmisebet) > float(self.bet):
                print(" Thats way too much for your wallet sir ")
                pxmisebet = input()
            else:
                self.bet = float(self.bet) - float(pxmisebet)
                print("You gambled " + str(pxmisebet) + " tokens this round")
                break  
        self.credits_checker()
        self.mise()      


    def mise(self):
        """Retrieve credits when tokens are gambled"""
        if float(self.pxmisebet) > 0:
            self.bet = float(self.bet) - float(self.pxmisebet)
        else: 
            return 'error 400'


    def usround(self):
        """Winning Number Generator
        Generates a random number then calculates
        said number color, evenodd, row and column"""
        self.winoperator = int(random.choice(rouletteCases))
        print("The winning number is : " + str(self.winoperator))
        #setattr(self.winoperator, Game, self.number)
        #Case.is_even(self.winoperator)
        #Case.color(self.winoperator)
        #Case.row(self.winoperator)
        #Case.column(self.winoperator)
        #Case stats checker ends^
        if self.context == "singlenumber":
            if int(self.winoperator) == int(self.pxnumber):
                self.roundwin()
            else:
                self.roundloss()
        #elif self.context == "color":
            #Case.color(self.winoperator)
        else:
            print("Unexpected Error")
            return 'Error404'
        

    def newRound(self):
        """Round Counter v1"""

        self.rx += 1
        if self.rx == 1:
            self.mbx += 1.0
        elif 2 <= self.rx <= 4:
            self.mbx += 0.5
        elif 4 < self.rx <= 8:
            self.mbx += 1.0
        else:
            self.mbx += 2.0    
        Gameinfo = "Current Game Stats: Round[ {} ] | Min.Bet[ {} ] | Player[ {} ] | Credits[ {} ]"
        print(Gameinfo.format(self.rx, self.mbx, px, self.bet))


    def currentRound(self):
        """Current Game Amount to Bet"""
#Gambling Mode Picker v1
        print("Which format do you want to gamble on ? ")
        print(" [1] Color (1:2) | [2] Even/Odd (1:2) | [3] Dozen (1:3) | [4] Sixt (1:6) | [5] Square (1:9) | [6] Double (1:18) | [7] Single (1:36) ")
        self.gamepicker = str(input()).lower()
        while self.gamepicker is not 'null':
            if self.gamepicker == "color":
                self.colorpicker()
                break
            elif self.gamepicker == "single":
                self.singlenumpicker()
                break
            else:
                print(self.gamepicker)
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

            while self.endround in range(0,2):
                if self.endround == 1:
                    self.newRound()
                    self.currentRound()
                    self.usround()
                    self.endround == 0
                else:
                    print(self.endround)
                    print('error')

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
    game = Game(0)
    game.guess_or_bet()
else:
   print("Invalid Player Name")