import Game
import Depot
from Depot import rouletteCases
from Depot import list_of_cases
from Depot import Case
from Game import bet

pxmisebet = ' '

def mise():
    if int(pxmisebet) > 0:
        bet = float(bet) - float(pxmisebet)


#Gamble on colors
def colorpicker():
    colors = {
        "red": "Red",
        "black": "Black"
    }
    print("What color do you want to gamble on ? [ red | black ]")
    pxcolor = input().lower()
    try:
        print(f"How many tokens do you want to gamble on {colors[pxcolor]} ?")
        pxmisebet = input()
    except:
        print("Error, that's not a valid color")


#Gamble on odd/even
