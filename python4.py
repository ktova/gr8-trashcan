import json
import python1
from python1 import cword, Bannounce, sword, bonuses

gamepicker  

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




        print("How many tokens are you gonna Bet this time ?")
        pxbet = float(input())
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