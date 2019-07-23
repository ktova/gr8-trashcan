import django
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
from Depot import f1,f2,f3,d1,d2,d3

class Game:
    rx = 0
    bet = 0
    minbetx = mbx = 0.0
    roundx = rx = 0
    winoperator = ' '
    pxnumber = ' '
    pxcolor = ' '
    pxodeven = ''
    pxbetcolor = " "
    pxhalf = " "
    pxdozen = 1
    gamepicker = ' '
    gameapprove = " "
    pxmisebet = 0
    pxbet = ' '
    halfbet = 0
    checked = 1
    number = 0
    context = " "
    multipler = 1.0
    powerbet = 1.0
    gain = 1.0
    endround = 1
    pickedpair = ''
    pickedtrio = ''
    casecolor = ''
    newOD = ''
    co = ' '
    ode = ' '
    evo = ' '
    col = 1
    doz = 1

    def __init__(self, number):
        self.number = number
        pass

    def roundwin(self):
        """Return win"""
        self.endround = 1
        if int(self.multipler) == 2:
            self.gain = float(self.pxmisebet) * int(self.multipler)
            self.bet = float(self.bet) + float(self.gain)
        #Gain for 3x multiplers
        elif int(self.multipler) == 3:
            self.gain = float(self.pxmisebet) * float(self.multipler)
            self.bet = self.bet + self.gain
        #Gain for trios
        elif int(self.multipler) == 12:
            self.gain = float(self.pxmisebet) * float(self.multipler)
            self.bet = self.bet + self.gain
        #Gain for pairs
        elif int(self.multipler) == 18:
            self.gain = float(self.pxmisebet) * float(self.multipler)
            self.bet = self.bet + self.gain
        #Gain for single numbers 0 included
        elif int(self.multipler) == 36:
            self.gain = float(self.pxmisebet) * float(self.multipler)
            self.bet = self.bet + self.gain
        else:
        #Debugg
            print("multipler: " + str(self.multipler))
            print("powerbet: " + str(self.powerbet))
            print("gains: " + str(self.gain))
            print("Error distributing the gains")
            return 'error invalid win'
        print("Congrats you won this round !")
        print("Your new amount of credits is : " + str(self.bet))

    def roundloss(self):
        """Return loss"""
        self.endround = 1
        print("Unlucky, you did bet on the wrong number. Better luck next time !")
        print("Your new amount of credits is : " + str(self.bet))

    def roundnul(self):
        self.endround = 1
        print("Unfortunately this round is not a win nor a lose for you, half your bet has been returned to your credits")
        self.gain = float(self.pxmisebet) / 2 
        self.bet = self.bet + self.gain

    def credits_checker(self):
        """Checks if player is allowed to bet"""
        if float(self.pxmisebet) > float(self.bet) :
            self.checked = 0
            return self.checked
        else:
            self.checked = 1
            return self.checked

    def halfpicker(self):
        """Gamble on the first 18s number or the last 18s"""
        self.context = "half"
        self.multatr()
        halfies = {
            "first" : "first half",
            "last" : "last half"
        }
        print("Do you want to gamble on the first half (1-18) numbers or the last half (19-36) ?")
        self.pxhalf = str(input().lower())
        while (self.pxhalf) != 0:
            if self.pxhalf == "first":
                self.halfbet = 1
                print(f"How many tokens are you gonna bet on the {halfies[self.pxhalf]} ?")
                self.confirmise()
                break
            elif self.pxhalf == "last":
                self.halfbet = 2
                print(f"How many tokens are you gonna bet on the {halfies[self.pxhalf]} ?")
                self.confirmise()
                break
            else:
                print("Please select a valid half")
                self.pxhalf = str(input().lower())

    def singlenumpicker(self):
        """Gamble on single numbers"""
        self.context = "singlenumber"
        self.multatr()
        print("Which number do you want to gamble on ?")
        self.pxnumber = input()
        while int(self.pxnumber) >= 0:
            if 0 <= int(self.pxnumber) < 37:
                print("You gambled on number " + str(self.pxnumber))
            else:
                print(" You must chose a number between 0 and 36 ")
                self.pxnumber = input()
            break
        print(f"How many tokens are you gonna bet on {[self.pxnumber]}")
        self.confirmise()

    def doublenumpicker(self):
        """Gamble on two numbers"""
        self.context = "doublenumbers"
        self.multatr()
        print("Notes: Only pairs of following numbers are allowed e.g. 1 & 2 | 35 & 36")
        print("What is the first number of the pair you want to Gamble on ?")
        self.pn1 = int(input())
        while self.pn1 >= 0 :
        #Pair Suggestion when number is 0 < n < 37
            if 1 <= self.pn1 <= 36 :
                self.multinumsugster()
                print("[1] Gamble on pair " + str(self.pn1) + "-" + str(self.pairprop1))
                print("[2] Gamble on pair " + str(self.pn1) + "-" + str(self.pairprop2))
                selectedpair = int(input())
                while selectedpair >= 0:
                    if selectedpair == 1:
                        self.pickedpair = self.pn1, self.pairprop1
                    elif selectedpair == 2:
                        self.pickedpair = self.pn1, self.pairprop2                       
                    else:
                        print("You must chose an existing pair")
                        selectedpair = int(input())
                    break

        #Pair Suggestion when number is 0
            elif self.pn1 == 0:
                self.multinumsugster()
                print("[1] Gamble on pair " + str(self.pn1) + "-" + str(self.pairprop1))
                print("[2] Gamble on pair " + str(self.pn1) + "-" + str(self.pairprop2))
                print("[3] Gamble on pair " + str(self.pn1) + "-" + str(self.pairprop3))
                selectedpair = int(input())
                while selectedpair >= 0:
                    if selectedpair == 1:
                        self.pickedpair = self.pn1, self.pairprop1                        
                    elif selectedpair == 2:
                        self.pickedpair = self.pn1, self.pairprop2                       
                    elif selectedpair == 3:
                        self.pickedpair = self.pn1, self.pairprop3                       
                    else:
                        print("You must chose an existing pair")
                        selectedpair = int(input())              
                    break
    #t srx la
            else:
                print("Please enter a valid number between 1 and 36")
                self.pn1 = int(input())
            break
 #calls bet input 
        print(f"How many tokens are you gonna bet on {self.pickedpair} ?")        
        self.confirmise()

    
    def trionumpicker(self):
        """"Gamble on three numbers"""
        self.context = "trionumbers"
        self.multatr()
        print("Notes: 3-numbers gambling according to American's roulette rules, you can only gamble on rows from the boardgame e.g. : 1-2-3 is allowed , 1-4-7 is not. ")
        print("What number do you want to gamble on ?")
        self.tn1 = int(input())
        while self.tn1 >= 0:
        #Trios Suggestion when number is 0 < n < 37
            if 1 <= self.tn1 <= 36 :
                self.multinumsugster()
                print("You are gonna gamble on the trio : " + str(self.tn1) + "-" + str(self.trioprop1) + "-" + str(self.trioprop2) + " are you ok with that ?")
                confirm = str(input().lower())
                if confirm == "yes":
                    self.pickedtrio = self.tn1, self.trioprop1, self.trioprop2
                else :
                    pass
        #Trios Suggestion when number = 0
            elif self.tn1 == 0:
                self.multinumsugster()
                print("[1] Gamble on trio " + str(self.trioprop1))
                print("[2] Gamble on trio " + str(self.trioprop2))
                print("[3] Gamble on trio " + str(self.trioprop3))
                selectedtrio = int(input())
                while selectedtrio >= 0:
                    if selectedtrio == 1:
                        self.pickedtrio = self.trioprop1
                    elif selectedtrio == 2:
                        self.pickedtrio = self.trioprop2
                    elif selectedtrio == 3:
                        self.pickedtrio = self.trioprop3
                    else:
                        print("You must chose an existing trio")
                        selectedtrio = int(input())
                    break
            else:
                print("Please enter a valid number between 1 and 36")
                self.tn1 = int(input())
            break
        print(f"How many tokens do you want to gamble on {self.pickedtrio} ?")
        self.confirmise()


    def multinumsugster(self):
        """Calculates pairs, trios, squares and sixts gambles"""
        #Pairs predict
        if self.context == "doublenumbers":              
            if self.pn1 == 0:
                self.pairprop1 = 1
                self.pairprop2 = 2
                self.pairprop3 = 3
                return self.pairprop1, self.pairprop2, self.pairprop3
            else:
                self.pairprop1 = self.pn1 + 1
                self.pairprop2 = self.pn1 - 1
                return self.pairprop1, self.pairprop2

        #Trios predict
        elif self.context == "trionumbers":
            if self.tn1 == 0:
                self.trioprop1 = (0, 1, 4)
                self.trioprop2 = (0, 2, 5)
                self.trioprop3 = (0, 3, 6)
                return self.trioprop1, self.trioprop2, self.trioprop3
            elif self.tn1 in f1:
                self.trioprop1 = self.tn1 + 1
                self.trioprop2 = self.tn1 + 2
                return self.trioprop1, self.trioprop2
            elif self.tn1 in f2:
                self.trioprop1 = self.tn1 + 1
                self.trioprop2 = self.tn1 - 1
                return self.trioprop1, self.trioprop2
            else:
                self.trioprop1 = self.tn1 - 1
                self.trioprop2 = self.tn1 - 2
                return self.trioprop1, self.trioprop2

        #Square predict
        #Sixt predict
        else:
            pass

    def oddevenpicker(self):
        """Gamble on Odd/Even numbers"""
        self.context = "oddeven"
        self.multatr()
        pairimpair = ("odd, even")
        print("Do you want to bet on an odd number or an even one ?")
        self.pxodeven = input().lower()
        if self.pxodeven in pairimpair:
            print(f"How many tokens do you want to gamble on {self.pxodeven} numbers ?")
            self.confirmise()
        else:
            print("Error thats not a valid value")


    def colorpicker(self):
        """Gamble on colors"""
        self.context = "color"
        self.multatr()
        colors = ("red, black")
        print("What color do you want to gamble on ? [ red | black ]")
        self.pxcolor = input().lower()        
        if self.pxcolor in colors:
            print(f"How many tokens do you want to gamble on {self.pxcolor} ?")
            self.confirmise()
        else:
            print("Error, that's not a valid color")

    def dozenpicker(self):
        """Gamble on dozens"""
        self.context = "dozens"
        self.multatr()
        print("Which dozen do you want to gamble on ?")
        self.pxdozen = int(input())
        while 0 < self.pxdozen:
            if 0 < self.pxdozen < 4:
                print(f"How many tokens do you want to gamble on Dozen n˚{self.pxdozen} ?")
                self.confirmise()
            else:
                print("You must chose a valid dozen. hint: there only are 3")
                self.pxdozen = (input())
            break

    def columnpicker(self):
        """Gamble on columns"""
        self.context = "columns"
        self.multatr()
        print("Which column do you want to gamble on ?")
        self.pxcol = int(input())
        while 0 < self.pxcol:
            if 0 < self.pxcol < 4:
                print(f"How many tokens do you want to gamble on Column n˚{self.pxcol} ?")
                self.confirmise()
            else:
                print("You must chose a valid column. hint: there only are 3")
                self.pxcol = (input())
            break

    def confirmise(self):
    #"""Check if player respects betting rules"""
        self.pxmisebet = float(input())
        while float(self.pxmisebet) >= 0.0 :
            if float(self.pxmisebet) < float(self.mbx):
                print(" In order to play, Please respect the minimum bet rule ")
                self.pxmisebet = float(input())
            elif float(self.pxmisebet) > float(self.bet):
                print(" Thats way too much for your wallet sir ")
                self.pxmisebet = float(input())
            else:
                print("You gambled " + str(self.pxmisebet) + " tokens this round")
                break  
        self.credits_checker()
        self.mise()      

    def multatr(self):
        if self.context == "singlenumber":
            self.multipler = 36.0
            return self.multipler
        elif self.context == "doublenumbers":
            self.multipler = 18.0
            return self.multipler
        elif self.context == "trionumbers":
            self.multipler = 12.0
            return self.multipler
        elif self.context == "square":
            self.multipler = 9.0
            return self.multipler
        elif self.context == "sixt":
            self.multipler = 6.0
            return self.multipler
        elif self.context == "dozens":
            self.multipler = 3.0
            return self.multipler
        elif self.context == "columns":
            self.multipler = 3.0
            return self.multipler
        elif self.context == "half":
            self.multipler = 2.0
            return self.multipler
        elif self.context == "color":
            self.multipler = 2.0
            return self.multipler
        elif self.context == "oddeven":
            self.multipler = 2.0
            return self.multipler
        else:
            print("error mutlipler")

    def mise(self):
        """Retrieve credits when tokens are gambled - will adapt for multiple bet per round"""
        if float(self.pxmisebet) > 0:
            self.bet = float(self.bet) - float(self.pxmisebet)
        else: 
            return 'error 400'


    def usround(self):
        """Winning Number Generator
        Generates a random number then calculates
        said number color, evenodd, row and column"""
        #Debugwinning
        #self.winoperator = int(1)

        self.winoperator = int(random.choice(rouletteCases))

        self.co = Case(self.winoperator).color()
        self.ode = Case(self.winoperator).is_even()
        self.doz = Case(self.winoperator).dozens()
        self.col = Case(self.winoperator).column()

        print("The winning number is : " + str(self.winoperator))
        print("Color: " + str(self.co) + " | " + "Even : " + str(self.ode) + " | " + " Dozen number " + str(self.doz) + " | " + " Column number " + str(self.col))

        #Case stats checker ends^
#1number
        if self.context == "singlenumber":
            if int(self.winoperator) == int(self.pxnumber):
                self.roundwin()
            else:
                self.roundloss()
#2number
        elif self.context == "doublenumbers":
            if int(self.winoperator) in self.pickedpair:
                self.roundwin()
            else:
                self.roundloss()
#3number
        elif self.context == "trionumbers":
            if int(self.winoperator) in self.pickedtrio:
                self.roundwin()
            else:
                self.roundloss()
#dozens
        elif self.context == "dozens":
            if self.pxdozen == 1:
                if int(self.winoperator) in d1:
                    self.roundwin()
                else:
                    self.roundloss()
            elif self.pxdozen == 2:
                if int(self.winoperator) in d2:
                    self.roundwin()
                else:
                    self.roundloss()
            elif self.pxdozen == 3:
                if int(self.winoperator) in d3:
                    self.roundwin()
                else:
                    self.roundloss()
            elif self.winoperator == 0:
                self.roundnul()
            else:
                print("Error 418 Coffeepot")
#columns
        elif self.context == "columns":
            if self.pxcol == 1:
                if int(self.winoperator) in f1:
                    self.roundwin()
                else:
                    self.roundloss()
            elif self.pxcol == 2:
                if int(self.winoperator) in f2:
                    self.roundwin()
                else:
                    self.roundloss()
            elif self.pxcol == 3:
                if int(self.winoperator) in f3:
                    self.roundwin()
                else:
                    self.roundloss()
            elif self.winoperator == 0:
                self.roundnul()
            else:
                print("Error 418 Coffeepot")
#high/low half
        elif self.context == "half":
            if self.halfbet == 1:
                if 1 <= int(self.winoperator) < 19:
                    self.roundwin()
                elif int(self.winoperator) == 0:
                    self.roundnul()
                else:
                    self.roundloss()
            elif self.halfbet == 2:
                if 18 < int(self.winoperator) < 37:
                    self.roundwin()
                elif int(self.winoperator) == 0:
                    self.roundnul()
                else:
                    self.roundloss()
            else:
                print("Unexpected Error")
                return 'Error411'
 #color      
        elif self.context == "color":
            self.casecolor = Case(self.winoperator).color()
            if self.casecolor == self.pxcolor:
                self.roundwin()
            elif self.casecolor == 0:
                self.roundnul()
            else:
                self.roundloss()
#odd/even
        elif self.context == "oddeven":

            if self.pxodeven == "odd":
                self.newOD = 'False'
            elif self.pxodeven == "even":
                self.newOD = 'True'
            else:
                print("Unexpected error")
                return 'Error 418'
            self.izeven = Case(self.winoperator).is_even()
            if str(self.izeven) == str(self.newOD):
                self.roundwin()
            elif self.winoperator == 0:
                self.roundnul()
            else:
                self.roundloss()

        else:
            print("Unexpected Error")
            return 'Error411'
        

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
        print('---------------------------------------------------------------------------------')
        print(Gameinfo.format(self.rx, self.mbx, px, self.bet))
        print('---------------------------------------------------------------------------------')


    def currentRound(self):
        """Current Game Amount to Bet"""
#Gambling Mode Picker v1
        print("Which format do you want to gamble on ? ")
        print(" ")
        print("[1] Single (1:36) | [2] Double (1:18) | [3] Triple (1:12) | [4] Square (1:9) | [5] Sixt (1:6) ")
        print(" ")
        print("[6] Dozen (1:3) | [7] Column (1:3) | [8] Half (1:2) | [9] Even/Odd (1:2) | [0] Color (1:2) ")
        print('--------------------------------------------------------------------------------------------------')
        if self.bet < self.mbx:
            print("Seems like you don't have enough tokens to play")
            print("You've lost today.")
        else:
            pass
        self.gamepicker = str(input()).lower()
        while self.gamepicker is not 'null':
            if self.gamepicker in ("color, 0"):
                self.colorpicker()
                break
            elif self.gamepicker in ("single, 1"):
                self.singlenumpicker()
                break
            elif self.gamepicker in ("double, 2"):
                self.doublenumpicker()
                break
            elif self.gamepicker in ("triple, 3"):
                self.trionumpicker()
                break
            elif self.gamepicker in ("dozen, 6"):
                self.dozenpicker()
                break
            elif self.gamepicker in ("column, 7"):
                self.columnpicker()
                break
            elif self.gamepicker in ("half, 8"):
                self.halfpicker()
                break
            elif self.gamepicker in ("even, odd, 9"):
                self.oddevenpicker()
                break
            else:
                print(self.gamepicker)
                print("Please chose a valid Gamemode")
                self.gamepicker = input()

    def guess_or_bet(self):
        """Load Game Function"""

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

        #Load Function

     #Player selected Bet-----------------------------------------------------------------------------------------------------


#Setup
#header

print("")
print("                                       –––––––––––––––––––––––––––––––––––––––––––––––––                    ")
print("                                      |                                                 |                   ")
print("                                      |                  Yeezus Casino                  |                   ")
print("                                      |                                                 |                   ")
print("                                       –––––––––––––––––––––––––––––––––––––––––––––––––                    ")
print("")
print("Hey Player, what is your name ?")
px = "    "
px = input()
if px.strip():
    game = Game(1)
    game.guess_or_bet()
else:
   print("Invalid Player Name, Autofilling")
   px = "Arouf"
   game = Game(0)
   game.guess_or_bet()