import json
import python1
from python1 import cword, Bannounce, sword, bonuses


def guess_or_bet():
    print("Guess or Bet ?")
    pick = input()

    # Player selected Guess

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

    # Player selected Bet

    elif pick == "Bet":
        print("lets do maths, please type your starting bet [10|25|50|100]")
        bet = m
        while m <= 25 :
                 bonuses = bonuses[0]
         if 25 < m <= 50:
                 bonuses = bonuses[1]
            elif 50 < m <= 75:
                 bonuses = bonuses[2]
            elif 75 < m <= 100:
                 bonuses = bonuses[3]
            else:
                 bonuses = bonuses[4]     
 
        bet = input()
        
        else:
            print("Don't mess with the casino, you're out")

    # Invalid Selection

    else:
        print("Enter a valid pick")


guess_or_bet()
